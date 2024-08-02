def task_manager():

    actions_dictionary = {}

    while True:
        selected_action = input('''
                        What Operation would you like to perform?
                        1 : View
                        2 : Add
                        3 : Remove
                        4 : Complete
                        5 : exit
                        ''')
        try:
            selected_action = int(selected_action)
            if selected_action not in range(1,6):
                print("Operation selected not in rage of valid operations")
                continue
        
        except:
            print("Unknown operation error")

        if selected_action == 1:
            view_taks(actions_dictionary)

        if selected_action == 2:
            add_task(actions_dictionary)

        if selected_action == 3:
            remove_task(actions_dictionary)

        if selected_action == 4:
            complete_task(actions_dictionary)

        if selected_action == 5:
            print("Bye!...")
            break

        again = input("Do you want to perform another operation? Y - N ") 

        if again == "Y" or again == "y":
            continue
        elif again == "N" or again == "n":
            print("Bye!...")
            break
        else:
            break

        

def view_taks(actions_dictionary):

    if not actions_dictionary:
        print("There are no Tasks or Status to display at this time")
        return

    print("Your Tasks Manager shows the following activities: " )
    for value in actions_dictionary:
        print(f" - Task: {value}  Status: {actions_dictionary[value]}")
        
    return


def add_task(actions_dictionary):
    task = input("What task would you like to add? ")
    status = input('''  What status would you like to add to your task?
                        1 : Pending
                        2 : Complete
                        ''')
    status = int(status)
    if status > 0 and status <= 2:
        if status == 1:
            actions_dictionary[task] = "Pending"
        else:
            actions_dictionary[task] = "Complete"
    else:
        print("Invalid Status Selected")
    return

def remove_task(actions_dictionary):

    available_tasks = ""
    for key in actions_dictionary.keys():
        available_tasks = available_tasks + "- " + key  + "\n"
    
    print("The following tasks are available for deletion: \n" + available_tasks)
    delete_task = input("Which Task would you like to delete? (Please select from one of the task in the list above) ")

    deleted_task = actions_dictionary.pop(delete_task)
    print(f"Task: {delete_task} was deleted from the list of tasks")

    return



def complete_task(actions_dictionary):
    available_tasks = ""
    for key in actions_dictionary.keys():
        available_tasks = available_tasks + "- " + key  + "\n"
    
    print("The following tasks are available for Update: \n" + available_tasks)
    update_task = input("Which Task would you like to Update? (Please select from one of the task in the list above) ")

    status = input('''  What status would you like to update on the task selected?
                        1 : Pending
                        2 : Complete
                        ''')
    status = int(status)
    if status > 0 and status <= 2:
        if status == 1:
            actions_dictionary[update_task] = "Pending"
        else:
            actions_dictionary[update_task] = "Complete"
    else:
        print("Invalid Status Selected")
    return


print(task_manager())
