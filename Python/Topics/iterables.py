def every()->None:
    for _ in range(2):
        print("EVERYTING'S GONNA BE OKAY!")

def trying()->None:
    x = "apple"
    if x.find("a"):
        print(x)
    
def anything()->None:
    every()
    trying()

answer = input().lstrip().lower()

anything() if answer == "yes" else "not at all"
