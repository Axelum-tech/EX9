order_food_names = ["pizza", "salad", "soup"] #list>str
order_food_price = [ 75.00,   45.00 ,  15.00] #list> float
order_food_q     = [     2,       1 ,      2] #list> int



for i in range(len(order_food_price)):  
    print(i+1,order_food_names[i], order_food_price[i],"u.c", order_food_q[i])
    

for i in range(len(order_food_price)):
    TOTAL=order_food_price[i]*order_food_q[i]
    print("TOTAL=",TOTAL)




    # if i==2: 
    #     print("TOTAL=",order_food_price[0]*order_food_q[0]+order_food_price[1]*order_food_q[1]+order_food_price[2]*order_food_q[2] )
    #     print(order_food_price[i]*order_food_q[i])


    
  
  
    

    


#HW2: calculate total-> print