
'''



x = input("welcome, Please select a drink: Apple($4), Coffe($6), Lemonade($3), Special blend($8), scam($9999) ")
import time
i = 0

z = """
                   KABOOM!!!
       ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⠿⣿⣿⠿⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⠿⠟⠛⠛⠁⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠉⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
       ⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿
       ⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢿⣿
       ⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
       ⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣾⣿
       ⣿⣿⣄⡀⢀⡀⠀⠀⠀⠀⣠⣤⣤⣴⠿⠿⣦⣄⣀⣀⣴⣄⡀⠀⠀⣠⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣷⣶⠶⠟⠋⠈⠉⠀⠀⠀⠀⠉⠉⠉⠁⠉⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣴⣷⣤⣀⣠⣶⣄⣀⣴⣶⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠉⠀⠀⠈⠙⠛⠛⠛⠛⠿⠿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⡏⠀⣤⣶⣶⣾⣿⣿⣿⡇⠀⠀⠘⣿⣿⣿⣿⣶⣶⣦⡄⠈⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣦⣄⣈⣉⠉⠛⠛⠛⠀⠀⠀⠀⠙⠛⠛⠋⢉⣉⣠⣤⣾⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

if x.lower() == "apple":
    cash = float(input("Enter amount of cash "))
    time.sleep(1)

    if cash >= 4:
        print("Thank you for buying apple!")
        time.sleep(1)
        change = float(cash) - 4
        print("Your change is: $" + str(change))
    else: 
        print("Enter the right amount of money! Stop trying to scam me!!!")
        time.sleep(2)
        print("Thats it. I'M SO MAD. I'M GOING TO MISSILE STRIKE YOUR HOME!!!")
        time.sleep(2)
        print("['Starting up fire sequence....']")
        time.sleep(5)
        while i < 2038:
            print("Estimated time passed: " + str(i))
            i = i + 1
            time.sleep(0.002)
        i = 0
        time.sleep(1)
        print("['Start up success']")
        time.sleep(2)
        print("['Loading files... ( 10984 )']")
        time.sleep(7)
        while i < 10885:
            print("Files loaded { " + str(i) + " }")
            i = i + 1
            time.sleep(0.0002)
        i = 10
        print("['Loading succsess.]'")
        time.sleep(2)
        print("['Launching missile...']")
        time.sleep(2)
        while i > 0 :
            print("T minus " + str(i))
            i = i - 1
            time.sleep(1)

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("['Launch succsess']")
        time.sleep(2)
        print("['Terminating program...']")
        time.sleep(1)
        print(z)












elif x.lower() == "coffe":
    cash = float(input("Enter amount of cash "))
    time.sleep(1)

    if cash >= 6:
        print("Thank you for buying coffe!")
        time.sleep(1)
        change = float(cash) - 6
        print("Your change is: $" + str(change))
    else: 
        print("Enter the right amount of money! Stop trying to scam me!!!")
        time.sleep(2)
        print("Thats it. I'M SO MAD. I'M GOING TO MISSILE STRIKE YOUR HOME!!!")
        time.sleep(2)
        print("['Starting up fire sequence....']")
        time.sleep(5)
        while i < 2038:
            print("Estimated time passed: " + str(i))
            i = i + 1
            time.sleep(0.002)
        i = 0
        time.sleep(1)
        print("['Start up success']")
        time.sleep(2)
        print("['Loading files... ( 10984 )']")
        time.sleep(7)
        while i < 10885:
            print("Files loaded { " + str(i) + " }")
            i = i + 1
            time.sleep(0.0002)
        i = 10
        print("['Loading succsess.]'")
        time.sleep(2)
        print("['Launching missile...']")
        time.sleep(2)
        while i > 0 :
            print("T minus " + str(i))
            i = i - 1
            time.sleep(1)

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("['Launch succsess']")
        time.sleep(2)
        print("['Terminating program...']")
        time.sleep(1)
        print(z)















elif x.lower() == "lemonade":
    cash = float(input("Enter amount of cash "))
    time.sleep(1)

    if cash >= 3:
        print("Thank you for buying lemonade!")
        time.sleep(1)
        change = float(cash) - 3
        print("Your change is: $" + str(change))
    else: 
        print("Enter the right amount of money! Stop trying to scam me!!!")
        time.sleep(2)
        print("Thats it. I'M SO MAD. I'M GOING TO MISSILE STRIKE YOUR HOME!!!")
        time.sleep(2)
        print("['Starting up fire sequence....']")
        time.sleep(5)
        while i < 2038:
            print("Estimated time passed: " + str(i))
            i = i + 1
            time.sleep(0.002)
        i = 0
        time.sleep(1)
        print("['Start up success']")
        time.sleep(2)
        print("['Loading files... ( 10984 )']")
        time.sleep(7)
        while i < 10885:
            print("Files loaded { " + str(i) + " }")
            i = i + 1
            time.sleep(0.0002)
        i = 10
        print("['Loading succsess.]'")
        time.sleep(2)
        print("['Launching missile...']")
        time.sleep(2)
        while i > 0 :
            print("T minus " + str(i))
            i = i - 1
            time.sleep(1)

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("['Launch succsess']")
        time.sleep(2)
        print("['Terminating program...']")
        time.sleep(1)
        print(z)














elif x.lower() == "special blend":
    cash = float(input("Enter amount of cash "))
    time.sleep(1)

    if cash >= 8:
        print("Thank you for buying special blend!")
        time.sleep(1)
        change = float(cash) - 8
        print("Your change is: $" + str(change))
    else: 
        print("Enter the right amount of money! Stop trying to scam me!!!")
        time.sleep(2)
        print("Thats it. I'M SO MAD. I'M GOING TO MISSILE STRIKE YOUR HOME!!!")
        time.sleep(2)
        print("['Starting up fire sequence....']")
        time.sleep(5)
        while i < 2038:
            print("Estimated time passed: " + str(i))
            i = i + 1
            time.sleep(0.002)
        i = 0
        time.sleep(1)
        print("['Start up success']")
        time.sleep(2)
        print("['Loading files... ( 10984 )']")
        time.sleep(7)
        while i < 10885:
            print("Files loaded { " + str(i) + " }")
            i = i + 1
            time.sleep(0.0002)
        i = 10
        print("['Loading succsess.]'")
        time.sleep(2)
        print("['Launching missile...']")
        time.sleep(2)
        while i > 0 :
            print("T minus " + str(i))
            i = i - 1
            time.sleep(1)

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("['Launch succsess']")
        time.sleep(2)
        print("['Terminating program...']")
        time.sleep(1)
        print(z)















elif x.lower() == "scam":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)
        print("ERROR!")
        time.sleep(1)
        print("ERROR!")
        time.sleep(1)
        print("HEY THE AMOUNT YOU ENTRED IS $9998.999!!!")
        time.sleep(2)

    
        
        print("Thats it. I'M SO MAD. I'M GOING TO MISSILE STRIKE YOUR HOME!!!")
        time.sleep(2)
        print("['Starting up fire sequence....']")
        time.sleep(5)
        while i < 2038:
            print("Estimated time passed: " + str(i))
            i = i + 1
            time.sleep(0.002)
        i = 0
        time.sleep(1)
        print("['Start up success']")
        time.sleep(2)
        print("['Loading files... ( 10984 )']")
        time.sleep(7)
        while i < 10885:
            print("Files loaded { " + str(i) + " }")
            i = i + 1
            time.sleep(0.0002)
        i = 10
        print("['Loading succsess.]'")
        time.sleep(2)
        print("['Launching missile...']")
        time.sleep(2)
        while i > 0 :
            print("T minus " + str(i))
            i = i - 1
            time.sleep(1)

        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(4)
        print("['Launch succsess']")
        time.sleep(2)
        print("['Terminating program...']")
        time.sleep(1)
        print(z)






'''






























#PROGRAM 2
        

















x = int(input("welcome, Please select a drink: 1 for apple Apple(small: $4, medium: $8, large $12), 2 for Coffe(small: $6, medium: $12, large: $18), 3 for Lemonade(small: $3, medium: $6, large $9), 4 for Special blend(small: $8, medium: $16, large: $24)"))
import time



def apple():
    y = input("Please select a size: (small: $4, medium: $8, large $12)")
    if y.lower() == "small":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 4:
            print("Thank you for buying a small apple!")
            time.sleep(1)
            change = float(cash) - 4
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 1")





    elif y.lower() == "medium":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 8:
            print("Thank you for buying a medium apple!")
            time.sleep(1)
            change = float(cash) - 8
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 2")



    elif y.lower() == "large":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 12:
            print("Thank you for buying a large apple!")
            time.sleep(1)
            change = float(cash) - 12
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 3")



    else: 
        print("Error: Did you type in the size or spell the name right?")
      









def coffe():
    y = input("Please select a size: (small: $6, medium: $12, large: $18)")

    if y.lower() == "small":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 6:
            print("Thank you for buying a small coffe!")
            time.sleep(1)
            change = float(cash) - 6
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 1")



    elif y.lower() == "medium":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 12:
            print("Thank you for buying a medium coffe!")
            time.sleep(1)
            change = float(cash) - 12
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")    
        print("Price multiplier: 2")


    elif y.lower() == "large":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 18:
            print("Thank you for buying a large coffe!")
            time.sleep(1)
            change = float(cash) - 18
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 3")


    else: 
        print("Error: Did you type in the size or spell the name right?")




















def lemonade():

    y = input("Please select a size: (small: $3, medium: $6, large $9)")
    if y.lower() == "small":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 2:
            print("Thank you for buying a small lemonade!")
            time.sleep(1)
            change = float(cash) - 2
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 1")



    elif y.lower() == "medium":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 6:
            print("Thank you for buying a medium lemonade!")
            time.sleep(1)
            change = float(cash) - 6
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")    
        print("Price multiplier: 2")


    elif y.lower() == "large":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 9:
            print("Thank you for buying a large lemonade!")
            time.sleep(1)
            change = float(cash) - 9
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 3")


    else: 
        print("Error: Did you type in the size or spell the name right?")
     
















def special_blend():

    y = input("Please select a size: (small: $8, medium: $16, large: $24)")
    if y.lower() == "small":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 8:
            print("Thank you for buying a small special blend!")
            time.sleep(1)
            change = float(cash) - 8
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 1")



    elif y.lower() == "medium":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 16:
            print("Thank you for buying a medium special blend!")
            time.sleep(1)
            change = float(cash) - 16
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")    
        print("Price multiplier: 2")


    elif y.lower() == "large":
        cash = float(input("Enter amount of cash "))
        time.sleep(1)

        if cash >= 24:
            print("Thank you for buying a large special blend!")
            time.sleep(1)
            change = float(cash) - 24
            print("Your change is: $" + str(change))
        else: 
            print("Enter the right amount of money! Stop trying to scam me!!!")
        print("Price multiplier: 3")


    else: 
        print("Error: Did you type in the size or spell the name right?")









if x == 1:
    apple()
    
elif x == 2:

    coffe() 
elif x == 3:

    lemonade()
elif x == 4:
    
    special_blend()


else:
    print("Please select a right rumber")



