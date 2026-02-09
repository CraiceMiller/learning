from  classes_to_use import Bank


user_1:dict[str,float|str]={"name":"Hersy","balance":150,"wallet":80.25} 
user_2:dict[str,float|str]={"name":"Craice","balance":702.77,"wallet":285}
user_3:dict[str,float|str]={"name":"Ashley","balance":59.55,"wallet":20}

all_users=[user_1,user_2,user_3]
Bank()


for user in all_users:
    a,b,c=user.get("name"),user.get("balance"),user.get("wallet")
    user_acount=Bank(name=a,balance=b,wallet=c)
    if a == "Hersy":
        user_acount.deposit()

    if a == "Craice":
        user_acount.withdraw()







   
       



