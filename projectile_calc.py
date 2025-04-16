import math
import random
import time


angle = 0
volocity = 0
gravity = 9.81
x = 0 
height = 0 
time = 0 
vx = 0
vi = 0
vf = 0 
accs = 0
tup = 0
tdown = 0
d1 = 0
d2 = 0
h_max = 0
x_p = 0
a = 1
ask = input("are you looking for distance, height, or angle")

volocity = input("what is your volocity in meters per second")
print(" ")
if ask == "distance":
  height = input("what is your height in meters")
  print(" ")
  angle = input("what is the angle")
  print(" ")

  volocity = float(volocity)
  height = float(height)
  angle = float(angle)

  vo = volocity * math.sin(math.radians(angle))
  tup = vo / gravity
  h_max = height + (vo * tup) - (gravity / 2.0 * (tup ** 2.0))


  tdown = math.sqrt((2.0*h_max)/gravity)
  time = tup + tdown
  x = volocity * math.cos(math.radians(angle)) * time



  x = round(x, 2)
  time = round(time, 2)
  print("________________________")
  print("your distance is")
  print(x, "m")
  print(" ")
  print("your time is")
  print(time, "s")
  print("________________________")

if ask == "angle":
  height = input("what is your height in meters")
  print(" ")
  
  x = input("what is your distance in meters you are trying to hit")
  print(" ")
  volocity = float(volocity)
  height = float(height)
  angle = float(angle)
  x = float(x)
  x1 = x + .05
  x2 = x - .05
  print("looking for an angle that will hit with in")
  print(x1, x2)
  print("____________________________")
  angle = 0
  while angle < 360:
    if angle < 360:
      angle = angle + 0.01
      angle = round(angle, 2)
        
      
      vo = volocity * math.sin(math.radians(angle))
      tup = vo / gravity
      h_max = height + (vo * tup) - (gravity / 2.0 * (tup ** 2.0))


      tdown = math.sqrt((2.0*h_max)/gravity)
      time = tup + tdown
      x_p = volocity * math.cos(math.radians(angle)) * time
      
      
      
      if x2  <= x_p < x1:  
        print("you angle is", angle)
        print("with a distance of", x_p, "m")
        a = 2
  
  
  print("____________________________")
  if a == 1:
    print("can not find")