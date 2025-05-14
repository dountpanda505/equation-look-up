
import math
import random
import time
count = 0
all_list = [ ]
some_list = [ ]
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
b = 1
ask = input("are you looking for distance (d) or angle (a)")
print(" ")


if (ask == "distance") or (ask == "d"):
  height = input("what is your height in meters")
  print(" ")
  angle = input("what is the angle")
  print(" ")
  volocity = input("what is your volocity in meters per second")
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

if (ask == "angle") or (ask == "a"):
  height = input("what is your height in meters")
  print(" ")
  volocity = input("what is your volocity in meters per second")
  print(" ")
  x = input("what is your distance in meters you are trying to hit")
  print(" ")
  volocity = float(volocity)
  height = float(height)
  angle = float(angle)
  x = float(x)
  x1 = x + .075
  x2 = x - .075
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
      x_p = round(x_p, 3)
      pair = angle, x_p, "m"
      
      if x2  <= x_p < x1:  
        print(pair)
        a = 2
    
        
      
      count = count + 1
      if count == 50:
        all_list.append(pair)
        count = 0
  
  print("____________________________")
  if a == 1:
    print("sorry i can't find")
    ask_2 = input("do you want to see some of the results in .5 incerments, yes or no")
    if ask_2 == "yes":
      count_2 = 0
      for i in range(len(all_list)):
        print(all_list[count_2])
        count_2 = count_2 + 1
      else:
        print("ok")