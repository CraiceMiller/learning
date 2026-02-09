from typing import Literal
from mypython.file_detection import FileManager #type: ignore
class ToDo: 
    thingtodo:str="todo.json"
    def __init__(self)->None: 
        self._isrunning:bool=True
        self._file:FileManager=FileManager()
        self._list_task=self._file.read_json(self.thingtodo,True)


    def filexist(self)->None:
        print("The file does not exist, but I can create one, just wait a minute")
        if self._file.create_json(self.thingtodo):
            print("The file was created try")
 
    
    def complete_task(self,taskName:str)->None:

        for dictionary in self._file.read_json(self.thingtodo,False):
            if dictionary["task"].lower() == taskName.lower(): 
                dictionary["compled"] = True
            

        self.listask=self._file.read_json(self.thingtodo,True)
    



    def create_task(self,task:str,
                    description:str="",
                    priority:Literal["High","Medium","Low"]="Medium",
                    deadline:str|None=None)->None: 
        """
        create a new task
        """
        if not self._file.file_exist(self.thingtodo):
            self.filexist()
            return 
        
        
        
        if self._file.write_json(self.thingtodo,{
            "task":task,
            "description":description,
            "priority":priority,
            "compled":False,
            "deadline":deadline
            }):

            self.listask=self._file.read_json(self.thingtodo,True)
            print("The task was succesfully create")


    def show_tasks(self):
        """
        Display the current task at hand
        """
        if not self._file.file_exist(self.thingtodo):
            self.filexist()
            return 
        
        if not self._list_task.items():
            print("There are no tasks here")
            return 
        
        print(self._list_task)
        

    def run(self)->None:
        while self._isrunning: 
            self.show_tasks()
            print("1. Create Task")
            print("2. Complete task")
            print("3. Exist")

            print("Chose one option")
            chose=input()

            if chose == "1": 
                task=input("Task: ")
                description=input("Description: ")

                priority=None
                while priority not in ['High', 'Medium', 'Low'] or priority =="" or priority is None :
                    print("['High', 'Medium', 'Low'] or press enter to skip")
                    priority=input("Priority:")


                deadline=None
                while not deadline == "" or deadline is  None:
                    print("press enter to skip")
                    deadline=input("Deadline:")

                deadline=None if deadline == "" else deadline
                priority="Medium" if priority == "" else priority
                self.create_task(task,description,priority,deadline) #type : ignore

            if chose == "2": 

                self.complete_task(input("Write the task to complete: "))

            if chose == "3":
                self._isrunning=False

            else:
                print("Chose a valid input")
            
    @property
    def listask(self):
        return self._list_task
    
    @listask.setter
    def listask(self,___value):
        self._list_task = ___value

if __name__ == "__main__": 
    td=ToDo()
    td.run()