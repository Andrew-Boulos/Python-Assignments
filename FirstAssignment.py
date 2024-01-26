x = input("Please enter your name person 1 ")
y = input("please enter your lunch menu cost ")
z = input("please enter your drink cost ")

w = input("Please enter your name person 2 ")
e = input("please enter your lunch menu cost " )
q = input("please enter your drink cost ")

o = input("Please enter your name person 3 ")
u = input("please enter your lunch menu cost ")
p = input("please enter your drink cost ")

j = int(y) + int(z)
a = int(e) + int(q)
m = int(u) + int(p)

po = float(j)*1.1

iu = float(a)*1.1

hi = float(m)*1.1

v = float(po + iu + hi)*1.2

print("Person 1: " + x + " has to pay " + str(po))

print("Person 2: " + w + " has to pay " + str(iu))

print("Person 3: " + o + " has to pay " + str(hi))

print("The total cost is " + str(v))


