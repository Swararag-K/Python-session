toppings=[]
print("Enter the toppings")
for i in range(100):
    X=input()
    if X=="quit":
        break
    toppings.append(X)
    
print("Your toppings are")
print(toppings)
