import random
from math import sqrt
from typing import Union 
from math import ceil
#08/07/2025
"""
Description:
this is my own module where it storages a little of info

My notes:
Here you'll just find simple formulas, like moda and mitad de rango, nothing more, 
Nonetheless i did my best to do it all by myself, and i think i'm proud of it 

Update 1.0.0: 08/07/2025


Special Grettings:
To Proffesor Federico
To Gemini AI

"""

#k_.py
def media(numbers:list[int])->float:
  #formula: sum(x) / n
  result = round(sum(numbers) / len(numbers),2)
  return result  

def mediana(numbers:list[int])->float:
  #this is just show the middle number of the list...
  numbers.sort()

  if len(numbers) % 2 ==0:
    x = len(numbers) / 2 - 1
    x = int(x)
    first= numbers[x]
    x += 1
    second=numbers[x]

    result=int ( (first + second) / 2)

    return result 
  
  else: 
    x = len(numbers) / 2 
    x = int(x)
    return x

def moda(numbers:list[int])->int:
 #this will gave how many repereated numbers there are whithin a list...
  moda_ = []
  counts = {}


  for num in numbers:
    counts[num] = counts.get(num, 0) + 1

  max_number = max(counts.values())


  if max_number !=1:
    for key,value in counts.items():
        if value == max_number:
          moda_.append(key)
  
  
  if  moda_:
    return moda_
  else:
    return None

def mitad_rango(numbers:list[int])->float:
  max_number=max(numbers)
  min_number=min(numbers)

  result= (max_number - min_number) / 2
  return result 

def rango(numbers:list[int])->float:
  max_number=max(numbers)
  min_number=min(numbers)

  result= max_number - min_number
  return result 
 
def desviacion_poblacion(numbers:list[int])->float:
  #formula: sum((x-_x))**2 / n

  nums = [(x-media(numbers))**2 for x in numbers ]
  varianza = sum(nums) / len(numbers)
  return round(sqrt(varianza),2)

def desviacion_muestra(numbers:list[int])->float:
  #formula: sum((x-_x))**2 / n-1

  nums = [(x-media(numbers))**2 for x in numbers ]
  varianza = sum(nums) / (len(numbers) -1)
  return round(sqrt(varianza),2)

def marca_clase(numbers:list[int])->float:
  return round(sum(numbers) / 2,2)

def media_marca(numbers:list[int],numbers_2:list[float])->float:
  quantity_1 = sum(numbers) #numbers one in marcas de clase mutiplied 
  quantity_2 = sum(numbers_2) #numbers two is the frecuency
  try:
     result= quantity_1 / quantity_2
     return round(result,2) 
  except ZeroDivisionError as e:
     print(f"An error has occured : {e}")

def get_range_of_list(numbers:list[int],class_n:int)->list[tuple]:
    my_list= numbers
    class_number = class_n
    max_num = max(my_list)
    min_num = min(my_list)

    anchura_clase = ceil((max_num - min_num) / class_number)

    #here is where i code a list of numbers needed 

    first_numbers = []
    first_numbers.append(min_num)
    for i in range(0,class_number-1):
        min_num += anchura_clase 
        first_numbers.append(min_num)
    

    second_numbers = []
    second_numbers.append(max_num)
    for i in range(0,class_number-1):
        max_num -= anchura_clase 
        second_numbers.append(max_num)
    
    second_numbers.reverse()
    info_needed = []

    for fr,sd in zip(first_numbers, second_numbers):
        info_needed.append((fr,sd))

    return info_needed

def get_frequancy(numbers:list[int],class_n:int)->list[int]:
    my_list = numbers
    info_needed = get_range_of_list(numbers,class_n)

    frequancy = []
    for numbers in info_needed:
        a,b = numbers
        xy = {}
        for i in range(a,b+1):
            xy[i]=my_list.count(i)

        addition = sum(xy.values())
        frequancy.append(addition)

    return frequancy


def Desviacion_estandar_poblacion(number_1:list[tuple],number_2:list[int])->None:
    overall_list =[16, 187, 160, 141, 147, 284, 299, 218, 38, 91, 160, 67,
                  12, 81, 295, 90, 176, 30, 162, 159, 94, 182, 86, 254, 255, 195, 36, 28,
                    291, 265, 121, 132, 17, 125, 50, 5, 49, 197, 167, 106, 97, 13, 155, 291,
                      159, 94, 182, 251, 162, 245, 55, 131, 265, 179, 250, 17, 174, 148, 45,
                        68, 45, 47, 72, 69, 123, 101, 140, 256, 158, 95, 39, 152, 199, 289,
                          157, 23, 203, 5, 83, 105, 93, 204, 240, 263, 300, 84, 101, 140, 256, 
                          158, 95, 39, 152, 199, 289, 133, 262, 147, 190, 206, 196, 222, 211, 
                          298, 28, 180, 98, 247, 23, 203, 5, 83, 105, 146, 272, 167, 268, 107, 
                          124, 124, 76, 166, 294, 224, 20, 274, 210, 166, 195, 291, 127, 243,
                            118, 175, 222, 11, 136, 259, 8, 134, 53, 178, 83, 234, 264, 219,
                              242, 143, 119] 
    classes_wanted = 6

    #this will storage any numbers we want
    ages:list[tuple] = number_1
    f:list[int] = number_2

    print(ages)
    print(f)

    #this will storage all info needed in a dictionary
    #btw the reason i create a dict was that if we wanna change the values above,
    # everything below will still the same.. well at leat i think so...
    quantities = {}

    for age_range, frequency in zip(ages, f):
        quantities[age_range] = frequency

    #now i try to get the marca de clase
    marcas = []
    for mc in quantities.keys():
        marcas.append(marca_clase(mc))
    
    #frecuencia multipy by marca
    _x_f_ = [round(frequency * marca,2) for frequency,marca in zip(quantities.values(),marcas) ]

    # this will give us the division  of _x_f_ and the frequancies 
    frequancies = [fr for fr in quantities.values()] #these are the frequancies
    media_frequancy = media_marca(_x_f_,frequancies)

    #now i can do this (x-m);the subration of the marca and the media frecuancy
    x_m = [round(x-media_frequancy ,2)for x in marcas]

    #this will give the power of x_m
    _x_m_2_ = [round(x**2,2 )for x in x_m]

    #now this give us the multiplication of the _x_m_2_ by the frequancies
    multiplycation_xm2 = [round(x*f,2 )for x,f in zip(_x_m_2_,frequancies)]

    
    #it is time to get the varianza...
    varianza = round(sum(multiplycation_xm2) / sum(frequancies),2)

    #now is time to get the result after everything i did
    #desviacion estandar de una pobalcion
    O  = round(sqrt(varianza),2)

 
    #this just will show what i did so far...
    print("-"*25 +"POBLACION ESTANDAR DE UNA POBALCION"+"-"*25)
    print(f"{"Ages":<18}{"f":<15}{"x":<15}{"x*f":<15}{"(x-m)":<15}{"(x-m)^2":<15}{"(x-m)^2*f":<15}")
    for age,f,x,xf,xm,xm2,xm2f in zip(quantities.keys(),quantities.values(),marcas,_x_f_,x_m,_x_m_2_,multiplycation_xm2):
        print(f"|{age}|{f:<15}|{x:<15.2f}|{xf:<15.2f}|{xm:<15.2f}|{xm2:<15.2f}|{xm2f:<15.2f}|")
    print("-"*90)

    
    print(f"Adittion of frequancies: {sum(frequancies)}")
    print(f"Adittion of x*f: {sum(_x_f_)}")
    print(f"Adittion of (x-m)^2*f: {sum(multiplycation_xm2)}")
    print(f"M = {round(media_frequancy,2)}")
    



    print(f"Varianza= {varianza}")
    print(f"O= {O}")


def Desviacion_estandar_muestra(number_1:list[tuple],number_2:list[int])->None:
    """
    Description: 
    this will give us the table of the "Desviacion Estandar de una Muestra" based on the
    formula: sum(f(x-_x_)^2) / n -1 .
    """
    overall_list =[None] 
    classes_wanted = None

    #this will storage any numbers we want
    ages:list[int] = number_1
    f:list[int] = number_2

    

    #this will storage all info needed in a dictionary
    #btw the reason i create a dict was that if we wanna change the values above,
    # everything below will still the same.. well at leat i think so...
    quantities = {}

    for age_range, frequency in zip(ages, f):
        quantities[age_range] = frequency

    #now i try to get the marca de clase
    marcas = []
    for mc in quantities.keys():
        marcas.append(marca_clase(mc))
    
    #frecuencia multipy by marca
    _x_f_ = [round(frequency * marca,2) for frequency,marca in zip(quantities.values(),marcas) ]

    # this will give us the division  of _x_f_ and the frequancies 
    frequancies = [fr for fr in quantities.values()] #these are the frequancies
    media_frequancy = media_marca(_x_f_,frequancies)

    #now i can do this (x-m);the subration of the marca and the media frecuancy
    x_m = [round(x-media_frequancy ,2)for x in marcas]

    #this will give the power of x_m
    _x_m_2_ = [round(x**2,2 )for x in x_m]

    #now this give us the multiplication of the _x_m_2_ by the frequancies
    multiplycation_xm2 = [round(x*f,2 )for x,f in zip(_x_m_2_,frequancies)]

    
    #it is time to get the varianza...
    varianza = round(sum(multiplycation_xm2) / (sum(frequancies)-1),2)

    #now is time to get the result after everything i did
    #desviacion estandar de una pobalcion
    S = round(sqrt(varianza),2)

 
    #this just will show what i did so far...
    print("-"*25 +"POBLACION ESTANDAR DE UNA MUESTRA"+"-"*25)
    print(f"{"Ages":<18}{"f":<15}{"x":<15}{"x*f":<15}{"(x-m)":<15}{"(x-m)^2":<15}{"(x-m)^2*f":<15}")
    for age,f,x,xf,xm,xm2,xm2f in zip(quantities.keys(),quantities.values(),marcas,_x_f_,x_m,_x_m_2_,multiplycation_xm2):
        print(f"|{age}|{f:<15}|{x:<15.2f}|{xf:<15.2f}|{xm:<15.2f}|{xm2:<15.2f}|{xm2f:<15.2f}|")
    print("-"*90)

    
    print(f"Adittion of frequancies (minus -1): {sum(frequancies)-1}")
    print(f"Adittion of x*f: {sum(_x_f_)}")
    print(f"Adittion of (x-m)^2*f: {sum(multiplycation_xm2)}")
    print(f"M = {round(media_frequancy,2)}")
    



    print(f"Varianza= {varianza}")
    print(f"S= {S}")


    

# 
def main_():
  a = [16, 187, 160, 141, 147, 284, 299]
  b = [218, 38, 91 ,160, 67]
  c = [12, 81, 295, 90, 176, 30, 162, 159, 94,182]
  d = [86, 254 ,255, 195 ,36, 28, 291, 265 ,121, 132, 17]
  e = [125, 50, 5 ,49 ,197 ,167 ,106, 97, 13 ,155, 291]
  f = [159, 94 ,182, 251 ,162, 245 ,55, 131, 265, 179, 250]
  g = [17, 174, 148, 45 ,68, 45, 47, 72, 69, 123]

  h= [101, 140, 256, 158, 95, 39 ,152 ,199, 289, 157]
  i= [23, 203, 5, 83, 105, 93, 204, 240, 263,300, 84]
  j= [101, 140, 256 ,158 ,95, 39, 152, 199, 289]
  k= [133, 262 ,147, 190, 206, 196, 222]
  l= [211, 298 ,28 ,180, 98, 247 ,23, 203, 5,83 ,105]
  m= [146, 272, 167, 268, 107, 124, 124, 76, 166, 294, 224, 20]
  n= [274 ,210 ,166, 195, 291, 127, 243, 118, 175, 222, 11 ,136]
  o= [259, 8 ,134 ,53, 178 ,83, 234, 264, 219, 242 ,143, 119]
  numbers_list = [16, 187, 160, 141, 147, 284, 299, 218, 38, 91, 160, 67,
                  12, 81, 295, 90, 176, 30, 162, 159, 94, 182, 86, 254, 255, 195, 36, 28,
                    291, 265, 121, 132, 17, 125, 50, 5, 49, 197, 167, 106, 97, 13, 155, 291,
                      159, 94, 182, 251, 162, 245, 55, 131, 265, 179, 250, 17, 174, 148, 45,
                        68, 45, 47, 72, 69, 123, 101, 140, 256, 158, 95, 39, 152, 199, 289,
                          157, 23, 203, 5, 83, 105, 93, 204, 240, 263, 300, 84, 101, 140, 256, 
                          158, 95, 39, 152, 199, 289, 133, 262, 147, 190, 206, 196, 222, 211, 
                          298, 28, 180, 98, 247, 23, 203, 5, 83, 105, 146, 272, 167, 268, 107, 
                          124, 124, 76, 166, 294, 224, 20, 274, 210, 166, 195, 291, 127, 243,
                            118, 175, 222, 11, 136, 259, 8, 134, 53, 178, 83, 234, 264, 219,
                              242, 143, 119]

  another_numbers_list = [
      73, 15, 201, 88, 5, 112, 27, 190, 42, 137,
      60, 233, 9, 175, 31, 296, 104, 18, 252, 77,
      149, 280, 6, 92, 163, 24, 117, 205, 48, 188,
      301, 71, 14, 215, 99, 1, 10, 126, 26, 170,
      35, 290, 81, 154, 220, 53, 19, 139, 28, 65,
      258, 2, 79, 108, 172, 40, 227, 94, 156, 33,
      110, 29, 200, 7, 185, 4, 129, 25, 168, 86,
      230, 59, 192, 13, 271, 96, 3, 115, 22, 177,
      44, 293, 76, 145, 210, 51, 16, 100, 30, 181,
      244, 62, 198, 8, 260, 11, 130, 20, 173, 46
  ]

  p = []
  for x in range(1000):
    p.append(random.randint(1,10000))

  r=[3,4,7,8,10]

  all_data = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,numbers_list,another_numbers_list,p,r]

  num = 1
  for data in all_data:
    print("_"*40 +f"RESULTS OF LIST NO.{num}"+"_"*40)

    print(f"Media Aritmetica: ",end="")
    print(media(data))
    print()
    print(mediana(data))
    print()
    print(moda(data))
    print()
    print(mitad_rango(data))
    print()
    print("Desviacion estandar de poblacion: ",end="")
    print(desviacion_poblacion(data))
    print()
    print("Desviacion estandar de una muestra: ", end="")
    print(desviacion_muestra(data))
    print()

    num += 1

  #:| did i really do this for my own ?, i still can´t belive it...

if __name__ == '__main__':
  main_()

