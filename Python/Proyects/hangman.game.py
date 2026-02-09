from random import choice
from list_words import words



#dict of key:()
hangma_art:dict[int,str]={0:("  ",
                             "   ",
                             "   "),

                          1:(" ° ",
                             "   ",
                             "   "),
                          2:(" ° ",
                             " | ",
                             "   "),
                          3:(" °",
                             "/|\\ ",
                             "   "),
                          4:(" ° ",
                             "/|\\ ",
                             "   "),
                          5:(" ° ",
                             "/|\\ ",
                             "/   "),
                          6:(" ° ",
                             "/|\\",
                             "/ \\ "),
                             }

# just print the art
def print_hangman(index):
   print("*"*10)
   for i in hangma_art[index]:
      print(i)
   print("*"*10)
      

#print each line 
def display_hint(hint):
   print(" ".join(hint))
   pass

def display_answer(answer):
   pass

   

def main():
   pc_chosse:str=choice(words).lower()
   hint:list = ["_"] * len(pc_chosse)
   wrong_gueses:int=0
   guessed_letters:set=set()
   _isrunning:bool=True

   print("-"*15+"HANGMAN"+"-"*15)

   while _isrunning:
      

      #this will display the man...
      print_hangman(wrong_gueses)
      #this will chek it this should run again or not...
      if wrong_gueses == 6:
         print("\n\n")
         print(f"Sucha loser...")
         print(f"the answer was '{pc_chosse}'")
         break

      display_hint(hint)
      print("Guess the letter...")
      guess = input().lower()

      
         

      if len(guess) !=1 :
         print("invalid input")
         print("\n\n")
         continue

      if guess in guessed_letters:
         print(f"{guess} is already guessesd")
         print("\n\n")
         continue

      guessed_letters.add(guess)

      if guess in pc_chosse:
         for i in range(len(pc_chosse)):
            if pc_chosse[i] == guess:
               hint[i] = guess
      else:
         wrong_gueses += 1

      print("\n\n")

      if not "_" in hint:
         print("you win...")




         _isrunning:bool=False

      

   
        
    

            


    
 

  





   





if __name__ == "__main__":
   main()








      

