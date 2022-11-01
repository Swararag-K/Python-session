toppings=[]
print("Enter the toppings")
for i in range(100):
    toppings.append(input())
    if toppings[i]=="quit":
        break
    
print("Your toppings are")
print(toppings)
