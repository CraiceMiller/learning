import customtkinter as ctk #type: ignore
from bank import Bank #type: ignore
from typing import Any, Callable
from file_detection import FileManager,my_dict_binary #type: ignore


ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")




class SignIn(ctk.CTkToplevel):

   
    def __init__(self,master=None):
       super().__init__(master=master)

       #setting the appereance
       window_color=self.cget("bg")
       self.geometry("400x500")
       self.title("Sing up")

       #
       main_frame=ctk.CTkFrame(self,fg_color=window_color)
       main_frame.pack(fill="y")

       #
       self._label_message=ctk.CTkLabel(main_frame,text="Please Enter your data")
       self._label_message.pack(fill="x",pady=15)


       #
       ctk.CTkLabel(main_frame,text="User Name").pack(pady=10)
       self.user_name=ctk.CTkEntry(main_frame,placeholder_text="Enter your user Name")
       self.user_name.pack(pady=10,fill="x")

       ctk.CTkLabel(main_frame,text="Password").pack(pady=10)
       self.password=ctk.CTkEntry(main_frame,placeholder_text="Enter your Password")
       self.password.pack(pady=10,fill="x")



       ctk.CTkButton(main_frame,text="Sign in ",command=lambda: self.enter(master)).pack(pady=10)


    def enter(self,master_)->None: 
        """This will close the TopLevel only if the user and the password was found"""

        if self.validing_account(master_): 

            #accesing the data base
            accounts:list[dict]=master_.DATABASE
            accounts.sort(key=lambda word:word["user"])
            index=my_dict_binary(accounts,"user",self.user_name.get())

            #Updating the values
            master_.customer_information = accounts[index]

            master_.balance= accounts[index]["balance"]
            master_.wallet= accounts[index]["wallet"]
            master_.debt=accounts[index]["debt"] 
            master_.name=accounts[index]["username"]
            master_.user=accounts[index]["user"]
            master_.password=accounts[index]["password"]
            master_.id = accounts[index]["id"]

            
            master_.hello()
            print("ID: ", master_.customer_id)

            self.destroy()

    def validing_account(self,master_)->bool:
        """
        DESCRIPTION: 
            This method will attempt to find the find both the user and password of the
            customer. 

        RETURN: 
            a True meaning that the user and the password was found, False otherwise
        
        """

        accounts:list[dict]=master_.DATABASE

        accounts.sort(key=lambda user:user["user"])

        index_user:int=my_dict_binary(accounts,"user",self.user_name.get())
        password_user:str=accounts[index_user]["password"]


        if  index_user == -1: 
            self._label_message.configure(text="The user provided was not found, Try again")
            return False
        

        if self.password.get() != password_user: 
            self._label_message.configure(text="The password provided does not match with the data storage, Try again")
            return False


        return True



class BankOunt(ctk.CTk,Bank):
    """
    I start 22/08/2025 at 20:00 hrs this proyect.
    End 24/08/205 at 18:00, working during the whole day and night :(  

    with this i will try to apply evrything regards to: 
        1. customtkinter
        2. classes
    
    Overall Goal:
        Create a mini app thata resemble a bank page where you can interac with your fictioary 
        money through the implementation of class, customtkinter, file manipulation and json files. 

    Objetives:
        1. Create the font-end
        2. create the backend
        3. create the storage database system
        4. create the user acount base.

    1. Backend
        - Create the code where interact all the money, names, debts of each customer
        - If the custumer do not have an account, create a very basic form to it 
        - create reports in word, excel with the resumen of all the info 

     2. Font-end
        -Use customtkinter to create a very friendly  
        -here the customer can check their balance      
    """
    #class variables
    bt_color1: str="#16292F"
    bt_color2: str="#074047"
    bt_color3: str="#1C8585"
    bt_color4: str="#1DA27D"
    bt_color5: str="#F9F8F2"
    botton_corner: int= 40

    PATH_DATABASE:str=r"C:\Users\Usuario Pc\Desktop\Learning_Python\User Accounts.json"
    DATABASE:list[dict]=FileManager().read_json(PATH_DATABASE,False)
    
    def __init__(self,
                 balance:float=0,
                 wallet:float=0,
                 debt:float=0, 
                 name:str="user",
                 user:str="N/A",
                 password:str="N/A",
                 id: int = 0)->None:
        
        Bank.__init__(self,balance,wallet,debt,name,user,password,id)
        super().__init__()

        #Information needed 
        self._customer_id:int=id
        # This prevents it from being garbage collected
        self.toplevel_window = None

        #If the customer information is None will opne de sign up window 
        if self._customer_id ==0: 
            self.open_toplevel_window()




        #setting the appereance
        self.geometry("1000x600")
        self.title("Bankount LLT.")

        self.grid_columnconfigure(0,weight=2)
        self.grid_columnconfigure(1, weight=4) # The right side is wider
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


        #variables needed 
        window_color=self.cget("bg")

        #
        self._number: int= 2



        

        #setting the frames
        frameRight=ctk.CTkFrame(self)
        frameRight.grid(row=0, column=0,  sticky="news")

        rightbottom=ctk.CTkFrame(frameRight,height=100)
        rightbottom.pack(fill="x",side="bottom")

        frameBottom=ctk.CTkFrame(self,height=500)
        frameBottom.grid(row=1, column=1, sticky="ews")
        
        frameinfo=ctk.CTkFrame(self)
        frameinfo.grid(row=0, column=1, sticky="new",pady=60)


        framemoney=ctk.CTkFrame(self)
        framemoney.grid(row=0, column=1, sticky="new",pady=200)


        #Setting buttons
        self.botton(rightbottom,"Sign-In",self.open_toplevel_window).pack(pady=10,side="top")
        self.botton(rightbottom,"Save Information ",self.save_info).pack(pady=10,side="top")
        self.botton(rightbottom,"Withdraw ",self.hello).pack(pady=10,side="top")
        self.botton(frameBottom,"Search",self.hello).pack(padx=10,side="left")

        #Setting the info frames
        frameBalance=ctk.CTkFrame(frameinfo,fg_color=self.bt_color4)
        frameBalance.pack(fill="both",side="left",padx=10,expand=True)

        frameWallet=ctk.CTkFrame(frameinfo,fg_color=self.bt_color4)
        frameWallet.pack(fill="both",side="left",padx=10,expand=True)

        frameDebt=ctk.CTkFrame(frameinfo,fg_color=self.bt_color4)
        frameDebt.pack(fill="both",side="left",padx=10,expand=True)

        #Info frames labels and text
        ctk.CTkLabel(frameBalance,
                     text="BALANCE",
                     font=ctk.CTkFont(family="Arial",size=20,weight="bold",underline=True),
                     text_color=self.bt_color5
                     ).pack(side="top",pady=10)
        
        self.balancelabel=ctk.CTkLabel(frameBalance,
                     text=f"{self._balance:.2f}",
                     font=ctk.CTkFont(family="Arial",size=40,weight="bold"),
                     text_color=self.bt_color5
                     )
        self.balancelabel.pack(side="top",pady=10)
        
        #Info frames labels and text
        ctk.CTkLabel(frameWallet,
                     text="WALLET",
                     font=ctk.CTkFont(family="Arial",size=20,weight="bold",underline=True),
                     text_color=self.bt_color5
                     ).pack(side="top",pady=10)
        
        self.walletlabel=ctk.CTkLabel(frameWallet,
                     text=f"{self._wallet}",
                     font=ctk.CTkFont(family="Arial",size=40,weight="bold"),
                     text_color=self.bt_color5
                     )
        self.walletlabel.pack(side="top",pady=10)

        #Info frames labels and text
        ctk.CTkLabel(frameDebt,
                     text="DEBT",
                     font=ctk.CTkFont(family="Arial",size=20,weight="bold",underline=True),
                     text_color=self.bt_color5
                     ).pack(side="top",pady=10)
        
        self.debtlabel=ctk.CTkLabel(frameDebt,
                     text=f"{self._debt}",
                     font=ctk.CTkFont(family="Arial",size=40,weight="bold"),
                     text_color=self.bt_color5
                     )
        self.debtlabel.pack(side="top",pady=10)

        self.interactive=ctk.CTkLabel(self,
                                      text="Hello :3",
                     font=ctk.CTkFont(family="Arial",size=15,weight="bold"),
                     text_color=self.bt_color5
                     )
        self.interactive.grid(row=0,column=1,sticky="n",pady=250)




        #setting Entries
        self.text_entry=ctk.CTkEntry(frameBottom,
                                corner_radius=50,
                                placeholder_text="Entry your text")
        
        self.text_entry.pack(fill="both")



        self._entry_withdraw=ctk.CTkEntry(framemoney,
                                          placeholder_text="Enter the amount to withdraw")
        self._entry_withdraw.pack(fill="both",side="left",padx=5)

        self.botton(framemoney,"Withdraw",self.withdrawmoney).pack(fill="both",side="left",padx=5)

        self._entry_deposit=ctk.CTkEntry(framemoney,
                                          placeholder_text="Enter the amoutn to Deposit")
        self._entry_deposit.pack(fill="both",side="left",padx=8)

        self.botton(framemoney,"Deposit",self.depositmoney).pack(fill="both",side="left",padx=5)

        self._entry_pay=ctk.CTkEntry(framemoney,
                                          placeholder_text="Enter the amoutn to Pay")
        self._entry_pay.pack(fill="both",side="left",padx=5)

        self.botton(framemoney,"Pay",self.paymoney).pack(fill="both",side="left")





        #Setting labels 
        self._name_bank=ctk.CTkLabel(frameRight,
                                 text="Bankount",
                                 font=ctk.CTkFont(family="Arial",size=30,weight="bold",underline=True)
                                 )
        self._name_bank.pack(side="top")


        self._label_=ctk.CTkLabel(self,
                            text=f"Welcome to Bankout Dear {self._name}",
                            font=ctk.CTkFont(family="Helvetica",size=40,weight="bold",underline=True))
        self._label_.grid(row=0,column=1,sticky="n")

        
        
    #This will open a top level window, will not work if there is a user already
    def open_toplevel_window(self):
        """
        Creates and shows the Toplevel window.
        Checks if a Toplevel window is already open.
        """
        # Prevents opening multiple Toplevel windows
        if self._customer_id !=0: 
            print("You alredy Sign-in")
            return 

        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = SignIn(self)
            
        else:
            self.toplevel_window.focus() # If window already exists, focus on it


    #This only will update the value s
    def hello(self)->None:
        self._label_.configure(text=f"Welcome to Bankout Dear {self._name}")
        self.balancelabel.configure(text=f"{self._balance:,.2f}")
        self.walletlabel.configure(text=f"{self._wallet:,.2f}")
        self.debtlabel.configure(text=f"{self._debt:,.2f}")


        self.text_entry.delete(0,ctk.END)
    

    #This funtion will save all the current info, and storage into a json file 
    def save_info(self)->None: 
        """
        DESCRIPTION: 
            After to do everything, this method will save tall the change during this time
        
        """

        if self._customer_id == 0: 
            print("You can do this now")
            return 
        
        INFORMATION= {
            "id": self._id,
            "user": self._user,
            "password": self._password,
            "balance": self._balance,
            "wallet": self._wallet,
            "username": self._name,
            "debt": self._debt
        }
  

        FileManager().update_json(self.PATH_DATABASE,
                                  "id",
                                  self._customer_id,
                                  **INFORMATION)
        print("Everything was succelly save. have a nce day :)")
        self.interactive.configure(text="Your current state was successully done. Have a nice day")



    #Main funtion to interact with the money 
    def withdrawmoney(self)->None: 
        try: 
            money=float(self._entry_withdraw.get())

        except ( TypeError, ValueError):
            self.interactive.configure(text="It must be a number")
            return 

        



        if not self.withdraw_amount(money):
            self.interactive.configure(text="The transation was not complet")
            return 


        self.interactive.configure(text="Everything goes well...")
        self.hello()
        self._entry_withdraw.delete(0,ctk.END)
        
        
    
        print("ok")

        pass
    
    def depositmoney(self)->None: 
        try: 
            money=float(self._entry_deposit.get())

        except ( TypeError, ValueError):
            self.interactive.configure(text="It must be a number")
            return 

        



        if not self.deposit(money):
            self.interactive.configure(text="The transation was not complet")
            return 


        self.interactive.configure(text="Everything goes well...")
        self.hello()
        self._entry_deposit.delete(0,ctk.END)

        
        
    
        print("ok")

        pass
    
        
    def paymoney(self)->None: 
        try: 
            money=float(self._entry_pay.get())

        except ( TypeError, ValueError):
            self.interactive.configure(text="It must be a number")
            return 

        



        if not self.pay__debt(money):
            self.interactive.configure(text="The transation was not complet")
            return 


        self.interactive.configure(text="Everything goes well...")
        self.hello()
        self._entry_pay.delete(0,ctk.END)

        
        
    
        print("ok")

        pass
    

    #Helper methods 
    @classmethod
    def get_info_user(cls, id_:int)->dict:
        index=my_dict_binary(cls.DATABASE,
                             "id",
                             id_)
        return cls.DATABASE[index]

    def __repr__(self)->str: 
        return Bank.__repr__(self)


    @classmethod
    def botton(cls,master:Any,
               name:str,
               purpose:Callable,)->ctk.CTkButton: 
        """This is my own template of a button"""
        
        return ctk.CTkButton(master, #this one will alwyas be needed
                             
                      #The main purpose of the button 
                      text=name,
                      command= purpose,

                      #customazing 
                      font=ctk.CTkFont(family="Helvetica",
                                         size=15,
                                         slant="italic",
                                         weight='bold'),

                      corner_radius=cls.botton_corner,
                      state="normal",

                      #changing the color 
                      text_color=cls.bt_color5,
                      fg_color=cls.bt_color4,
                      hover_color=cls.bt_color3,
                      border_color=cls.bt_color2,
                      text_color_disabled=cls.bt_color1

                      )


    @property 
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self,value:str): 
        if not isinstance(value,int) : 
            raise TypeError("The new value must be an a valid number ")
        
        if value < 0: 
            raise TypeError("The new value must be greaten than zero  ")



        print("The change was successully done")
        self._customer_id = value

    #This method will help me to work whti this entire logic in a simple way
    def run(self)->None: 
        """This method will help me to work whti this entire logic in a simple way"""
        Bank.run(self)
        self.save_info()

"""
    {
        "user": "mysafetyplace.54@gmail.com",
        "password": "you//don'Tn33d1T",
        "balance": 702.77,
        "wallet": 285,
        "username": "Craice Miler",
        "debt": 0
    },

"""



col="""
----------------------------------------
       |COLUMN 0 | COLUMN 1 | COLUMN 2 |
----------------------------------------
ROW 0 |
----------------------------------------
ROW 1 |
----------------------------------------
ROW 2 |
----------------------------------------


n=top
s: botton
w:left
e: right

{
        "user": "mysafetyplace.54@gmail.com",
        "password": "you//don'Tn33d1T",
        "balance": 702.77,
        "wallet": 285,
        "username": "Craice Miler",
        "debt": 0
},


"""



class InitBank:
    INFO=BankOunt.DATABASE


    @classmethod
    def initiation(cls, id_=int)->BankOunt:
        """
        This funtion will only storage all info into the bankout class,if there is a key error, 
        will return a empty BankOunt class. \n
            Craice: 1234
            Hersy: 1235
            Ashley: 1236
        """
        index=my_dict_binary(cls.INFO,"id",id_)

        if index != -1: 

            try: 

                return BankOunt(
                    balance=cls.INFO[index]["balance"], 
                    wallet=cls.INFO[index]["wallet"], 
                    name=cls.INFO[index]["username"],
                    debt=cls.INFO[index]["debt"],
                    id=cls.INFO[index]["id"],
                    user=cls.INFO[index]["user"],
                    password=cls.INFO[index]["password"]
                )
            except (KeyError,IndexError): 
                return BankOunt()

        return BankOunt()



if __name__ == "__main__": 
    bank=InitBank.initiation(1236)

    #bank.run()


    bank.mainloop()



