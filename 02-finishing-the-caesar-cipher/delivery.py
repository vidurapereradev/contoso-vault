DAYS_IN_WEEK: int = 7


#lab activity
day: int = int(input("Day: "))
delivery_day: int = 0

if 1 > day or day > DAYS_IN_WEEK:
    print("Invalid day")

else:
    
    days_to_wait = int(input("Days to wait: "))

    if 0 > days_to_wait or days_to_wait > DAYS_IN_WEEK: 

        print("Invalid days to wait")
    else:
        delivery_day = (day + days_to_wait)
        if delivery_day > DAYS_IN_WEEK:
            delivery_day -= DAYS_IN_WEEK
            print("Delivery day: ", delivery_day)
        else:
            print("Delivery day: ","Delivery will be within today!" )

assert 0 <=  delivery_day <= DAYS_IN_WEEK, "Delivery day must be between 0 and 7"


 