import speech_recognition as sr
from classes_to_use import MyCalculator

cal=MyCalculator(10,5)




recognizer=sr.Recognizer()
def _get_text()->str:
    global recognizer
    
    with sr.Microphone() as source:
        print("Say something I'm listaning...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

        try: 
            text=recognizer.recognize_google(audio)
            return text.lower()
        except:
            return 'N/A'

def _get_math_result(text:str):
    if "multiplication" in text:
        return f"The multiplication is: {cal.multiplication()}"
    elif "division" in text:
        return f"The division is: {cal.division()}"
    elif "addition" in text:
        return f"The addition is: {cal.addtion()}"
    elif "subtraction" in text:
        return f"The subtraction is: {cal.subtraction()}"
      
    
    return "None"



text:str=_get_text()       
print(f"you said {text}")
if "math" in text:
    print(f"What kind of operationg do you want to do: ")
    chose:str=_get_text()
    print(f"X={cal.x} Y={cal.y}")
    print(_get_math_result(chose))



    







