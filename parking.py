p = [None, None, "BMW", None, None, "TOYOTA", "BMW"]

user_car_brand =input("Name your brand: ")
user_park_index=int(input("What place? "))
total    = len(p)
free     = 0
BMW      = 0
MERCEDES = 0
TOYOTA   = 0

if p[user_park_index]==None:
    print("Ok, your place is ready")
    p[user_park_index]=user_car_brand
else:
    print("Sorry the place is occupied")




for i in range(len(p)):
    if p[i]==None:
        free+=1
   
print("Parking (free/total):",free,"/",total,"places")
for i in range(len(p)):
    if p[i]== "BMW":
        BMW+=1
    

    elif p[i]=="TOYOTA":
        TOYOTA+=1
    
   
    elif p[i]=="MERCEDES":
        MERCEDES+=1
    
    
print("# BMW-",BMW)
print("# TOYOTA-",TOYOTA)
print("# MERCEDES-",MERCEDES)






