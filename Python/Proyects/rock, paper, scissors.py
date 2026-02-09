import random 





is_running: bool = True

while is_running:
    option: tuple[int] = ('rock', 'paper', 'scissors')
    player: str = None
    ia = random.choice(option)

    print('write your choose')
    print('rock', 'paper', 'scissor')
    player: str = input()

    while player not in option:
        
        print()
        print('please player, write a choose, i wanna play so bad')
        print('write your choose')
        print('rock', 'paper', 'scissors')
        player: str = input().lstrip()

    print(f"Player: {player}")
    print(f"Computer: {ia}")
    print()

    if player == ia:
        print('well, i guess its a tie :|')
        print()
    elif player == 'rock' and ia == 'scissors':
        print('oh, you win :)')
        print()
    elif player == 'scissors' and ia == 'paper':
        print('oh, you win :)')
        print()
    elif player == 'paper' and ia == 'rock':
        print('oh, you win :)')
        print()
    else:
        print('such a loser!!')
        print()

    if input('Wanna play again dude? [yes or no]: ').lower() != "yes":
        is_running: bool = False

print()
print('Thank you so much for playing my game!!')
    
    
