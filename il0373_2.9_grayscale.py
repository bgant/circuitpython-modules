# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test script for 2.9" 296x128 grayscale display.

Supported products:
  * Adafruit 2.9" Grayscale
    * https://www.adafruit.com/product/4777
  """

import time
import busio
import board
import displayio
import adafruit_il0373

displayio.release_displays()

spi = busio.SPI(board.SCK, board.MOSI)  # Uses SCK and MOSI

# Feather M4
#epd_cs = board.D9
#epd_dc = board.D10

# FeatherS2
epd_cs = board.IO1  # 2.9" E-Ink FeatherWing ECS pin
epd_dc = board.IO3  # 2.9" E-Ink FeatherWing DC pin

display_bus = displayio.FourWire(
    spi, command=epd_dc, chip_select=epd_cs, baudrate=1000000
)
time.sleep(1)

display = adafruit_il0373.IL0373(
    display_bus,
    width=296,
    height=128,
    rotation=270,
    black_bits_inverted=False,
    color_bits_inverted=False,
    grayscale=True,
    refresh_time=1,
)

g = displayio.Group()

#f = open("/display-ruler.bmp", "rb")
#f = open("/29gray4.bmp", "rb")
f = open("/panda_head.bmp", "rb")
#f = open("/adabot_head.bmp", "rb")

pic = displayio.OnDiskBitmap(f)
t = displayio.TileGrid(pic, pixel_shader=displayio.ColorConverter())
g.append(t)

display.show(g)

display.refresh()

print("refreshed")

time.sleep(120)
