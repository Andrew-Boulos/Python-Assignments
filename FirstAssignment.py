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










e1 = input("employee one enter your name ")
e1s = input("enter your salary ")

e2 = input("employee two enter your name ")
e2s = input("enter your salary ")

e3 = input("employee three enter your name ")
e3s = input("enter your salary ")

e4 = input("employee four enter your name ")
e4s = input("enter your salary ")

e5 = input("employee five enter your name ")
e5s = input("enter your salary ")



ts = int(e1s) + int(e2s) + int(e3s) + int(e4s) + int(e5s)


print("employee 1: " + e1 + ", salary: " + e1s)

print("employee 2: " + e2 + ", salary: " + e2s)

print("employee 3: " + e3 + ", salary: " + e3s)

print("employee 4: " + e4 + ", salary: " + e4s)

print("employee 5: " + e5 + ", salary: " + e5s)



print("Total salary: " + str(ts))
