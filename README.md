# Learning something new everyday

## Introduction

---
All started on May 1, 2026 at 20:00hrs. all thanks to my computer teacher that taught me how to create a very simple form on VBA. later I start to learn python, html, css, typescript, react. This repository is just an evidence of my very awful beginning code... i guess :3.

Today is 2026-02-09 Sunday at 13:00 and I am currently learning how to use git to create my respository

Sorry beforehand for my bad english.

## In this Repository

Here i will update all my progress of what i learn regards languagues.

### Langugues

1. Python
2. Java
3. Typescript
4. VBA
5. HTML
6. CSS
7. MySql
8. Git
9. Bash

## Python

---
Learned on May 01 2025 at 20:00hrs, This was my very first languague i learned. I started wathcing vidoes on internet. I expericed a lot of stuff in here. and I took me around one month to get used in all of this field, programming itself. I really love this language, I dunno, it is very simple very frinedly that make me feel that i can  create several thing. but its speed is too much for my 32-bits old computer :v that it always need to wait aroung five minutes to print a little single thing.

```python
print("Never give in no matter what ")
```
## HTML and CSS 

---

## JavaScript and TypeScript

---
```typescript 
console.log("It will be a lot of scary stuff out there");
```



## Java

---
Started to learned on 01.01.2026, in order to leran **Object-Oriented Programming**. I just had a few ideas of what was a class, but here i could understand the fundamentals of it.

1. encapsulation 
2. polymorphism
3. inherentance
4. abstraction 

```java
public class Main{
    public static void main(String[] args){
        System.out.println("You must faced them over and over again,but one day, that pain will worth it...");
    }
}
```


## Git 
---

## MySQL

---

## Terminal 

## PowerShell



### Comands 

|command|shorcut|description|
|-|-|-|
|Get-ChildItem|ls | |
| Set-Location|cd |  |
| Copy-Item |cp |  |
| Remove-Item |rm |  |
|Get-Content  |cat |to read the content of a file  |
|Invoke-Item | |to open an item  |
| Stop-Process | | to close an app |
| Start-Process | |to open an app  |
|Get-Member  | |it show us the methods and properties of an object...  |
|Get-help  | |  |
|Start-Sleep  | |it wait untill a certain amount of time...  |



### Symples Commands
This will help us to the see the Types of the parameter the function needs and the return type. 
like i do in python with simple hover it...
```powershell
Get-Help <function, object name> -full
```

```python 
def fn()-><type>
```

### Type 
 




### Bash
 
```bash
echo "Coding is more than just write line of instruction, is another mindset, very tired and tough to learn. "
```



## VBA

This was my very first programming language ever. here is where all started, thank to my computer teacher,Profe Federico of thrid grade of high school when i was 18, he taught us how to create a very simple form in excel. and well i like it a lot.

Today 08.03.2026 Sunday i wnated to learning again in order to do autmactly my job and stop doing tedious thing. like i manually copy paste paste 8 columns but the last ones must be in the number 11 (L COLUNM). based on my expirence in other languges, i feel this a strange combination of typescript and java.

### Kind of Errors
---

In VBA and Excel, errors are not just "bugs"—they are **specific return values**. 
Use this guide to debug your code and handle exceptions.


### 1. The "Big Five" Error Reference
| Error | Name | Developer's Translation | Common Cause |
| :--- | :--- | :--- | :--- |
| **#NULL!** | Null Error | Range Syntax Error | Missing a comma or colon in a range (e.g., `=SUM(A1 A2)`). |
| **#DIV/0!** | Division Error | `ArithmeticException` | Dividing by zero or an empty cell. |
| **#VALUE!** | Value Error | **Data Type Mismatch** | Trying to do math on a String (e.g., `10 + "Apple"`). |
| **#REF!** | Reference Error | `NullPointerException` | The cell/sheet the formula pointed to was **Deleted**. |
| **#NAME?** | Name Error | **Syntax/Scope Error** | Misspelled function or function is `Private` in VBA. |
| **#N/A** | Not Available | "Not Found" | Lookup value doesn't exist in the target range. |

---

### 2. VBA "Guard Clauses" (Handling Errors)

When reading a cell that might contain an error, always check it first to prevent a **Type Mismatch** crash.

```vba
Dim cellVal As Variant
cellVal = Range("A1").Value

If IsError(cellVal) Then
    Debug.Print "Error detected: " & Range("A1").Text
    ' Handle error logic here
Else
    ' Proceed with logic
End If


### Range Methods

|Method | Description |
|------|-------------|
|.Clear |delete everything | 
|.clearContent |delete only the data, leaving formulas and style | 
|.Delete  |remove the cell | 
|.ClearFormat |delete the styles and formulas | 
|.Copy  |you can move the data from another cell | 
|.PasteSpecial | This just let us to paste it with different formats, like paste with values| 
|.Select  |I dunno | 
|.Active  |dunno | 
|.Show  |it move the windows untill the selected cell | 
|.Merge / UnMerge |combine or split a serie of cell |
|.RemoveDuplicates  |as it says It remove all the duplicates | 
|  | | 
|  | | 
|  | | 

### WorkSheets Methods

|Method | Description |
|------|-------------|
|  | | 
|  | | 
|  | | 
|  | | 
|  | | 




```bas
sub main()
    MsgBox("Even if you reach you limit...")
End sub
```

# Sources

---

- [bro code](https://www.youtube.com/@BroCodez)

I only storage a lot of language, too much knwoladge and i am not fluently in any of them. but I like code thing that works :). it makes me feel real.
TODO:keep writting your progress
