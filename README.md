# Complex Number Operations using OOP (Python)

## 📌 Project Description

This project demonstrates the implementation of **Complex Number operations** using **Object-Oriented Programming (OOP)** in Python.

The program performs:

* Addition of complex numbers
* Subtraction of complex numbers

## 🧠 Concepts Used

* Classes and Objects
* Constructor (`__init__`)
* Operator Overloading (`__add__`, `__sub__`)
* User Input Handling
* Conditional Statements

## ⚙️ Working of the Program

### 1. Class Definition

A class `Complex` is created to represent a complex number.

python
class Complex:

Each object has:

* `real` → real part
* `img` → imaginary part

### 2. Constructor (`__init__`)

python
def __init__(self, real, img):

This initializes:

* real part
* imaginary part

### 3. Addition of Complex Numbers
python
def __add__(self, other):

* Adds real parts
* Adds imaginary parts
* Returns a new Complex object

### 4. Subtraction of Complex Numbers

python
def __sub__(self, other):

* Subtracts real parts
* Subtracts imaginary parts

### 5. Display Function

python
def display(self):

Displays the result in custom format.

### 6. User Input

The program takes input separately:

text
Enter first real number
Enter first imaginary number
Enter second real number
Enter second imaginary number

👉 These values together represent two complex numbers:

* First number → (real1 + img1 i)
* Second number → (real2 + img2 i)

### 7. Operator Selection

User selects operation:

text
+ → Addition  
- → Subtraction  

### 8. Object Creation

python
c1 = Complex(real1, img1)
c2 = Complex(real2, img2)

Two objects are created representing complex numbers.

### 9. Operation Execution

Based on user input:

python
if operand == "+":
    c3 = c1 + c2
or
python
elif operand == "-":
    c3 = c1 - c2

### 10. Output Display

Final result is displayed using:

python
c3.display()

## ▶️ Example Run

text
Addition and Subtraction of two Complex Numbers

Enter first real number: 3
Enter first imaginary number: 4
Enter first real number: 1
Enter first imaginary number: 2
Enter the operator + or -: +

Output:
4 i + 6 j

## 📁 Project Structure

text
complex-number-project/
│
├── main.py
└── README.md

## 🎯 Learning Outcomes

* Understanding of OOP concepts
* Use of operator overloading
* Working with user input
* Designing mathematical models using classes
