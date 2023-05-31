with open ('currencyDatabase.txt')as f:
    lines=f.readlines()

currencyDict={}
for line in lines:
    parsed=line.split('\t')
    currencyDict[parsed[0]]=parsed[1]
    
amount=int(input("Enter amount:\n"))
print("Enter the name of currency you want to convert this amount to ? Available Option:\n")
[print(item) for item in currencyDict.keys()]
currency=input("Please enter one of these values:\n")
converted_amount=amount *float(currencyDict[currency])
print(f"{amount} INR is equal to {converted_amount}{currency}")
