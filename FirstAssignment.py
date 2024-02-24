#code 1

'''task:

Write a program to collect the following data from the 3 users.
1. Name
2. Amount of Lunch Menu item
3. Amount of Drink

Calculate and output the Name and the Amount of each person's check including a 10% tip.

eg output. Mike $15.24
John $ 23.10
Jane $ 18.40

Then, calculate the total amount for all three together including a 20% tip.'''



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
























#code 2

'''Task:

Write a program to accept the yearly salary of five employees (one at a time). Using the Accumulation concept,
 calculate and display the total salary from all employees combined.'''





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
























#code 3

'''task:

 A movie theater only keeps a percentage of the revenue earned from ticket sales. The
remainder goes to the distributor. Write a program that calculates a theater’s gross and net
box ofﬁce proﬁt for a night. The program should ask for the name of the movie, and how
many adult and child tickets were sold. (The price of an adult ticket is $6.00 and a child’s
ticket is $3.00.) It should display a report similar to the following:

NOTE: Movies' name should be enclosed within the double quotation.


Movie Name: “Wheels of Fury”
Adult Tickets Sold: 382
Child Tickets Sold: 127
Gross Box Ofﬁce Proﬁt: $ 2673.00
Amount Paid to Distributor: – $ 2138.40
Net Box Ofﬁce Proﬁt: $ 534.60
Assume the theater keeps 20 percent of the gross box ofﬁce proﬁt.'''













movie = input("Enter movie name: ")



n_a = int(input("Enter number of adult tickets sold: "))
n_c = int(input("Enter number of children sold. "))


print("THE FRICKING MOVIE NAME IS " + '"' + movie + '"')
print("Adult tickets sold: " + str(n_a) )
print("N u m b e r    o f    c h i l d r e n    s o l d     i s :    " + str(n_c) + "!!!!")

y = int(n_a * 6)
z = int(n_c * 3)

b = float(y + z)

print("Total money: $" + str(b))

paid = float(b * (80/100))

print("Money paid to the very greedy owner: $" + str("%.2f" % paid))

vb = float(b - paid)

print("MONEY FRICKIN KEPT: $" + str("%.2f" % vb))

