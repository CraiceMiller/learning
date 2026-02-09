#4/8/2025
import random as r
from dataclasses import dataclass,field
import time as t
from classes_to_use import MyWatch as m


@dataclass(order=True,slots=True)
class Player:
    """
        DESCRIPTION: 
            This class only storage the very basic info of a person (player in this case)
        
        PARAMETERS: 
            _players: this only is a str that will storage the name of the player
            _is_alive: this only will track if the person is alive as a bool

        RETURN:
            A Player object
        """
    _player:str

    _is_alive:bool=field(init=False, default=True)
    _money:float|int=field(init=False, default=0.00)


    pass

class SquidGame:
    Available_player:list[Player]=[]
    Leave:bool=False
    False_True:list=[True,False]
    final_prize:int=0
    amount_per_death:int=484705


    def __init__(self, player:Player)->None:
        """
        DESCRIPTION: 
            This funtion only track the people here, and storage the info in a list of Player
            The class Player is create in another place i think...

        PARAMETERS:
            It must have a player object

        RETURN:
            Nothing
        """
        self._player=player
        SquidGame.Available_player.append(player)

    @classmethod
    def kill(cls, person:Player)->Player:
        """
        DESCRIPTION: 
            This funtion only simulate the action of kill a person. Base of the module random.choice
            and a list of [True, False]. If choice pick True the person die, keeps alive otherwise

        RETURN:
            A Player object
        """
        chossing=cls.False_True
        person._is_alive = r.choice(chossing)
        return person
     
    @classmethod
    def wanna_leave(cls,)->None:
        """
        DESCRIPTION: 
            This funtion only simulate the people votes, Counts the votes. If the amounts of 
            votes is greater than the amount of players or the is only two 
             players left the game is over

        RETURN:
            Nothing, due this funtion only do an action, nothing more, print a massge
            based on the currently situation though.
        """
        count_votes:int=0
        alives=cls.display_alive_player()

        if ( len(alives) <=2):
            print("the game is over")
            cls.Leave=True 
            return 

        for vote in alives:
    
            if r.choice(cls.False_True):
                count_votes += 1
        
        if count_votes > (len(alives) // 2):
            print("The majority of players decided to leave")
            cls.Leave=True
            return 
        else:
            print("The majority wants to keep playing")

    @classmethod
    def divide_price(cls)->int|float:
        """
        DESCRIPTION: 
                This funtion only dived the prize money equally.
                it will return zero (0)if there is no people

            RETURN:
                int or float
        """
        try: 
            return cls.final_prize / len(cls.display_alive_player())
        except ZeroDivisionError:
            return 0


    @classmethod
    def give_price(cls)->None:
        """
        DESCRIPTION: 
                This funtion only simulate the money given 

            RETURN:
                nothing
        """
        alive=cls.display_alive_player()
        for player in alive:
            player._money = cls.divide_price()



    
    @classmethod
    def text(cls, person:Player)->str:
        """
        DESCRIPTION: 
            This funtion only give a text base if a peson is death or alive

        RETURN:
            A str
        """
      
        alive=cls.display_alive_player()

        if not person._is_alive:
            return f"Player No. {person._player} has dead"

        return f"Player No. {person._player} has passed the game"
    

    @classmethod
    def game_1(cls)->None:
        """
        DESCRIPTION: 
            This simulate a kind of killing game..

        RETURN:
            nothing cuz this funtion only do an action 
            
        """

        availables=cls.display_alive_player()


        for player in availables:
            cls.kill(player)
            t.sleep(0.05)
            print(cls.text(player))

            if not player._is_alive:
                cls.final_prize += cls.amount_per_death
       

  
    @classmethod
    def display_alive_player(cls)->list[Player]:
        """
        DESCRIPTION: 
            This funtion only track the currect alive person

        RETURN:
            A list of Player
        """

        alives:list[Player]=[p for p in cls.Available_player if p._is_alive ]
        return alives
     
    


def add_playes(player:int)->None:
    """
    DESCRIPTION: 
        This funtion only create a new Player class and add it into the class 
        SquidGame. The given number will be storage as a str (eg,. 001,011, or 111)
        

    PARAMETERS: 
        player: this is only an int that will be the name ( in this case should be a number
        eg,. 1)

    RETURN:
        Nothing
    """

    if player<10:
        SquidGame(Player(f"00{player}"))
        return 
    if player <100:
        SquidGame(Player(f"0{player}"))
        return
    
    SquidGame(Player(f"{player}"))
  

def main()->None:


    num_players:int= 456
  
  
    for i in range(1,num_players+1):
        add_playes(i )

    SquidGame.display_alive_player()

    num_game:int=1
    

    while  any(x._is_alive for x in SquidGame.Available_player):
        alives=SquidGame.display_alive_player()
        if SquidGame.Leave:
            SquidGame.give_price()

            break

    
        print(f"Currently players: {len([i._is_alive for i in alives])} ")
        print(f"Currently Final Prize ${SquidGame.final_prize:,}")
        print(f"Amount of each peson ${SquidGame.divide_price():,}")
        print()

        t.sleep(2)
        print(f"The game No.{num_game} is starting now")
        print()
        SquidGame.game_1()
        print()
        print("\nPlayer are deciding if they wants to continue")
        t.sleep(2)
        SquidGame.wanna_leave()
        print()

        if SquidGame.Leave:
            SquidGame.give_price()
            break

        num_game += 1
        print(f"\nThe {len(SquidGame.display_alive_player())} are waiting untill the next day..")
        m.countdown(5)
        print()

        
        
    remaining:list=[player for player in SquidGame.display_alive_player() ]
 

    if []:
        print("no peaple alive")
    else:
        print(f"Remainging players: {len(SquidGame.display_alive_player())}")
        print(f"Final Price {SquidGame.final_prize:,}")
        print(f"Amount of each peson ${SquidGame.divide_price():,}")
        print(f"Name: {remaining[0]._player}, Money: {remaining[0]._money}")

        SquidGame.Available_player.clear()


        
    

    


    

if __name__ == "__main__":
    main()