def calories(entree_num, side_num, dessert_num, drink_num):
    # menu = {
    #     "Entree":{
    #         "1": ["Hamburger", 522],
    #         "2": ["Veggie Burger", 399],
    #         "3": ["Impossible Burger", 501]
    #         },
    #     "Side": {
    #         "1": ["French Fries", 130],
    #         "2": ["Sweet Potato Fries", 125],
    #         "3": ["Salad", 72]
    #     },
    #     "Dessert" : {
    #         "1": ["Apple Pie", 222],
    #         "2": ["MilkShake", 391],
    #         "3": ["Fruit Cup", 100]
    #     },
    #     "Drink" : {
    #         "1": ["Diet soft drink", 10],
    #         "2": ["Coffee", 8],
    #         "3": ["Martini", 120]
    #     }

    # }

    menu = {
        "Entree":{
            "1": 522,
            "2": 399,
            "3": 501
            },
        "Side": {
            "1": 130,
            "2": 125,
            "3": 72
        },
        "Dessert" : {
            "1": 222,
            "2": 391,
            "3": 100
        },
        "Drink" : {
            "1": 10,
            "2": 8,
            "3": 120
        }

    }

    entree_cals = menu.get("Entree").get(str(entree_num))
    side_cals = menu.get("Side").get(str(side_num))
    dessert_cals = menu.get("Dessert").get(str(dessert_num))
    drink_cals = menu.get("Drink").get(str(drink_num))

    return entree_cals + side_cals + dessert_cals + drink_cals

print(calories(2,2,2,2))