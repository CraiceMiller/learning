from whatever.My_Classes.my_mini_store import PlushieStore,Bank
from whatever.My_Classes.my_mini_store import create_new_product,InventaryStore

if __name__ == '__main__':
    #this i only create new  products for the inventary...
    create_new_product('Candies Pop',5.75,150,Taste='Sweet',Color='Red',Size='small')
    create_new_product("Spider Stuffed",24.99,200)  
    InventaryStore.add_more_stock_existing_product("Giant Teddy Bear",47)
    InventaryStore.add_more_stock_existing_product("Spider Stuffed",25)      





def main()->None:
       
    user_1={'user':"mysafetyplace.54@gmail.com","password":"you//don'Tn33d1T","balance":5702.77,"wallet":285,"username":"Craice Miler","debt":0}

    #this are the info of the person 
    name:str="Craice Miler"
    balance:float|int=5702.77
    wallet:float|int=285
    debt:float|int=0
    bag:dict={'books':3,'bottle of water':10,'Snacks':{'candies':7,'chocolate':5}}
    


    user_bank=Bank(
        balance=balance,
        wallet=wallet,
        name=name,
        debt=debt

    )


    a=PlushieStore(user_bank,bag,name)
    a.display_products_to_sell()
    a.selecting_stuff()
    a.show_chart_before_to_buy()
    a.pay_chart()
    a.PACKAGING()
    print(bag)


    #####

    {'user':"hersyis.thebest.334@gmail.com","password":"inDeEd1m_205/","balance":150,"wallet":80.25,"username":"Hersy Halston","debt":10.5}

    name2:str="Hersy Halston"
    balance2:float|int=1000
    wallet2:float|int=80.25
    debt2:float|int=10.5
    bag2:dict={'make-up':3,'soda':4,'Snacks':{'candies':8,'cockies':15}}


    user_bank2=Bank(
        balance=balance2,
        wallet=wallet2,
        name=name2,
        debt=debt2

    )


    b=PlushieStore(user_bank2,bag,name2)
    b.display_products_to_sell()
    b.selecting_stuff()
    b.show_chart_before_to_buy()
    b.pay_chart()
    b.PACKAGING()
    print(bag2)
    pass


if __name__ == '__main__':
    main()


