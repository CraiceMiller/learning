import time
print('WELCOME TO MY QUIZ GAME!!!')
time.sleep(10)


questions = ("Cual es la contraseña que usa el fisacal Von Karma?:",
             "Cual es el truco secreto de Kokichi?: ",
             "En donde se presenta por primera vez a la entrenadora Cynthia?: ",
             "Que estaba  haciendo Vent/Alie, al comenzar Megaman XZ?: ",
             "Despues de una larga travesia junto con una chica de cabello color esmeralda, se convertio en rey de su respetivo reino, sin embargo el fallece despues de ser capturado debido a sus multiples herridas. Dejando a mercer de su Hija Lilina a un joven de roja cabellera:",)

options = (("A.Von_Karma_1 ", "B. 0001 ", "C.1000 ", "D.2007 "), 
           ("A.Los engaños ", "B.Las mentiras ", "C.Su habilidad ", "D.La ganzua "),
           ("A. Ciudad Pirita ", "B. Lago Veraz ", "C. Cuidad Eterna ", "D. Ciudad Pradera "),
           ("A. Paseando con su maestro ", "B. Salvando al mundo ", "C. Explorando  la zona C-2 ", "D. Realizando una entrega "),
           ("A. Jaffar ", "B. Eliwood ", "C. Hector ", "D. Dorcas"))


answers = ("B", "D", "C", "D", "C",)
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    time.sleep(3)
    print()
    for option in options[question_num]:
        print(option)
    
    print('Enter (A, B, C or D): ')
    guess = input().strip().upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('Correct !!')
    else:
        print('Incorrect!! ')
        print(f"{answers[question_num]} is the correct answer")
        
    question_num += 1
    print('\n')


print("----------------------------------")
print("             RESULT               ")
print("----------------------------------")

time.sleep(4)
print('answers: ', end="")
for answer in answers:
    print(answer, end= " ")
print()

print('guesses: ', end="")
for guess in guesses:
    print(guess, end= " ")
print()

i = int(score / len(questions) * 100)
print(f"your score is {i}%")
print('\n')


#................................


# my attemped
print('Do you want continue?(yes/no): ')
again = input().strip().lower()
while again == 'no':
    print('I hope you liked it :)')
    print()
    time.sleep(20)
    print('Do you want continue?(yes/no): ')
    again = input().strip().lower()
     



if again == 'yes':
    print('Ok, lets with another round :) ')
    time.sleep(5)
print('\n')
    

questions_2 = ("En yoshi island DS, cual bebé le permite a yoshi la abilidad de destruir bloques.?:",
             "En Hollow Knight, Cual es el nombre del caballero solemne y noble quien el protagonista encuentra primero bloqueando el camino a Senderos Verdes, quien despues se convierte en un aliado fundamental en la batalla contra la infeccion?: ",
             "En dead Space, Que sistema crucial necesitaba Isaac manualmente restablecer y activar en Ishimura para establecer la comunicacion ?: ",
             "En Danganronpa 2: GoodBye Despair, Cual es el motivo espefico que Monokuma presento en el comienzo del capitulo 4, la cual obligo a uno de ellos a cometer un asesinato en la casa de la risa?: ",
             "Cual es el tipico item que los jugadores utilizan para invocar al Ojo de Cthulhu, En terraria?: ",
             "En Apex legends, quien posee la habilidad unica de crear portales para que los aliados y enemigos puedad usarlos?:  ", 
             "En Professor Layton and the Lost Future, Cual es la verdadera naturaleza de la <<Maquina del tiempo>> que transportaba al Profesor y a Luck al Londres del Futuro?: ",
             "En Majoras Mask, Para conseguir la mascara nocturna Link debe que detener a un ladron al norte de la ciudad reloj; Sin embargo al hacer dicha accion, que mascara se convierte imposible de conseguir?:  ",
             "En Ghost Trick, Para resolver el caso entero se necesitaba realizar acciones para cambiar el futuro. por lo tanto quien fue el verdadero protagista y el heroe responsable de todo esto, desde el principio del juego?: ")

options_2 = (("A.Wario bebé ", "B. Mario bebé ", "C.Peach bebé ", "D.DK bebé "), 
           ("A.Nailsmith ", "B.Hornet ", "C. Cornifer ", "D. Quirrel "),
           ("A. La antena de comunicacion Pirita ", "B. El campo USM ", "C. La unitologia ", "D. El cuarto de comandos "),
           ("A. Revelar su secretos ", "B. Amenzar de ejecucion colectiva ", "C. La interminable sensacion de hambre si un asesinato no ocurria ", "D. Revelar la indentidad de la mente maestra "),
           ("A. El ojo de aspecto sospechoso ", "B. Comida de gusano ", "C. Espina dorsal sangrieta ", "D. El ojo mecanico"),
           ("A. Octane  ", "B. Wraith ", "C. Loba  ", "D. Ash  "),
            ("A. Un artefacto poderoso de un civilzacion antigua ", "B.Un proyecto de holograma  ", "C.Una gran elaborda ciudad falsa bajo tierra  ", "D. Una verdadera maquina del tiempo construida por los cientificos  "),
            ("A. Las mascara de Romani ", "B.Las mascara del capitan  ", "C.Las mascara de Keaton  ", "D.Las mascara de los enamorados  "),
            ("A.Sissel ", "B.Lynne  ", "C. Missile  ", "D.Cabanela  "),)

answers_2 = ("A", "B", "A", "C", "A", "B", "C", "D", "C",)
guesses_2 = []
score_2 = 0
question_num_2 = 0

for question in questions_2:
    print('------------------------------------------------------------------------')
    print(question)
    time.sleep(7)
    print()
    for i in options_2[question_num_2]:
        print(i)

    print('write your answer (A, B, C, D)')
    attemp = input().strip().capitalize()
    guesses_2.append(attemp)

    if attemp == answers_2[question_num_2]:
        score_2 += 1
        print(f'Correct!!, the answer was {answers_2[question_num_2]:_>20} ')

    else:
        print('Wrong!!')

    
    question_num_2 += 1
    print('\n')

print('--------------------------------------------------')
print('                       RESULT                     ')
print('--------------------------------------------------')

time.sleep(4)
print('Guesses:', end= '')
for i in guesses_2:
    print(i, end= ' ')
print()

score_2 = int(score_2 / len(answers_2) * 100)
print(f'your score of this round is {score_2}%')
