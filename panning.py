def panning_rotation(panning_step, stack_step, step_cnt):
  from time import sleep
  import RPi.GPIO as GPIO
  import os
  import stack

  DIR =18 
  STEP =14
  CW = 1
  CCW = 0
  SPR = 1600/revnum

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(DIR, GPIO.OUT)
  GPIO.setup(STEP, GPIO.OUT)
  GPIO.output(DIR, CW)
  delay = .005


  for x in range(panning_step):
    for y in range(SPR):
      GPIO.output(STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP, GPIO.LOW)
      sleep(delay)
    sleep(2)
    stack.photo_stack(stack_step, step_cnt)
    #os.system('./run.sh')
    sleep(1)
    DIR =18 
    STEP =14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)

  sleep(.5)
  GPIO.cleanup()
