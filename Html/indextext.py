from js import document, fetch #type: ignore
import asyncio
from time import perf_counter
async def read_local_file():
    try:
        # We use 'fetch' to get the file over the network (even if it's on your local machine)
        response = await fetch('./Learning_Tread')
        text = await response.text()
        
        # Now we write the content of the file to the HTML element
        document.getElementById('my-text-output3').innerHTML = text
        print("Successfully read and displayed the file content.")
    except Exception as e:
        document.getElementById('my-text-output3').innerHTML = "Could not load the file."
        print(f"An error occurred: {e}")

start=perf_counter()
#asyncio.ensure_future(read_local_file())


print("Hello world form pythn file...")
text1 = "Here is just a normal paragh written in python file"
text2 = "I'm learning new things"

document.getElementById('my-text-output').innerHTML = text1
#document.getElementById('my-text-output2').innerHTML = text2
end=perf_counter()
final=end - start 
print(f"The operation run in {final:.2f} seconds")

"""
So my structure in my vscode editor is looking something like this: 
Learing Python
    Html
        index.html
        indextext.py
        Learning Tread.txt


Is it well structured or not?

"""