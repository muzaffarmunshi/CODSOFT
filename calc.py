from tkinter import *

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def clear():
    num1_entry.delete(0,END)
    num2_entry.delete(0,END)
    output_entry.delete(0,END)
def calculate():
    num1=float(num1_entry.get())
    num2=float(num2_entry.get())
    operation=operator_entry.get()
    
    if operation=='+':
        result=add(num1,num2)
    elif operation=='-':
        result=subtract(num1,num2)
    elif operation=='*':
        result=multiply(num1,num2)
    elif operation=='/':
        result=divide(num1,num2)
        
    output_entry.insert(0,result)

root=Tk()
root.title('Simple Calculator')

num1_label=Label(root,text='First Number:')
num2_label=Label(root,text='Second Number:')
operator_label=Label(root,text='Operation:')
output_label=Label(root,text='Result:')

num1_entry=Entry(root)
num2_entry=Entry(root)
operator_entry=Entry(root)
output_entry=Entry(root)

add_button=Button(root,text='+',command=lambda:calculate())
subtract_button=Button(root,text='-',command=lambda:calculate())
multiply_button=Button(root,text='*',command=lambda:calculate())
divide_button=Button(root,text='/',command=lambda:calculate())
clear_button=Button(root,text='Clear',command=clear)
calculate_button=Button(root,text='Calculate',command=calculate)
num1_label.grid(row=0,column=0)
num1_entry.grid(row=0,column=1)
num2_label.grid(row=1,column=0)
num2_entry.grid(row=1,column=1)
operator_label.grid(row=2,column=0)
operator_entry.grid(row=2,column=1)
output_label.grid(row=3,column=0)
output_entry.grid(row=3,column=1)
add_button.grid(row=4,column=0)
subtract_button.grid(row=4,column=1)
multiply_button.grid(row=5,column=0)
divide_button.grid(row=5,column=1)
clear_button.grid(row=6,column=0)
calculate_button.grid(row=6,column=1)

# Running the main event loop
root.mainloop()
