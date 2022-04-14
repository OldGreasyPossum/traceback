Exception in thread Thread-1:
Traceback (most recent call last):
  File "/usr/lib/python3.9/threading.py", line 954, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.9/threading.py", line 892, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 595, in fill
    value = self.parent._read()
  File "/usr/lib/python3/dist-packages/gpiozero/input_devices.py", line 702, in _read
    self.pin.function = 'input'
  File "/usr/lib/python3/dist-packages/gpiozero/pins/__init__.py", line 263, in <lambda>
    lambda self, value: self._set_function(value),
  File "/usr/lib/python3/dist-packages/gpiozero/pins/rpigpio.py", line 138, in _set_function
    GPIO.setup(self.number, self.GPIO_FUNCTIONS[value], self.GPIO_PULL_UPS[self._pull])
RuntimeError: Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)
Error in atexit._run_exitfuncs:
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/gpiozero/pins/pi.py", line 307, in _set_when_changed
    self._disable_event_detect()
  File "/usr/lib/python3/dist-packages/gpiozero/pins/rpigpio.py", line 232, in _disable_event_detect
    GPIO.remove_event_detect(self.number)
RuntimeError: Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)
Exception ignored in: <function GPIOBase.__del__ at 0xb65181d8>
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 155, in __del__
  File "/usr/lib/python3/dist-packages/gpiozero/input_devices.py", line 283, in close
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 240, in close
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 568, in close
  File "/usr/lib/python3/dist-packages/gpiozero/pins/rpigpio.py", line 115, in close
  File "/usr/lib/python3/dist-packages/gpiozero/pins/__init__.py", line 432, in <lambda>
  File "/usr/lib/python3/dist-packages/gpiozero/pins/pi.py", line 307, in _set_when_changed
  File "/usr/lib/python3/dist-packages/gpiozero/pins/rpigpio.py", line 232, in _disable_event_detect
RuntimeError: Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)
