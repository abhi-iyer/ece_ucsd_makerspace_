from subprocess import call
from threading import Timer
mode = 1
def call_alarm():
  global mode
  if mode ==1:
    call(["omxplayer","--vol","-1200","-o","local","justwhat.mp3"])

def sleep_alarm():
  global mode
  mode = 0
  t = Timer(10, set_alarm)
  t.start()

def set_alarm():
  global mode
  mode = 1

def get_mode():
  global mode
  return mode



