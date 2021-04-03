# The MIT License (MIT)
#
# Copyright (c) 2021 William Cabrera
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from machine import Pin, SoftSPI, I2C
from random import randint
from mfrc522 import MFRC522 # https://github.com/vtt-info/MicroPython_MFRC522
from ssd1306 import SSD1306_I2C # https://github.com/stlehmann/micropython-ssd1306

# Configure RFID reader
sda = Pin(14, Pin.OUT)
sck = Pin(15, Pin.OUT)
mosi = Pin(16, Pin.OUT)
miso = Pin(17, Pin.OUT)
spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)
reader = MFRC522(spi, sda)
KEY = [255, 255, 255, 255, 255, 255]
BLOCK = 20

# Configure OLED Display
WIDTH = 128
HEIGHT = 64
i2c = I2C(1, scl=Pin(19), sda=Pin(18))
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)
oled.contrast(0)

# First print in terminal and display
print('Place Card In Front Of Device\n')
oled.text('Waiting for card', 0, 0)
oled.show()

# Infinite Loop
while True:
    (status, tag_type) = reader.request(reader.CARD_REQIDL) # Get the Tag Type
    if status == reader.OK:
        oled.fill(0)
        (status, raw_uid) = reader.anticoll() # Get de UID
        if status == reader.OK:
            # Print the Type and UID
            print('\nNew Card Detected')
            print('  - Tag Type: 0x{:x}'.format(tag_type))
            print('  - UID: 0x{:x}{:x}{:x}{:x}'.format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            oled.text('Tag Type: 0x{:x}'.format(tag_type), 0, 0)
            oled.text('UID: 0x{:x}{:x}{:x}{:x}'.format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]), 0, 12)
            if reader.select_tag(raw_uid) == reader.OK:
                if reader.auth(reader.AUTH, BLOCK, KEY, raw_uid) == reader.OK:
                    old_value = reader.read(BLOCK) # get the actual value in the block
                    new_value = randint(0, 255) # Set the new Value
                    print('Old Value: {}'.format(old_value[0]))
                    oled.text('Old Value: {}'.format(old_value[0]), 0, 24)
                    value = bytes([new_value, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    status = reader.write(BLOCK, value) # Set the new Value in the block
                    reader.stop_crypto1()
                    if status == reader.OK:
                        print('New value: {}'.format(new_value))
                        oled.text('New Value: {}'.format(new_value), 0, 36)
                    else:
                        print('FAILED TO WRITE DATA')
                        oled.text('FAILED TO WRITE', 0, 36)
                        oled.text("DATA", 0, 48)
                else:
                    print("AUTH ERROR")
                    oled.text("AUTH ERROR", 0, 36)
            else:
                print("FAILED TO SELECT TAG")
                oled.text("FAILED TO SELECT", 0, 36)
                oled.text("TAG", 0, 48)
    oled.show()
