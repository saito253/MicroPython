import machine
import ssd1306
import time

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0,sda=sda, scl=scl, freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("Hello everyone", 0, 5)
oled.show()
time.sleep(2)
oled.text("Welcome to my", 0, 15)
oled.text("blog", 10, 25)
oled.show()
time.sleep(2)
oled.text("Thank You", 0, 35)
oled.show()