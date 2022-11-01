mark=[]
print("Enter 5 marks")
for i in range(5):
    mark.append(int(input()))
sum=0
for i in range(5):
    sum=sum+mark[i]
print("sum :")    

if sum >=400:
    print("A")
elif sum>=300 and sum<400:
    print("B")
elif sum>=200 and sum<300:
    print("c")    
elif sum>=100 and sum<200:
    print("D")
else:
    print("F")    
