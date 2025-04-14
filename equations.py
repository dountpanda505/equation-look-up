
physic_equations = ["P=m*v", "fg=m*g", "a=fn/m","x=vi/t+.5*at²", "v=Δx/Δt", "a=(vf-vi)/t", "vf=vi+a*t","Σf=m*a", "J=ΔP/Δt","m1*v1+m2*v2=(m1+m2)vf", "x=vx*t", "t=√((2*h)/g)", "Ep+m*g*h", "Ek=.5*m*v²","Ep=.5*k*x²"]

math_equations = ["y=mx+b", "a²+b²=c²"]

count = 0
a = 0


physic_equations_def = ["the formula for momentum, where 'p' is momentum, 'm' is mass, and 'v' is velocity", "represents the force of gravity (Fg) acting on an object with mass (m), where 'g' is the acceleration due to gravity (approximately 9.8 m/s² on Earth)", "The net force is equated to the product of the mass times the acceleration.", "represents the distance travelled by a body moving with uniform acceleration a with an initial velocity in the amount of time t", "used to find volocity with the chnage in distance devided by the change in time", "used to find acceloration", "relates the final velocity (vf) of an object to its initial velocity (vi), acceleration (a), and time (t). It is a fundamental kinematic equation used to describe the motion of objects with constant acceleration.", "means the force (F) acting on an object is equal to the mass (m) of an object times its acceleration (a). ", "represents the relationship between impulse (J), change in momentum (ΔP), and change in time (Δt). It signifies that the impulse applied to an object is equal to the change in its momentum divided by the time interval over which the force acts. ", "The general equation for conservation of momentum in a collision is m₁v₁ + m₂v₂ = m₁v'₁ + m₂v'₂, where m₁ and m₂ are the masses of the two objects, v₁ and v₂ are their initial velocities, and v'₁ and v'₂ are their final velocities. This equation applies to both elastic and inelastic collisions", "The equation \(x=vx\cdot t\) describes the horizontal displacement (x) of an object in motion, where \(vx\) is the constant horizontal velocity and \(t\) is the time. This equation is fundamental in understanding projectile motion and uniform motion.", "The time taken for an object to fall under gravity can be calculated using the equation of motion: where: t = time taken to fall, h = height from which the object is falling, and g = acceleration due to gravity (approximately 9.8 m/s2 on Earth).",  "the equation used to find Potential Energy useing (m) mass (g) gravity (approximately 9.8 m/s2 on Earth) and (h) hight the object is falling from.", "the equation used to find kentic energy useing half of the objects mass times volocity squared", "the equation used to find spring Potential Energy using half of (k) spring constent times (x²) or distance squared."]

math_equations_def = ["slope-intercept form of a linear equation, where: y: and x represent the coordinates of a point on the line. m: represents the slope of the line (how steep it is). b: represent s the y-intercept of the line (where the line crosses the y-axis).", "The Pythagorean Theorem describes the relationship among the three sides of a right triangle"]




print("are you looking for math, physics, or any")
ask = input()
if (ask != "physics") or (ask != "math") or (ask != "any"):
    c = 1
if (ask == "physics") or (ask == "math") or (ask == "any"):
  c = 0
while c == 1:
  if (ask != "physics") or (ask != "math") or (ask != "any"):
    c = 1
  if (ask == "physics") or (ask == "math") or (ask == "any"):
    c = 0
  if c == 1:
    print("nope try again")
    ask = input()
    
  


if ask == "physics":
  print("what are you loking for")
  ask_2 = input()
  for i in range(len(physic_equations)):
    look = physic_equations[count].count(ask_2)
    if look != 0:
      a = 1
      print(physic_equations[count])
      print(physic_equations_def[count])
      print(" ") 
    count = count + 1
  if a == 0:
    print("hmm can't seem to find anything")
  count = 0
  
  
if ask == "math":
  print("what are you loking for")
  ask_2 = input()
  for i in range(len(math_equations)):
    look = math_equations[count].count(ask_2)
    if look != 0:
      a = 1
      print(math_equations[count])
      print(math_equations_def[count])
      print(" ")
    count = count + 1
  if a == 0:
    print("hmm can't seem to find anything")
  count = 0

if ask == "any":
  all = math_equations + physic_equations
  all_def = math_equations_def + physic_equations_def
  print("what are you loking for")
  ask_2 = input()
  for i in range(len(all)):
    look = all[count].count(ask_2)
    if look != 0:
      a = 1
      print(all[count])
      print(all_def[count])
      print(" ")
    count = count + 1
  if a == 0:
    print("hmm can't seem to find anything")
  count = 0
  