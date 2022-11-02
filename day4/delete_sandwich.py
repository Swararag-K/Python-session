
sandwich_orders=["Chicken","veg","Chicken","Cheese","Tuna","Chicken"]
length=len(sandwich_orders)
finished_sandwiches=[]
for i in range(length):
    if sandwich_orders[i]=="Chicken" :
        print("Chicken not available")
        
    else:    
        print("I made your ",sandwich_orders[i]," sandwich")
        finished_sandwiches.append(sandwich_orders[i])
    
print(finished_sandwiches)    
