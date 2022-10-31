# Version 1.1
#AUTHOR: Justin R.
#        Joseph N.
#        Jeshua F.
#
#COURSE:CPRG-216-B
#DATE:   2022-10-31

######################################################################################################
#                                     TIME PERIOD VARIABLE                                           #
######################################################################################################
####### START
while True:
    while True:
        try:
            print("Enter:\n1 - For specific Day"'\n'"2 - For the Week"'\n'"3 - Dor Week Business Days"'\n'"4 - For Weekend days"'\n'"0 - Exit")
            Time_Period = int(input(""))
            if Time_Period not in (0,1,2,3,4): #Time period not in range it returns the option to input again
                print("INVALID INPUT")
                continue    
        except ValueError:
            print("INVALID INPUT") #Return any error apart from the integers
            continue
        else:
            break
    ######################################################################################################
    #                                    Exit option 0                                           #
    ######################################################################################################
    if (Time_Period == 0): #Selection should break incase the users decide to exit
        while True:
            print("EXIT")
            break
    ######################################################################################################
    #                                 Specific day option 1                                            #
    ######################################################################################################
    if (Time_Period == 1): #Time period for specific date
        while True:
            try:
                print("")
                Spec_Day = str.lower(input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]: "))
                if Spec_Day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
                    print("Invalid Input") #DATE input for lowercase and uppercase
                    continue
                ProdNum1 = int(input("ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: ")) #Input product number
                if ProdNum1 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum1 == 0): 
                    break  #Should break the loop incase the users doesn't calculate
                if ProdNum1 in (1,2,3,4,5):
                    QuanNum1 = int(input("Enter quantity sold: ")) #Quantity used 
            
                ProdNum2 = int(input("ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: ")) #Input product number
                if ProdNum2 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum2 == 0):
                    break
                if ProdNum2 in (1,2,3,4,5):
                    QuanNum2 = int(input("ENTER THE QUANTITY SOLD: ")) 
            
                ProdNum3 = int(input("ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum3 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum3 == 0):
                    break
                if ProdNum3 in (1,2,3,4,5):
                    QuanNum3 = int(input("ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
            else:
                break
    ######################################################################################################
    #                               Specific days of the week                                          #       
    ######################################################################################################
    if (Time_Period == 2): #Sales for Monday
        while True:
            try:
                print("ENTER THE SALES DATA FOR EACH DAY OF THE WEEK")
                ProdNum1 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: ")) #Input figures for Monday
                if ProdNum1 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum1 == 0):
                    break
                elif (ProdNum1 == "1", "2", "3", "4", "5"):
                    QuanNum1 = int(input("ENTER THE QUANTITY SOLD: "))
                ProdNum2 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum2 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum2 == 0):
                    break
                elif (ProdNum2 == "1", "2", "3", "4", "5"):
                    QuanNum2 = int(input("ENTER THE QUANTITY SOLD: "))
                ProdNum3 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum3 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum3 == 0):
                    break
                elif (ProdNum3 == "1", "2", "3", "4", "5"):
                    QuanNum3 = int(input("ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2):  #Sales for Tuesday     
        while True:
            try:            
                ProdNum4 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: ")) 
                if ProdNum4 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum4 == 0):
                    break
                elif ProdNum4 in (1,2,3,4,5):
                    QuanNum4 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
                ProdNum5 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum5 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum5 == 0):
                    break
                elif ProdNum5 in (1,2,3,4,5):
                    QuanNum5 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
                ProdNum6 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum6 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum6 == 0):
                    break
                elif ProdNum6 in (1,2,3,4,5):
                    QuanNum6 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2): #Sales for Wednesday
        while True:
            try:
                ProdNum7 = int(input("[WEDNESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum7 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum7 == 0):
                    break
                elif ProdNum7 in (1,2,3,4,5):
                    QuanNum7 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
                ProdNum8 = int(input("[WEDNESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum8 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum8 == 0):
                    break
                elif ProdNum8 in (1,2,3,4,5):
                    QuanNum8 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
                ProdNum9 = int(input("[WEDNESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum9 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum9 == 0):
                    break
                elif ProdNum9 in (1,2,3,4,5):
                    QuanNum9 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2): #Sales for Thursday
        while True:
            try:
                ProdNum10 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum10 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum10 == 0):
                    break
                if ProdNum10 in (1,2,3,4,5):
                    QuanNum10 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum11 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum11 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum11 == 0):
                    break
                if ProdNum11 in (1,2,3,4,5):
                    QuanNum11 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum12 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum12 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum12 == 0):
                    break
                if ProdNum12 in (1,2,3,4,5):
                    QuanNum12 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2): #Sales for Friday
        while True:
            try:
                ProdNum13 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum13 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum13 == 0):
                    break
                if ProdNum13 in (1,2,3,4,5):
                    QuanNum13 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum14 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum14 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum14 == 0):
                    break
                if ProdNum14 in (1,2,3,4,5):
                    QuanNum14 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum15 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum15 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum15 == 0):
                    break
                if ProdNum15 in (1,2,3,4,5):
                    QuanNum15 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2): #Sales for Saturday
        while True:
            try:
                ProdNum16 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum16 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum16 == 0):
                    break
                if ProdNum16 in (1,2,3,4,5):
                    QuanNum16 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum17 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum17 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum17 == 0):
                    break
                if ProdNum17 in (1,2,3,4,5):
                    QuanNum17 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum18 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum18 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum18 == 0):
                    break
                if ProdNum18 in (1,2,3,4,5):
                    QuanNum18 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 2): #Sales for Sunday
        while True:
            try:
                ProdNum19 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum19 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum19 == 0):
                    break
                if ProdNum19 in (1,2,3,4,5):
                    QuanNum19 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum20 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum20 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum20 == 0):
                    break
                if ProdNum20 in (1,2,3,4,5):
                    QuanNum20 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum21 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum21 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum21 == 0):
                    break
                if ProdNum21 in (1,2,3,4,5):
                    QuanNum21 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))

            except ValueError:
                print("INVALID INPUT")
                continue

    ######################################################################################################
    #                                    Weekday sales (Option 3)                                    #
    ######################################################################################################
    if (Time_Period == 3): #Sales for Monday
        while True:
            try:
                print("ENTER THE SALES DATA FOR WEEKDAYS")
                ProdNum1 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum1 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum1 == 0):
                    break
                elif (ProdNum1 == "1", "2", "3", "4", "5"):
                    QuanNum1 = int(input("ENTER THE QUANTITY SOLD: "))
                ProdNum2 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum2 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum2 == 0):
                    break
                elif (ProdNum2 == "1", "2", "3", "4", "5"):
                    QuanNum2 = int(input("ENTER THE QUANTITY SOLD: "))
                ProdNum3 = int(input("[MONDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum3 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum3 == 0):
                    break
                elif (ProdNum3 == "1", "2", "3", "4", "5"):
                    QuanNum3 = int(input("ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 3): #Sales for Tuesday
        while True:
            try:            
                ProdNum4 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum4 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum4 == 0):
                    break
                elif ProdNum4 in (1,2,3,4,5):
                    QuanNum4 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
                ProdNum5 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum5 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum5 == 0):
                    break
                elif ProdNum5 in (1,2,3,4,5):
                    QuanNum5 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
                ProdNum6 = int(input("[TUESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum6 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum6 == 0):
                    break
                elif ProdNum6 in (1,2,3,4,5):
                    QuanNum6 = int(input("[TUESDAY] ENTER QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 3): #Sales for Wednesday
        while True:
            try:
                ProdNum7 = int(input("[WEDBESDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum7 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum7 == 0):
                    break
                elif ProdNum7 in (1,2,3,4,5):
                    QuanNum7 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
                ProdNum8 = int(input("[WEDNESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum8 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum8 == 0):
                    break
                elif ProdNum8 in (1,2,3,4,5):
                    QuanNum8 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
                ProdNum9 = int(input("[WEDNESDAY] ENTER PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum9 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum9 == 0):
                    break
                elif ProdNum9 in (1,2,3,4,5):
                    QuanNum9 = int(input("[WEDNESDAY] ENTER QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
            
    if (Time_Period == 3): #Sales for Thursday
        while True:
            try:
                ProdNum10 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum10 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum10 == 0):
                    break
                if ProdNum10 in (1,2,3,4,5):
                    QuanNum10 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum11 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum11 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum11 == 0):
                    break
                if ProdNum11 in (1,2,3,4,5):
                    QuanNum11 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum12 = int(input("[THURSDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum12 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum12 == 0):
                    break
                if ProdNum12 in (1,2,3,4,5):
                    QuanNum12 = int(input("[THURSDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 3): #Sales for Friday
        while True:
            try:
                ProdNum13 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum13 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum13 == 0):
                    break
                if ProdNum13 in (1,2,3,4,5):
                    QuanNum13 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum14 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum14 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum14 == 0):
                    break
                if ProdNum14 in (1,2,3,4,5):
                    QuanNum14 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum15 = int(input("[FRIDAY] ENTER THE PRODUCT NUMBER FROM 1-5 OR 0 TO STOP: "))
                if ProdNum15 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum15 == 0):
                    break
                if ProdNum15 in (1,2,3,4,5):
                    QuanNum15 = int(input("[FRIDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    ######################################################################################################
    #                                   Weekend sales(Option 4)                                             #
    ######################################################################################################
    if (Time_Period == 4): #Sales for Saturday
        while True:
            try:
                ProdNum1 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum1 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum1 == 0):
                    break
                if ProdNum1 in (1,2,3,4,5):
                    QuanNum1 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum2 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum2 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum2== 0):
                    break
                if ProdNum2 in (1,2,3,4,5):
                    QuanNum2 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum3 = int(input("[SATURDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum3 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum3 == 0):
                    break
                if ProdNum3 in (1,2,3,4,5):
                    QuanNum3 = int(input("[SATURDAY] ENTER THE QUANTITY SOLD: "))
            except ValueError:
                print("INVALID INPUT")
                continue
    if (Time_Period == 4): #Sales for Sunday
        while True:
            try:
                ProdNum4 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum4 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum4 == 0):
                    break
                if ProdNum4 in (1,2,3,4,5):
                    QuanNum4 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum5 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum5 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum5 == 0):
                    break
                if ProdNum5 in (1,2,3,4,5):
                    QuanNum5 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))
                ProdNum6 = int(input("[SUNDAY] ENTER THE PRODUCT NUMEBR FROM 1-5 OR 0 TO STOP: "))
                if ProdNum6 not in (0,1,2,3,4,5):
                    print("INVALID INPUT")
                    continue
                if (ProdNum6 == 0):
                    break
                if ProdNum6 in (1,2,3,4,5):
                    QuanNum6 = int(input("[SUNDAY] ENTER THE QUANTITY SOLD: "))

            except ValueError:
                print("INVALID INPUT")
                continue
    ######################################################################################################
    #                                    Calculation conditions#
    ######################################################################################################
    if Time_Period == 1:
        if (ProdNum1 == 1):
            Profit1 = 120.45 * QuanNum1
        elif (ProdNum1 == 2):
            Profit1 = 99.50 * QuanNum1
        elif (ProdNum1 == 3):
            Profit1 = 75.69 * QuanNum1
        elif (ProdNum1 == 4):
            Profit1 = 65.73 * QuanNum1
        elif (ProdNum1 == 5):
            Profit1 = 51.49 * QuanNum1
        else:
            (ProdNum1 == 0)
            Profit1 = 0
            ProdNum2 = 0
            ProdNum3 = 0
    if Time_Period == 1:
        if (ProdNum2 == 1):
            Profit2 = 120.45 * QuanNum2
        elif (ProdNum2 == 2):
            Profit2 = 99.50 * QuanNum2
        elif (ProdNum2 == 3):
            Profit2 = 75.69 * QuanNum2
        elif (ProdNum2 == 4):
            Profit2 = 65.73 * QuanNum2
        elif (ProdNum2 == 5):
            Profit2 = 51.49 * QuanNum2
        else:
            (ProdNum2 == 0)
            Profit2 = 0
            ProdNum3 = 0
    if Time_Period == 1:
        if (ProdNum3 == 1):
            Profit3 = 120.45 * QuanNum3
        elif (ProdNum3 == 2):
            Profit3 = 99.50 * QuanNum3
        elif (ProdNum3 == 3):
            Profit3 = 75.69 * QuanNum3
        elif (ProdNum3 == 4):
            Profit3 = 65.73 * QuanNum3
        elif (ProdNum3 == 5):
            Profit3 = 51.49 * QuanNum3
        else:
            (ProdNum3 == 0)
            Profit3 = 0

        totalprofit = Profit1 + Profit2 + Profit3
    if Time_Period == 1:
        while True:
            if totalprofit >=10000: ##Will return a positive message if the sales were greater than $10000
                print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID GREAT THIS PERIOD!")
                print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
                break
            else: #Will return an encouragement message if sales were less than $10000
                print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID NOT REACH YOUR GOAL KEEP TRYING!")
                print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
                break

    #################################################################################################
    if (Time_Period == 2):
        if (ProdNum1 == 1):
            Profit1 = 120.44 * QuanNum1
        elif (ProdNum1 == 2):
            Profit1 = 99.50 * QuanNum1
        elif (ProdNum1 == 3):
            Profit1 = 75.69 * QuanNum1
        elif (ProdNum1 == 4):
            Profit1 = 65.73 * QuanNum1
        elif (ProdNum1 == 5):
            Profit1 = 51.49 * QuanNum1
        else:
            if ProdNum1 == 0:
                Profit1 = 0
                ProdNum2 = 0
                ProdNum3 =0
    if Time_Period ==2:
        if (ProdNum2 == 1):
            Profit2 = 120.44 * QuanNum2
        elif (ProdNum2 == 2):
            Profit2 = 99.50 * QuanNum2
        elif (ProdNum2 == 3):
            Profit2 = 75.69 * QuanNum2
        elif (ProdNum2 == 4):
            Profit2 = 65.73 * QuanNum2
        elif (ProdNum2 == 5):
            Profit2 = 51.49 * QuanNum2
        else:
            if (ProdNum2 == 0):
                Profit2 = 0
                ProdNum3 = 0

    if Time_Period ==2:
        if (ProdNum3 == 1):
            Profit3 = 120.44 * QuanNum3
        elif (ProdNum3 == 2):
            Profit3 = 99.50 * QuanNum3
        elif (ProdNum3 == 3):
            Profit3 = 75.69 * QuanNum3
        elif (ProdNum3 == 4):
            Profit3 = 65.73 * QuanNum3
        elif (ProdNum3 == 5):
            Profit3 = 51.49 * QuanNum3
        else:
            if (ProdNum3 == 0):
                Profit3 =0
    if Time_Period ==2:
        if (ProdNum4 == 1):
            Profit4 = 120.44 * QuanNum4
        elif (ProdNum4 == 2):
            Profit4 = 99.50 * QuanNum4
        elif (ProdNum4 == 3):
            Profit4 = 75.69 * QuanNum4
        elif (ProdNum4 == 4):
            Profit4 = 65.73 * QuanNum4
        elif (ProdNum4 == 5):
            Profit4 = 51.49 * QuanNum4
        else:
            if (ProdNum4 == 0):
                Profit4 = 0
                ProdNum5 = 0
                ProdNum6 = 0
    if Time_Period ==2:
        if (ProdNum5 == 1):
            Profit5 = 120.44 * QuanNum5
        elif (ProdNum5 == 2):
            Profit5 = 99.50 * QuanNum5
        elif (ProdNum5 == 3):
            Profit5 = 75.69 * QuanNum5
        elif (ProdNum5 == 4):
            Profit5 = 65.73 * QuanNum5
        elif (ProdNum5 == 5):
            Profit5 = 51.49 * QuanNum5
        else:
            if (ProdNum5 == 0):
                Profit5 = 0
                ProdNum6 = 0
    
    if Time_Period ==2:
        if (ProdNum6 == 1):
            Profit6 = 120.44 * QuanNum6
        elif (ProdNum6 == 2):
            Profit6 = 99.50 * QuanNum6
        elif (ProdNum6 == 3):
            Profit6 = 75.69 * QuanNum6
        elif (ProdNum6 == 4):
            Profit6 = 65.73 * QuanNum6
        elif (ProdNum6 == 5):
            Profit6 = 51.49 * QuanNum6
        else:
            if (ProdNum6 == 0):
                Profit6 = 0
    if Time_Period ==2:
        if (ProdNum7 == 1):
            Profit7 = 120.44 * QuanNum7
        elif (ProdNum7 == 2):
            Profit7 = 99.50 * QuanNum7
        elif (ProdNum7 == 3):
            Profit7 = 75.69 * QuanNum7 
        elif (ProdNum7 == 4):
            Profit7 = 65.73 * QuanNum7
        elif (ProdNum7 == 5):
            Profit7 = 51.49 * QuanNum7
        else:
            if (ProdNum7 == 0):
                Profit7 = 0
                ProdNum8 = 0
                ProdNum9 = 0
    if Time_Period ==2:
        if (ProdNum8 == 1):
            Profit8 = 120.44 * QuanNum8
        elif (ProdNum8 == 2):
            Profit8 = 99.50 * QuanNum8
        elif (ProdNum8 == 3):
            Profit8 = 75.69 * QuanNum8
        elif (ProdNum8 == 4):
            Profit8 = 65.73 * QuanNum8
        elif (ProdNum8 == 5):
            Profit8 = 51.49 * QuanNum8
        else:
            if (ProdNum8 == 0):
                Profit8 = 0
                ProdNum9 = 0

        if (ProdNum9 == 1):
            Profit9 = 120.44 * QuanNum9
        elif (ProdNum9 == 2):
            Profit9 = 99.50 * QuanNum19
        elif (ProdNum9 == 3):
            Profit9 = 75.69 * QuanNum9
        elif (ProdNum9 == 4):
            Profit9 = 65.73 * QuanNum9
        elif (ProdNum9 == 5):
            Profit9 = 51.49 * QuanNum9
        else:
            if (ProdNum9 == 0):
                Profit9 = 0
    if Time_Period ==2:
        if (ProdNum10 == 1):
            Profit10 = 120.44 * QuanNum10
        elif (ProdNum10 == 2):
            Profit10 = 99.50 * QuanNum10
        elif (ProdNum10 == 3):
            Profit10 = 75.69 * QuanNum10
        elif (ProdNum10 == 4):
            Profit10 = 65.73 * QuanNum10
        elif (ProdNum10 == 5):
            Profit10 = 51.49 * QuanNum10
        else:
            if (ProdNum10 ==0):
                Profit10 = 0
                ProdNum11 = 0
                ProdNum12 = 0
    if Time_Period ==2:
        if (ProdNum11 == 1):
            Profit11 = 120.44 * QuanNum11
        elif (ProdNum11 == 2):
            Profit11 = 99.50 * QuanNum11
        elif (ProdNum11 == 3):
            Profit11 = 75.69 * QuanNum11
        elif (ProdNum11 == 4):
            Profit11 = 65.73 * QuanNum11
        elif (ProdNum11 == 5):
            Profit11 = 51.49 * QuanNum11
        else:
            if (ProdNum11 == 0):
                Profit11 = 0
                ProdNum12 = 0
    if Time_Period ==2:
        if (ProdNum12 == 1):
            Profit12 = 120.44 * QuanNum12
        elif (ProdNum12 == 2):
            Profit12 = 99.50 * QuanNum12
        elif (ProdNum12 == 3):
            Profit12 = 75.69 * QuanNum12
        elif (ProdNum12 == 4):
            Profit12 = 65.73 * QuanNum12
        elif (ProdNum12 == 5):
            Profit12 = 51.49 * QuanNum12
        else:
            if (ProdNum12 == 0):
                Profit12 = 0
    if Time_Period ==2:
        if (ProdNum13 == 1):
            Profit13 = 120.44 * QuanNum13
        elif (ProdNum13 == 2):
            Profit13 = 99.50 * QuanNum13
        elif (ProdNum13 == 3):
            Profit13 = 75.69 * QuanNum13
        elif (ProdNum13 == 4):
            Profit13 = 65.73 * QuanNum13
        elif (ProdNum13 == 5):
            Profit13 = 51.49 * QuanNum13
        else:
            if (ProdNum13 == 0):
                Profit12 = 0
                ProdNum13 = 0
                ProdNum14 = 0
    if Time_Period ==2:
        if (ProdNum14 == 1):
            Profit14 = 120.44 * QuanNum14
        elif (ProdNum14 == 2):
            Profit14 = 99.50 * QuanNum14
        elif (ProdNum14 == 3):
            Profit14 = 75.69 * QuanNum14
        elif (ProdNum14 == 4):
            Profit14 = 65.73 * QuanNum14
        elif (ProdNum14 == 5):
            Profit14 = 51.49 * QuanNum14
        else:
            if (ProdNum14 == 0):
                Profit14 = 0
                ProdNum15 = 0
    if Time_Period ==2:
        if (ProdNum15 == 1):
            Profit15 = 120.44 * QuanNum15
        elif (ProdNum15 == 2):
            Profit15 = 99.50 * QuanNum15
        elif (ProdNum15 == 3):
            Profit15 = 75.69 * QuanNum15
        elif (ProdNum15 == 4):
            Profit15 = 65.73 * QuanNum15
        elif (ProdNum15 == 5):
            Profit15 = 51.49 * QuanNum15
        else:
            if (ProdNum15 == 0):
                Profit15 = 0
    if Time_Period ==2:
        if (ProdNum16 == 1):
            Profit16 = 120.44 * QuanNum16
        elif (ProdNum16 == 2):
            Profit16 = 99.50 * QuanNum16
        elif (ProdNum16 == 3):
            Profit16 = 75.69 * QuanNum16
        elif (ProdNum16 == 4):
            Profit16 = 65.73 * QuanNum16
        elif (ProdNum16 == 5):
            Profit16 = 51.49 * QuanNum16
        else:
            if (ProdNum16 == 0):
                Profit16 = 0
                ProdNum17 = 0
                ProdNum18 = 0
    if Time_Period ==2:
        if (ProdNum17 == 1):
            Profit17 = 120.44 * QuanNum17
        elif (ProdNum17 == 2):
            Profit17 = 99.50 * QuanNum17
        elif (ProdNum17 == 3):
            Profit17 = 75.69 * QuanNum17 
        elif (ProdNum17 == 4):
            Profit17 = 65.73 * QuanNum17
        elif (ProdNum17 == 5):
            Profit17 = 51.49 * QuanNum17
        else:
            if (ProdNum17 == 0):
                Profit17 = 0
                ProdNum18 = 0
    if Time_Period ==2:
        if (ProdNum18 == 1):
            Profit18 = 120.44 * QuanNum18
        elif (ProdNum18 == 2):
            Profit18 = 99.50 * QuanNum18
        elif (ProdNum18 == 3):
            Profit18 = 75.69 * QuanNum18
        elif (ProdNum18 == 4):
            Profit18 = 65.73 * QuanNum18
        elif (ProdNum18 == 5):
            Profit18 = 51.49 * QuanNum18
        else:
            if (ProdNum18 == 0):
                Profit18 = 0
    if Time_Period ==2:
        if (ProdNum19 == 1):
            Profit19 = 120.44 * QuanNum19
        elif (ProdNum19 == 2):
            Profit19 = 99.50 * QuanNum19
        elif (ProdNum19 == 3):
            Profit19 = 75.69 * QuanNum19
        elif (ProdNum19 == 4):
            Profit19 = 65.73 * QuanNum19
        elif (ProdNum19 == 5):
            Profit19 = 51.49 * QuanNum19
        else:
            if (ProdNum19 == 0):
                Profit19 = 0
                ProdNum20 = 0
                ProdNum21 = 0
    if Time_Period ==2:
        if (ProdNum20 == 1):
            Profit20 = 120.44 * QuanNum20
        elif (ProdNum20 == 2):
            Profit20 = 99.50 * QuanNum20
        elif (ProdNum20 == 3):
            Profit20 = 75.69 * QuanNum20
        elif (ProdNum20 == 4):
            Profit20 = 65.73 * QuanNum20
        elif (ProdNum20 == 5):
            Profit20 = 51.49 * QuanNum20
        else:
            if (ProdNum20 == 0):
                Profit20 = 0
                ProdNum21 = 0
    if Time_Period ==2:
        if (ProdNum21 == 1):
            Profit21 = 120.44 * QuanNum21
        elif (ProdNum21 == 2):
            Profit21 = 99.50 * QuanNum21
        elif (ProdNum21 == 3):
            Profit21 = 75.69 * QuanNum21
        elif (ProdNum21 == 4):
            Profit21 = 65.73 * QuanNum21
        elif (ProdNum21 == 5):
            Profit21 = 51.49 * QuanNum21
        else:
            if (ProdNum21 == 0):
                Profit21 = 0

        totalprofit = Profit1 + Profit2 + Profit3 + Profit4 + Profit5 + Profit6 + Profit7 + Profit8 +Profit9 + Profit10 + Profit11 + Profit12 + Profit12 + Profit14 + Profit15 + Profit16 + Profit17 + Profit18 + Profit19 + Profit20 + Profit21

    if Time_Period ==2:
        if totalprofit >=10000:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID GREAT THIS PERIOD!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
        else:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID NOT REACH YOUR GOAL KEEP TRYING!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    ##############################################################################################         
    if (Time_Period == 3):
        if (ProdNum1 == 1):
            Profit1 = 120.44 * QuanNum1
        elif (ProdNum1 == 2):
            Profit1 = 99.50 * QuanNum1
        elif (ProdNum1 == 3):
            Profit1 = 75.69 * QuanNum1
        elif (ProdNum1 == 4):
            Profit1 = 65.73 * QuanNum1
        elif (ProdNum1 == 5):
            Profit1 = 51.49 * QuanNum1
        else:
            if ProdNum1 == 0:
                Profit1 = 0
                ProdNum2 = 0
                ProdNum3 =0
    if Time_Period ==3:
        if (ProdNum2 == 1):
            Profit2 = 120.44 * QuanNum2
        elif (ProdNum2 == 2):
            Profit2 = 99.50 * QuanNum2
        elif (ProdNum2 == 3):
            Profit2 = 75.69 * QuanNum2
        elif (ProdNum2 == 4):
            Profit2 = 65.73 * QuanNum2
        elif (ProdNum2 == 5):
            Profit2 = 51.49 * QuanNum2
        else:
            if (ProdNum2 == 0):
                Profit2 = 0
                ProdNum3 = 0

    if Time_Period ==3:
        if (ProdNum3 == 1):
            Profit3 = 120.44 * QuanNum3
        elif (ProdNum3 == 2):
            Profit3 = 99.50 * QuanNum3
        elif (ProdNum3 == 3):
            Profit3 = 75.69 * QuanNum3
        elif (ProdNum3 == 4):
            Profit3 = 65.73 * QuanNum3
        elif (ProdNum3 == 5):
            Profit3 = 51.49 * QuanNum3
        else:
            if (ProdNum3 == 0):
                Profit3 =0
    if Time_Period ==3:
        if (ProdNum4 == 1):
            Profit4 = 120.44 * QuanNum4
        elif (ProdNum4 == 2):
            Profit4 = 99.50 * QuanNum4
        elif (ProdNum4 == 3):
            Profit4 = 75.69 * QuanNum4
        elif (ProdNum4 == 4):
            Profit4 = 65.73 * QuanNum4
        elif (ProdNum4 == 5):
            Profit4 = 51.49 * QuanNum4
        else:
            if (ProdNum4 == 0):
                Profit4 = 0
                ProdNum5 = 0
                ProdNum6 = 0
    if Time_Period ==3:
        if (ProdNum5 == 1):
            Profit5 = 120.44 * QuanNum5
        elif (ProdNum5 == 2):
            Profit5 = 99.50 * QuanNum5
        elif (ProdNum5 == 3):
            Profit5 = 75.69 * QuanNum5
        elif (ProdNum5 == 4):
            Profit5 = 65.73 * QuanNum5
        elif (ProdNum5 == 5):
            Profit5 = 51.49 * QuanNum5
        else:
            if (ProdNum5 == 0):
                Profit5 = 0
                ProdNum6 = 0
    
    if Time_Period ==3:
        if (ProdNum6 == 1):
            Profit6 = 120.44 * QuanNum6
        elif (ProdNum6 == 2):
            Profit6 = 99.50 * QuanNum6
        elif (ProdNum6 == 3):
            Profit6 = 75.69 * QuanNum6
        elif (ProdNum6 == 4):
            Profit6 = 65.73 * QuanNum6
        elif (ProdNum6 == 5):
            Profit6 = 51.49 * QuanNum6
        else:
            if (ProdNum6 == 0):
                Profit6 = 0
    if Time_Period ==3:
        if (ProdNum7 == 1):
            Profit7 = 120.44 * QuanNum7
        elif (ProdNum7 == 2):
            Profit7 = 99.50 * QuanNum7
        elif (ProdNum7 == 3):
            Profit7 = 75.69 * QuanNum7 
        elif (ProdNum7 == 4):
            Profit7 = 65.73 * QuanNum7
        elif (ProdNum7 == 5):
            Profit7 = 51.49 * QuanNum7
        else:
            if (ProdNum7 == 0):
                Profit7 = 0
                ProdNum8 = 0
                ProdNum9 = 0
    if Time_Period ==3:
        if (ProdNum8 == 1):
            Profit8 = 120.44 * QuanNum8
        elif (ProdNum8 == 2):
            Profit8 = 99.50 * QuanNum8
        elif (ProdNum8 == 3):
            Profit8 = 75.69 * QuanNum8
        elif (ProdNum8 == 4):
            Profit8 = 65.73 * QuanNum8
        elif (ProdNum8 == 5):
            Profit8 = 51.49 * QuanNum8
        else:
            if (ProdNum8 == 0):
                Profit8 = 0
                ProdNum9 = 0
    if Time_Period ==3:
        if (ProdNum9 == 1):
            Profit9 = 120.44 * QuanNum9
        elif (ProdNum9 == 2):
            Profit9 = 99.50 * QuanNum19
        elif (ProdNum9 == 3):
            Profit9 = 75.69 * QuanNum9
        elif (ProdNum9 == 4):
            Profit9 = 65.73 * QuanNum9
        elif (ProdNum9 == 5):
            Profit9 = 51.49 * QuanNum9
        else:
            if (ProdNum9 == 0):
                Profit9 = 0
    if Time_Period ==3:
        if (ProdNum10 == 1):
            Profit10 = 120.44 * QuanNum10
        elif (ProdNum10 == 2):
            Profit10 = 99.50 * QuanNum10
        elif (ProdNum10 == 3):
            Profit10 = 75.69 * QuanNum10
        elif (ProdNum10 == 4):
            Profit10 = 65.73 * QuanNum10
        elif (ProdNum10 == 5):
            Profit10 = 51.49 * QuanNum10
        else:
            if (ProdNum10 ==0):
                Profit10 = 0
                ProdNum11 = 0
                ProdNum12 = 0
    if Time_Period ==3:
        if (ProdNum11 == 1):
            Profit11 = 120.44 * QuanNum11
        elif (ProdNum11 == 2):
            Profit11 = 99.50 * QuanNum11
        elif (ProdNum11 == 3):
            Profit11 = 75.69 * QuanNum11
        elif (ProdNum11 == 4):
            Profit11 = 65.73 * QuanNum11
        elif (ProdNum11 == 5):
            Profit11 = 51.49 * QuanNum11
        else:
            if (ProdNum11 == 0):
                Profit11 = 0
                ProdNum12 = 0
    if Time_Period ==3:
        if (ProdNum12 == 1):
            Profit12 = 120.44 * QuanNum12
        elif (ProdNum12 == 2):
            Profit12 = 99.50 * QuanNum12
        elif (ProdNum12 == 3):
            Profit12 = 75.69 * QuanNum12
        elif (ProdNum12 == 4):
            Profit12 = 65.73 * QuanNum12
        elif (ProdNum12 == 5):
            Profit12 = 51.49 * QuanNum12
        else:
            if (ProdNum12 == 0):
                Profit12 = 0
    if Time_Period ==3:
        if (ProdNum13 == 1):
            Profit13 = 120.44 * QuanNum13
        elif (ProdNum13 == 2):
            Profit13 = 99.50 * QuanNum13
        elif (ProdNum13 == 3):
            Profit13 = 75.69 * QuanNum13
        elif (ProdNum13 == 4):
            Profit13 = 65.73 * QuanNum13
        elif (ProdNum13 == 5):
            Profit13 = 51.49 * QuanNum13
        else:
            if (ProdNum13 == 0):
                Profit12 = 0
                ProdNum13 = 0
                ProdNum14 = 0
    if Time_Period ==3:
        if (ProdNum14 == 1):
            Profit14 = 120.44 * QuanNum14
        elif (ProdNum14 == 2):
            Profit14 = 99.50 * QuanNum14
        elif (ProdNum14 == 3):
            Profit14 = 75.69 * QuanNum14
        elif (ProdNum14 == 4):
            Profit14 = 65.73 * QuanNum14
        elif (ProdNum14 == 5):
            Profit14 = 51.49 * QuanNum14
        else:
            if (ProdNum14 == 0):
                Profit14 = 0
                ProdNum15 = 0
    if Time_Period ==3:
        if (ProdNum15 == 1):
            Profit15 = 120.44 * QuanNum15
        elif (ProdNum15 == 2):
            Profit15 = 99.50 * QuanNum15
        elif (ProdNum15 == 3):
            Profit15 = 75.69 * QuanNum15
        elif (ProdNum15 == 4):
            Profit15 = 65.73 * QuanNum15
        elif (ProdNum15 == 5):
            Profit15 = 51.49 * QuanNum15
        else:
            if (ProdNum15 == 0):
                Profit15 = 0

        totalprofit = Profit1 + Profit2 + Profit3 + Profit4 + Profit5 + Profit6 + Profit7 + Profit8 +Profit9 + Profit10 + Profit11 + Profit12 + Profit12 + Profit14 + Profit15

    if Time_Period ==3:
        if totalprofit >=10000:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID GREAT THIS PERIOD!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
        else:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID NOT REACH YOUR GOAL KEEP TRYING!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
    #################################################################################################
    if (Time_Period == 4):
        if (ProdNum1 == 1):
            Profit1 = 120.44 * QuanNum1
        elif (ProdNum1 == 2):
            Profit1 = 99.50 * QuanNum1
        elif (ProdNum1 == 3):
            Profit1 = 75.69 * QuanNum1
        elif (ProdNum1 == 4):
            Profit1 = 65.73 * QuanNum1
        elif (ProdNum1 == 5):
            Profit1 = 51.49 * QuanNum1
        else:
            if ProdNum1 == 0:
                Profit1 = 0
                ProdNum2 = 0
                ProdNum3 =0
    if Time_Period ==4:
        if (ProdNum2 == 1):
            Profit2 = 120.44 * QuanNum2
        elif (ProdNum2 == 2):
            Profit2 = 99.50 * QuanNum2
        elif (ProdNum2 == 3):
            Profit2 = 75.69 * QuanNum2
        elif (ProdNum2 == 4):
            Profit2 = 65.73 * QuanNum2
        elif (ProdNum2 == 5):
            Profit2 = 51.49 * QuanNum2
        else:
            if (ProdNum2 == 0):
                Profit2 = 0
                ProdNum3 = 0

    if Time_Period ==4:
        if (ProdNum3 == 1):
            Profit3 = 120.44 * QuanNum3
        elif (ProdNum3 == 2):
            Profit3 = 99.50 * QuanNum3
        elif (ProdNum3 == 3):
            Profit3 = 75.69 * QuanNum3
        elif (ProdNum3 == 4):
            Profit3 = 65.73 * QuanNum3
        elif (ProdNum3 == 5):
            Profit3 = 51.49 * QuanNum3
        else:
            if (ProdNum3 == 0):
                Profit3 =0
    if Time_Period ==4:
        if (ProdNum4 == 1):
            Profit4 = 120.44 * QuanNum4
        elif (ProdNum4 == 2):
            Profit4 = 99.50 * QuanNum4
        elif (ProdNum4 == 3):
            Profit4 = 75.69 * QuanNum4
        elif (ProdNum4 == 4):
            Profit4 = 65.73 * QuanNum4
        elif (ProdNum4 == 5):
            Profit4 = 51.49 * QuanNum4
        else:
            if (ProdNum4 == 0):
                Profit4 = 0
                ProdNum5 = 0
                ProdNum6 = 0
    if Time_Period ==4:
        if (ProdNum5 == 1):
            Profit5 = 120.44 * QuanNum5
        elif (ProdNum5 == 2):
            Profit5 = 99.50 * QuanNum5
        elif (ProdNum5 == 3):
            Profit5 = 75.69 * QuanNum5
        elif (ProdNum5 == 4):
            Profit5 = 65.73 * QuanNum5
        elif (ProdNum5 == 5):
            Profit5 = 51.49 * QuanNum5
        else:
            if (ProdNum5 == 0):
                Profit5 = 0
                ProdNum6 = 0
    
    if Time_Period ==4:
        if (ProdNum6 == 1):
            Profit6 = 120.44 * QuanNum6
        elif (ProdNum6 == 2):
            Profit6 = 99.50 * QuanNum6
        elif (ProdNum6 == 3):
            Profit6 = 75.69 * QuanNum6
        elif (ProdNum6 == 4):
            Profit6 = 65.73 * QuanNum6
        elif (ProdNum6 == 5):
            Profit6 = 51.49 * QuanNum6
        else:
            if (ProdNum6 == 0):
                Profit6 = 0
        
        totalprofit = Profit1 + Profit2 + Profit3 + Profit4 + Profit5 + Profit6
        
    if Time_Period == 4:
        if totalprofit >=10000:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID GREAT THIS PERIOD!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")
        else:
            print("YOUR TOTAL PROFIT IS",totalprofit,"YOU DID NOT REACH YOUR GOAL KEEP TRYING!")
            print("You can calculate the profit of the company according to a specific day or by a week or divide the week into weekdays and weekend")

####################
############
###END



    


 






