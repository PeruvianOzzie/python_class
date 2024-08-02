def shortest(route_1, route_2, route_3):
    
    sorted_list = []
    sorted_list.append(route_1)
    sorted_list.append(route_2)
    sorted_list.append(route_3)
    
    sorted_list.sort()
    
    return sorted_list[0]

print(shortest(121892,3333435,4534546))