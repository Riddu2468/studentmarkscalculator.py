

m1 = int(input("enter engish marks:"))
m2 = int(input("enter hindi marks:"))
m3 = int(input("enter marathi marks:"))
m4 = int(input("enter maths marks:"))
m5 = int(input("enter science marks:"))
m6 = int(input("enter ssd marks:"))
total= m1+m2+m3+m4+m5+m6
print("your toatl marks is :", total)
if m1 >= 35 and m2 >= 35 and m3 >= 35 and m4 >= 35 and m5 >= 35 and m6 >= 35: print("pass")
else:
 print("fail")
percentage = total / 6
print(round(percentage,2),"%") 
