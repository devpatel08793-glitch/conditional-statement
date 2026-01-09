mark1 = int(input("enter mark 1: "))
mark2 = int(input("enter mark 2: "))
mark3 = int(input("enter mark 3: "))

total_percentage = (100*(mark1 + mark2 + mark3))/300

if(total_percentage >= 40 and mark1 >=33 and mark2>=33 and mark3>=33):
    print("pass :", total_percentage )
    
else:
    print("you fail :", total_percentage)