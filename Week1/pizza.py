def pizza_satisfaction(pizza_size, cheese_multiplier):
  
    ret_message = "very satisfied"

    if pizza_size >= 10:
        if cheese_multiplier >= 2:
            ret_message = "really satisfied"
    
    if pizza_size >= 12:
        if cheese_multiplier >= 3:
            ret_message = "maximally satisfied"    

   

    return ret_message
    pass

print(pizza_satisfaction(11, 2))