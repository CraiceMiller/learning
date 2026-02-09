from My_Statistics import *
import My_Statistics as My_Statistics 
#new thing, zip()
#17/7/2025

#desviancion estandar de una poblacion indeed works
#desviancion estandar de una muestra indeed works


# 
def main()->None:
    list_a = [154, 48, 167, 235, 20, 32, 282, 138, 228, 189]
    list_b = [130, 233, 196, 228, 281, 158, 94, 49, 25, 224]
    list_c = [155, 110, 274, 237, 286, 108, 23, 114, 168, 278]
    list_d = [141, 146, 110, 69, 131, 175, 260, 210, 67, 216]
    list_e = [125, 45, 257, 281, 161, 274, 98, 153, 21, 292]
    list_f = [153, 83, 189, 51, 153, 53, 94, 35, 187, 116]
    list_g = [42, 138, 153, 150, 119, 294, 125, 94, 14, 28]
    list_h = [150, 106, 162, 190, 64, 266, 111, 36, 249, 50]
    list_i = [117, 82, 57, 97, 45, 15, 262, 203, 46, 21]
    list_j = [148, 137, 220, 55, 91, 160, 186, 69, 277, 25]
    list_xyz=[1,3,14]
  

    all_data:list[list] = [list_a,list_b,list_c,list_d,list_e,list_f,list_g,list_h,list_i,list_j,list_xyz]

    num = 1
    for data in all_data:
        print("_"*40 +f"RESULTS OF LIST NO.{num}"+"_"*40)
        print(data)
        print(f"Media Arimetmetica: {media(data)}")
        print(f"Lenght: {len(data)}")
        
        nums = [(x-media(data))**2 for x in data ]
        varianza = sum(nums) / (len(nums)-1)
        print()
        for numbers,result in zip(data,nums):
            print(f"{numbers}-{media(data)} = {numbers-media(data)}^2 = {result}")
        print(f"Result of the sum: {sum(nums)}")
        print()



        print(f"Varianza: {varianza:.2f}")
        #print("Desviacion estandar de poblacion: ",end="")
        #print(desviacion_poblacion(data))
        print()
        print("Desviacion estandar de una muestra: ", end="")
        print(desviacion_muestra(data))
        print()

        num += 1

    #:| did i really do this for my own ?, i still can´t belive it...




def main_2()->None:
    list_num:list[tuple] = [(40,49),(50,59),(60,69),(70,79)]
    frequancies:list[int] = [3,10,1,1]

    exercise_3 = {'numbers':[(35,39),(40,44),(45,49),(50,54),(55,59),(60,64),(65,69)],
                  'frequancies':[1,3,5,11,7,7,1]
                  }
    
    exercise_1 = {'numbers':[(0.00,0.49),(0.5,0.99),(1.00,1.49),(1.50,1.99),(2.00,2.49),(2.50,2.99)],
                  'frequancies':[31,1,0,2,0,1]
                  }
    
    exercise_4 = {'numbers':[(42,45),(46,49),(50,53),(54,57),(58,61)],
                  'frequancies':[25,14,7,3,1]
                  }
    
    exercise_2 = {'numbers':[(96.5,96.8),(96.9,97.2),(97.3,97.6),(97.7,98.0), (98.1,98.4),(98.5,98.8),(98.9,99.2),(99.3,99.6)],
                  'frequancies':[1,8,14,22,19,32,6,4]
                  }
    
    list_exercises = [exercise_1,exercise_2,exercise_3,exercise_4]

    for index, values in enumerate(list_exercises,start=1):
        print("-"*50+f"Exercise No{index}"+"-"*44)
        print()
        numbers= values["numbers"]
        frequancies=values["frequancies"]
        Desviacion_estandar_poblacion(numbers,frequancies)
        print("\n")
        Desviacion_estandar_muestra(numbers,frequancies)
        print("\n")
        print()
        print("-"*94)

    print("Good luck Master!...")





if __name__ == '__main__':
    main_2()