#04/07/2025
from classes_to_use import ToDoList

#new thing all()

def main()->None:

    is_running = False 
    user: ToDoList = ToDoList(name="Master")
    things_to_do:list[str]=["Add a new task", "Select a task as complete", "Modify the urgency of a tak","Delate a task","Exit"]


    print("-"*30)
    print("PYTHON TO DO LIST MINI PERSONAL PROJECT")

    print(f"Hi {user.name} these are your tasks to do..."\
              f" what do you wanna do today?")

    while not is_running:

        print("-"*100)
        #this show all the tasks
        user.show_tasks()
        #this will show all things to do
        print("-"*100)
        num = 1
        for i in things_to_do:
            print(f"{num}.{i}")
            num +=1

        if all(user.is_complete):
            print(f"Congratulation {user.name} you have completed all your tasks...")
            desicion = input("do you wanna stay and keep adding new task...?: ").lstrip().lower()
            if desicion != "yes":
                break
            else:
                select = 1
        else:
            select =input("select a number: ")

        try:
            select = int(select)

            match select:
                case 1:
                    new_task = "1"

                    while new_task.isdigit():
                        new_task = input(f"{user.name} write down a taks: ")
                    
                    user.add_task(new_task)
                case 2:
                    while True:
                        try:
                            complet = input("write a the number of the task to change: ")
                            complet = int(complet)
                            if complet > len(user.tasks) or complet <=0:
                                print(f"{user.name} write a number within the range")
                                continue 
                            break

                        except ValueError:
                            print(f"{user.name} a number please!!...")
                            continue 

                    user.complet_task(complet)

                    pass
                case 3:
                    #this will give us the what task modify...
                    while True:
                        try : 
                            task_to_modify = input("what task do you want to modify[select a numbers]: ")
                            task_to_modify = int(task_to_modify)

                            while task_to_modify > len(user.tasks) or task_to_modify <= 0:
                                print(f"{user.name} pleser write a valid input....")
                                t = input()
                                try: 
                                    task_to_modify = int(t)
                                except ValueError:
                                    continue 

                            break

                        except ValueError:
                            print(f"{user.name}!!!")

                    #this will give us the urgency to modify 
                    modify_task = 0
                    while True:
                        kind_of_urgency = ["Low","Medium","High"]
                        num = 1
                        for i in kind_of_urgency:
                            print(f"{num}.{i}")
                            num+=1

                        test_modify = input(f"{user.name} select a number: ")
                        try:
                            test_modify=int(test_modify)
                            #     0    >=   8    >      3
                            if  0 >= test_modify or test_modify > len(kind_of_urgency):
                                print(f"{user.name} type a number within the range, please...")
                                continue 

                            modify_task = test_modify
                        
                        except ValueError:
                            print(f"Plese {user.name} type a number...")
                            continue 
                        break


                    user.modify_importance(task_to_modify,modify_task)
                case 4:
                    while True:
                        try:
                            delate = input("write a the number of the task to change: ")
                            delate = int(delate)
                            if delate > len(user.tasks) or delate <=0:
                                print(f"{user.name} write a number within the range")
                                continue 
                            break

                        except ValueError:
                            print(f"{user.name} a number please!!...")
                            continue 

                    user.delate_task(delate)


                    

                    pass
                case 5:
                    is_running = True


        except ValueError as e:
            print("Please write a valid input")
            continue 
    print(f"{user.name}, I hope you like this...")
        


if __name__ == '__main__':
    main()