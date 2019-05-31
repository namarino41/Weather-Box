#!/usr/bin/python
# -*- coding:utf-8 -*-

from internal.lib import epd4in2
from internal.lib import ui_builder
from internal.lib import weatherbox_client
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import sys
sys.path.append('internal/')
sys.path.append('../assets/')



def updateDisplay():
    forecast = weatherboxClient.getFull()

    currently_forecast = forecast['currently']
    daily_forecast = forecast['daily']
    hourly_forecast = forecast['hourly']

    ui = ui_builder.UIBuilder() \
        .date(datetime.today()) \
        .currently(currently_forecast) \
        .daily(daily_forecast) \
        .hourly(hourly_forecast) \
        .build()

#     epd = epd4in2.EPD()
#     epd.init()
#     epd.display(epd.getbuffer(ui))
#     epd.sleep()

    ui.show()

if __name__ == '__main__':
    global weatherboxClient
    weatherboxClient = weatherbox_client.WeatherboxClient()
    scheduler = BlockingScheduler()
    scheduler.add_job(updateDisplay, 'interval', hours=1)
    scheduler.start()

# import time
# from PIL import Image,ImageDraw,ImageFont
# import traceback

# try:
#     epd = epd4in2.EPD()
#     epd.init()
#     epd.Clear(0xFF)

#     # Drawing on the Horizontal image
#     Himage = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame

#     # Horizontal
#     print("Drawing")
#     draw = ImageDraw.Draw(Himage)
#     font24 = ImageFont.truetype("arial.ttf", 24)
#     draw.text((10, 0), 'hello world', font = font24, fill = 0)
#     draw.text((10, 20), '2.9inch e-Paper', font = font24, fill = 0)
#     draw.line((0, 0, 400, 300), fill = 0)
#     draw.line((0, 300, 400, 0), fill = 0)
#     draw.line((70, 50, 20, 100), fill = 0)
#     draw.rectangle((20, 50, 70, 100), outline = 0)
#     draw.line((165, 50, 165, 100), fill = 0)
#     draw.line((140, 75, 190, 75), fill = 0)
#     draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
#     draw.rectangle((80, 50, 130, 100), fill = 0)
#     draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
#     epd.display(epd.getbuffer(Himage))
#     time.sleep(2)

#     #Vertical
#    # draw = ImageDraw.Draw(Limage)
#    # font18 = ImageFont.truetype('arial.ttf', 18)
#    # draw.text((2, 0), 'hello world', font = font18, fill = 0)
#    # draw.text((2, 20), '2.9inch epd', font = font18, fill = 0)
#    # draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
#    # draw.line((10, 90, 60, 140), fill = 0)
#    # draw.line((60, 90, 10, 140), fill = 0)
#    # draw.rectangle((10, 90, 60, 140), outline = 0)
#    # draw.line((95, 90, 95, 140), fill = 0)
#    # draw.line((70, 115, 120, 115), fill = 0)
#    # draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
#    # draw.rectangle((10, 150, 60, 200), fill = 0)
#    # draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
#    # epd.display(epd.getbuffer(Limage))
#    # time.sleep(2)

#     print("drawing on image")

# #    image = Image.open("UI.png")
#    # draw = ImageDraw.Draw(image)
#    # draw.text((10, 10),"Come on, Morty, quick *BELCH* quick 20 minute adventure", fill=10)

#    # epd.display(epd.getbuffer(image))

#     #time.sleep(2)

#    # print("read bmp file on window")
#    # Himage2 = Image.new('1', (epd4in2.EPD_WIDTH, epd4in2.EPD_HEIGHT), 255)  # 255: clear the frame
#    # bmp = Image.open('100x100.bmp')
#    # Himage2.paste(bmp, (50,10))
#    # epd.display(epd.getbuffer(Himage2))
#    # time.sleep(2)

#     epd.sleep()

# except:
#     print('traceback.format_exc():\n%s',traceback.format_exc())
#     exit()
