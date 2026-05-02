class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,other):
        new_real=self.real+other.real
        new_img=self.img+other.img
        return Complex(new_real,new_img)
    def __sub__(self,other):
        new_real=self.real-other.real
        new_img=self.img-other.img
        return Complex(new_real,new_img)
    def display(self):
        print(f"{self.real} i {operand} {self.img} j")
print("Addtion and Subtractiion of two Complex Numbers") 
real1=int(input("Enter first real number:"))
img1=int(input("Enter first imaginary number:"))
real2=int(input("Enter first real number:"))
img2=int(input("Enter first imaginary number:"))
operand=input("Enter the operator + or -:")
c1=Complex(real1,img1)
c2=Complex(real2,img2)
if operand=="+":
    c3=c1+c2
    c3.display()
elif operand=="-":
    c3=c1-c2
    c3.display()
else:
    print("Invalid Operator")
