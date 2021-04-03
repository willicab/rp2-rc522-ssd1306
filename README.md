# rp2-rc522-ssd1306
Read and write test with RC522 module on Raspberry Pi Pico

# Pin connection
## RFID-RC522
* SDA: GP14
* SCK: GP15
* MOSI: GP16
* SIMO: GP17
* GND: GND
* 3.3V: 3V3(OUT)

## SSD1306
* GND: GND
* VCC: 3V3(OUT)
* SCL: GP19
* SDA: GP18

# External Libraries
* https://github.com/vtt-info/MicroPython_MFRC522
* https://github.com/stlehmann/micropython-ssd1306

# License
The MIT License (MIT)

Copyright (c) 2021 William Cabrera

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
