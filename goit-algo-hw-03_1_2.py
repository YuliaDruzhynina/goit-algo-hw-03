
from datetime import datetime

def get_days_from_today(data):
    datetime_today = datetime.today()

    try: 
        date_object = datetime.strptime(data, "%Y-%m-%d")
    except Exception:
        print("incorrect date") 
        return  
   
    days_beetwen = datetime_today.toordinal() - date_object.toordinal()
    print(f"Days between: {days_beetwen}")
    return []

get_days_from_today("2024-01-31")  
get_days_from_today("2024-01-20")  




import random
def get_numbers_ticket(min: int, max: int, quantity: int):

    set_number = set()  

    if min >=1 and max <=1000 and quantity > 0 and quantity < max:            
        while len(set_number) != quantity:
                number = random.randrange(min, max)
                set_number.add(number)   

        else: 
            return sorted(set_number)        
    else:            
        print("incorrect date")     
    return []
        
     
lottery_numbers = get_numbers_ticket(10,20,5)
print("Ваші лотерейні числа:", lottery_numbers)



