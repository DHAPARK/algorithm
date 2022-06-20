T = int(input(""))

for i in range(T):
    cm, kg = map(float,input("").split(" "))
    if cm < 140.1:
        print("6")
        continue
    if cm >= 140.1 and cm < 146:
        print("5")
        continue
    if cm >= 146 and cm < 159:
        print("4")
        continue
    
    bmi = kg / ((cm / 100) * (cm / 100))
    if cm >= 159 and cm < 161:
        if (bmi >= 16.0 and bmi < 35.0):
            print("3")
            continue
        else:
            print("4")
            continue
    
    if cm >= 161 and cm < 204:
        if (bmi >= 20.0 and bmi < 25.0):
            print("1")
            continue
        elif ((bmi >= 18.5 and bmi < 20.0) or (bmi >= 25.0 and bmi < 30.0)):
            print("2")
            continue
        elif ((bmi >= 16.0 and bmi < 18.5) or (bmi >= 30.0 and bmi < 35.0)):
            print("3")
            continue
        elif ((bmi < 16.0) or (bmi >= 35.0)):
            print("4")
            continue
    
    if cm >= 204:
        print("4")
