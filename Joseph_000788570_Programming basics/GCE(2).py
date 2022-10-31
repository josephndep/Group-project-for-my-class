###  Version 1.0 python 3
###  Name: JOSEPH N.
#### SAIT number: 000788570

#################################################################################################
# START


print("Welcome to the Global bill calculator!")
print("     ")
#acc_num = account number
acc_num = int(input("Enter account number: "))

month = int(input('Enter month: '))  
while month not in{1,2,3,4,5,6,7,8,9,10,11,12}:  #include the while loop to end process incase the format was
    print('Incorrect month format....Process ended') #was input incorrectly

#elec_plan = electricity plan to select between the fixed rate and floating rate
elec_plan = str(input('Enter your electricity plan (EFIR or ELFR):'))
while elec_plan not in{"EFIR","EFLR"}:
    print("Incorrect format..Process ended")
# elec_amt = input the amount of electricity used in kwh     
elec_amt = float(input(f"Enter the amount of electricity you used in month {month} (in KWh): "))

#gas_plan = natural gas plan to select between the fixed rate and floating rate
gas_plan = str(input("Enter your gas plan (GFIR or GFLR): "))
while gas_plan not in {"GFIR", "GFLR"}:
    print("incorrect format... Process ended")

# gas_amt = input the amount of natural gas used in GJ  
gas_amt = float(input(f"Enter the amount of gas you used in month {month} (in GJ): "))
#prov = diffrent provinces have a diffrent gst percentage
prov = str(input("Enter the abbreviation for your province of residence (two letters): "))

# calculate the amount of electricity used in C$d = kwh
if (elec_plan == "EFIR"):
    if (elec_amt <= 1000):
        kwh = elec_amt * 0.0836
    else:
        kwh = elec_amt * 0.0941
else:
    (elec_amt == "EFLR")
    kwh = elec_amt * 0.0911
    
# calculate the amount of natural gas used in C$d = gj
if (gas_plan == "GFIR"):
    if (gas_amt <= 950):
        gj = gas_amt * 0.0456
    else:
        gj = gas_amt * 0.0589
else:
    (gas_plan == "GFLR")
    gj = gas_amt * 0.0393
#fixed_gj = added transaction fee for natural gas which is 0.0132cents(c$d1.32)    
fixed_gj = gj + 0.0132
total_amt = fixed_gj + kwh + 120.62
#total_amt = total natural gas + electricity + 120.62....120.62 is the fixed monthly fee
#province= gst applied depending percentage tax in different provinces
if(prov == "AB" or prov == "BC" or prov == "NB" or prov == "NT"or prov == "NU" or prov == "QC" or prov == "SK"or prov == "YT" ):
    gst = total_amt * 0.05
    total_due = gst + total_amt
elif(prov == "NB"or prov == "NL"or prov =="NS"or prov =="PE" ):
    gst = total_amt * 0.15
    total_due = gst + total_amt 
elif(prov == "ON"):
    gst = total_amt * 0.13
    total_due = gst + total_amt
else:
    while prov not in {"AB","BC","NB","NT","NU","QC","SK","YT","ON","NB","NL","NS","PE"}:
        print('Incorrect format....Process ended') #Terminate process if incorrect input is registered
 #statement printed       
print(f"Thank you! Your amount due c${total_due:.2f}")


#END
#################################################################################################

        