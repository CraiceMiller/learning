from file_detection import FileManager #type: ignore


"""
1. NEVER USE THREADDING WITH TWO SAME FILES AT THE SAME TIME. BECUSE IT WILL CORRUPTED IT
2. The file has weight, if the has zero (0) bytes, it will cuz an error. This means the file is 
empty

"""

python_docx:str = r"C:\Users\Usuario Pc\Desktop\python.docx"

f=FileManager()


#print(f.write_word(python_docx,"Hello World!"))



print("Size: ", f.get_file_size(python_docx))
print("Ok")
print(f.word_styles(python_docx))