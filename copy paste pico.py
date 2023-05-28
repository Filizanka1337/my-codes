import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

button1 = digitalio.DigitalInOut(board.GP15)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP16)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

while True:
    if not button1.value:
        kbd.press(Keycode.LEFT_CONTROL, Keycode.C)
        kbd.release_all()
        time.sleep(0.2)
    if not button2.value:
        kbd.press(Keycode.LEFT_CONTROL, Keycode.V)
        kbd.release_all()
        time.sleep(0.2)