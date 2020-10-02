from tkinter import*

def btnclick(numbers):   #define the button(btn)click function
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():   # define the clear function
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():     #define the Equal to function
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operators=""

cal = Tk()
cal.title("Calculator")       # name the app, i choose a "Calculator" because it's random
cal.geometry("360x588")
cal.maxsize(360,588)
cal.minsize(360,588)
operator = ""
text_Input = StringVar()



txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                   bg="powder blue", justify='right').grid(columnspan=4)

btnclear=Button(cal,padx=16,pady=16,bd=8, fg="white",font=('arial', 19,'bold'),
            text="C",bg="crimson",command=btnClearDisplay).grid(row=1,column="0")

BtnM=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 17,'bold'),
            text="M",bg="#7FFFD4",).grid(row=1,column="1",ipady=3)

Btnbraket1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 19,'bold'),
            text="(",bg="#7FFFD4",command=lambda:btnclick("(")).grid(row=1,column="2",ipadx=5)

Btnbracket2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 19,'bold'),
            text=")",bg="#7FFFD4",command=lambda:btnclick(")")).grid(row=1,column="3",ipadx=1)
#=======================================================================================================================

btn7=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="7",bg="powder blue",command=lambda:btnclick(7)).grid(row=2,column="0")

btn8=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="8", bg="powder blue",command=lambda:btnclick(8)).grid(row=2,column="1")

btn9=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="9", bg="powder blue",command=lambda:btnclick(9)).grid(row=2,column="2")

Division=Button(cal,padx=16,pady=16,bd=8, fg="yellow",font=('arial', 20,'bold'),
            text="/",bg="#2F4F4F",command=lambda:btnclick("/")).grid(row=2,column="3")
#===========================================================================================================================

btn6=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="6",bg="powder blue",command=lambda:btnclick(6)).grid(row=3,column="0")

btn5=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="5",bg="powder blue",command=lambda:btnclick(5)).grid(row=3,column="1")

btn4=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="4",bg="powder blue",command=lambda:btnclick(4)).grid(row=3,column="2")

subtraction=Button(cal,padx=16,pady=16,bd=8, fg="yellow",font=('arial', 20,'bold'),
            text="-",bg="#2F4F4F",command=lambda:btnclick("-")).grid(row=3,column="3")
#===============================================================================================================================

btn3=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="3",bg="powder blue",command=lambda:btnclick(3)).grid(row=4,column="0")

btn2=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="2",bg="powder blue",command=lambda:btnclick(2)).grid(row=4,column="1")

btn1=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="1",bg="powder blue",command=lambda:btnclick(1)).grid(row=4,column="2")

Multiplication=Button(cal,padx=16,pady=16,bd=8, fg="yellow",font=('arial', 17,'bold'),
            text="x",bg="#2F4F4F",command=lambda:btnclick("*")).grid(row=4,column="3",ipady=4)
#==================================================================================================================================

Btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="0",bg="powder blue",command=lambda:btnclick(0)).grid(row=5,column="0")

Dot=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text=".",bg="#7FFFD4",command=lambda:btnclick(".")).grid(row=5,column="1",ipadx=3)

Equal=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial', 20,'bold'),
            text="=",bg="#9ACD32",command=btnEqualsInput).grid(row=5,column="2")

Addition=Button(cal,padx=16,pady=16,bd=8, fg="yellow",font=('arial', 16,'bold'),
            text="+",bg="#2F4F4F",command=lambda:btnclick("+")).grid(row=5,column="3",ipady=6)



cal.mainloop()
