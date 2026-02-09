players:list[str] = []
def create_character(name: str, role:str,*abilities:tuple[str], level:str ="Begginer", starting_gold:float= 100.00, exp:int = 0, **additional_info:dict )-> None:
    print("-----------A new character has been added------------")
    players.append(name)
    print()
    print("Name: " + name)
    print("Role: " + role)
    print("Level: " + level)
    print(f"Exp: {exp:,}")
    print(f"Gold: G.{starting_gold:,.2f}")
    print()
    print("Abilities: ")
    for i in abilities:
        print(f"- {i}")
    print()
    if additional_info == {}:
        print("Curently this character doesn't have any extra info ")
        
    else:
        print("Extra info: ")
        for key, value in additional_info.items():
            print(f"{key}: {value}")
    print()



create_character("Craice",
                 "Archer",
                 "health", "bleeding", "Eager eye",
                 starting_gold= 500.00,
                 exp=48,
                 level="Medium",
                 origin="Altisora",
                 weapon="The blesing bow",
                 languague="English"
                 )

create_character("Ashley",
                 "Healther",
                 "Blessing", "Holy water",
                 )

create_character("Hersy",
                 "Heroe",
                 "Bleeding", "dash", "autohealt", "recicly", "Killer", "retrieve", "honorability",
                 level="Master",
                 starting_gold= 875269.425,
                 exp= 584202,
                 languague=("enlgish", "Alistoriano", "spanish", "elf"),
                 weapon=["The sacred Blade", "The flamming blade", "The fairy bow", "the killer shield "],
                 hours_play="325 Hours",
                 achivement=["rescue the princess", "help a village", "become a heroe", "The honorable heroe of the nation "])

print("currently these are the list of player at hand:")
for player in players:
    print(player, end=" ")
    