def skating_day_message(month_num, day_num):
    message1 = "World Ice Skating Day is coming up!"
    
    if month_num == 12:
        if day_num == 4:
            message1 = "YAY! It's World Ice Skating Day!"
        elif day_num > 4:
            message1 = "You just missed it. There's another next year!"
            
    
    return message1

print(skating_day_message(8,8)) 