import random
a = [ ]
b = [ ]
c = [ ]
d = [ ]
e = [ ]
f = [ ]
g = [ ]
h = [ ]
i = [ ]
playerx = 0
playery = 0
win = [f]
x = 0
random_t = 1
random_v = 2
r = 10

print(a,b,c)
print(d,e,f)
print(g,h,i)

while win != [3]:
  playerx = int(input("x whare do you want to go"))
 
  if playerx == 1:
    if a == [ ]:
      a = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 2:
    if b == [ ]:
      b = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 3:
    if c == [ ]:
      c = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 4:
    if d == [ ]:
      d = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 5:
    if e == [ ]:
      e = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 6:
    if f == [ ]:
      f = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 7:
    if g == [ ]:
      g = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 8:
    if h == [ ]:
      h = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
  if playerx == 9:
    if i == [ ]:
      i = [1]
      print(a,b,c)
      print(d,e,f)
      print(g,h,i)
      
      
      
  if a == b == c:
    if a != [ ]:
      print("x wins")
      win = [3]
  if d == e == f:
    if d != [ ]:
      print("x wins")
      win = [3]
  if g == h == i:
    if g != [ ]:
      print("x wins")
      win = [3]
  if a == d == g:
    if a != [ ]:
      print("x wins")
      win = [3]
  if b == e == i:
    if b != [ ]:
      print("x wins")
      win = [3]
  if c == f == i:
    if c != [ ]:
      print("x wins")
      win = [3]
  if a == e == i:
    if a != [ ]:
      print("x wins")
      win = [3]
  if c == e == g:
    if c != [ ]:
      print("x wins")
      win = [3]
    
    
    
      
  if a == b != [ ]:
    if c == [ ]:
      r = 3
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if c == b != [ ]:
    if a == [ ]:
      r = 1
      random_v = 1
    else: 
      random_v = 2
  else:
    random_v = 2
  
  if d == e != [ ]:
    if f == [ ]:
      r = 6
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if f == e != [ ]:
    if d == [ ]:
      r = 4
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2

  if g == h != [ ]:
    if i == [ ]:
      r = 9
      random_v = 1
    else:
      random_v = 2 
  else:
    random_v = 2
  
  if i == h != [ ]:
    if g == [ ]:
      r = 7
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if a == d != [ ]:
    if g == [ ]:
      r = 7
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if g == d != [ ]:
    if a == [ ]:
      r = 1
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2

  if b == e != [ ]:
    if h == []:
      r = 8
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2

  if h == e != [ ]:
    if b == [ ]:
      r = 2
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if c == f != [ ]:
    if i == [ ]:
      r = 9
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2

  if i == f != [ ]:
    if c == [ ]:
      r = 3
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2

  if a == e != [ ]:
    if i == [ ]:
      r = 9
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if i == e != [ ]:
    if a == [ ]:
      r = 1
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2
  
  if c == e != [ ]:
    if g == [ ]:
      r = 7
      random_v = 1
    else:
      random_v = 2
  else:
    random_v = 2  

  if g == e != [ ]:
    if c == [ ]:
      r = 3
      random_v = 1
    else:
      ramdom_v = 2
  else:
    random_v = 2
    
    
  if random_v == 2:
    if r == 10: 
      r = random.randint(1,9)
  
  while random_t == 2:
   
    if r == 1:
      if a != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
  
    if r == 2:
      if b != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 3:
      if c != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 4:
      if d != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 5:
      if e != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 6:
      if f != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 7:
      if g != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else: 
        random_t = 1
 
    if r == 8:
      if h != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1
 
    if r == 9:
      if i != [ ]:
        r = random.randint(1,9)
        random_t = 2
      else:
        random_t = 1

  
  print("cpu is going")
  
  
  if random_t == 1:
    if r == 1:
      if a == [ ]:
        a = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 2:
      if b == [ ]:
        b = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 3:
      if c == [ ]:
        c = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 4:
      if d == [ ]:
        d = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 5:
      if e == [ ]:
        e = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 6:
      if f == [ ]:
        f = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 7:
      if g == [ ]:
        g = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 8:
      if h == [ ]:
        h = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    if r == 9:
      if i == [ ]:
        i = [2]
        print(a,b,c)
        print(d,e,f)
        print(g,h,i)
    
    if a == b == c:
      if a != [ ]:
        print("y wins")
        win = [3]
    if d == e == f:
      if d != [ ]:
        print("y wins")
        win = [3]
    if g == h == i:
      if g != [ ]:
        print("y wins")
        win = [3]
    if a == d == g:
      if a != [ ]:
        print("y wins")
        win = [3]
    if b == e == i:
      if b != [ ]:
        print("y wins")
        win = [3]
    if c == f == i:
      if c != [ ]:
        print("y wins")
        win = [3]
    if a == e == i:
      if a != [ ]:
        print("y wins")
        win = [3]
    if c == e == g:
      if c != [ ]:
        print("y wins")
        win = [3]
    
    print(r)
    r = 10
    x = x + 1
    print("turn", x)
  
 
 
























































