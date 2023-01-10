from tkinter import *
from tkmacosx import *


class Calculator():
    currentVal = ''
    operandVal = ''
    operandSymbol = ''
    btnClearText = 'AC'

    def deleteDisplay(this):
        display.delete(1.0, END)

    def updateDisplay(this):
        this.deleteDisplay()
        display.insert(
            INSERT, f"{this.operandVal}{this.operandSymbol}\n{this.currentVal}")
        display.tag_configure("right", justify='right')
        display.tag_add("right", 1.0, "end")

    def num_click(this, val):
        if "." in this.currentVal and val == ".":
            return
        else:
            this.currentVal = str(this.currentVal) + str(val)
            this.deleteDisplay()
            this.updateDisplay()

    def negate_click(this):
        if "." in str(this.currentVal):
            this.currentVal = float(this.currentVal) * (-1)
        else:
            this.currentVal = int(this.currentVal) * (-1)
        this.deleteDisplay()
        this.updateDisplay()

    def percentage_click(this):
        if "." in str(this.currentVal):
            this.currentVal = float(this.currentVal) / 100
        else:
            this.currentVal = int(this.currentVal) / 100
        this.deleteDisplay()
        this.updateDisplay()

    def clear_click(this):
        this.deleteDisplay()
        this.currentVal = ''
        this.operandVal = ''

    def button_add(this):
        this.operandVal = this.currentVal
        this.operandSymbol = "+"
        this.currentVal = ''
        this.updateDisplay()

    def button_sub(this):
        this.operandVal = this.currentVal
        this.operandSymbol = "-"
        this.currentVal = ''
        this.updateDisplay()

    def button_mul(this):
        this.operandVal = this.currentVal
        this.operandSymbol = "x"
        this.currentVal = ''
        this.updateDisplay()

    def button_div(this):
        this.operandVal = this.currentVal
        this.operandSymbol = "÷"
        this.currentVal = ''
        this.updateDisplay()

    def button_equals(this):
        if "." in str(this.operandVal) or "." in str(this.currentVal):
            this.operandVal = float(this.operandVal)
            this.currentVal = float(this.currentVal)
        else:
            this.operandVal = int(this.operandVal)
            this.currentVal = int(this.currentVal)

        if this.operandSymbol == '+':
            this.currentVal = this.operandVal + this.currentVal
        elif this.operandSymbol == '-':
            this.currentVal = this.operandVal - this.currentVal
        elif this.operandSymbol == 'x':
            this.currentVal = this.operandVal * this.currentVal
        elif this.operandSymbol == '÷':
            this.currentVal = this.operandVal / this.currentVal

        this.operandVal = ''
        this.operandSymbol = ""
        this.updateDisplay()


calculator = Calculator()

# Window Container:
root = Tk()
root.title("Dan's Calculator App")

# Button Display Settings:
btn_width = 75
btn_height = 75
btn_bg_01 = 'darkorange'
btn_bg_02 = 'black'
btn_bg_03 = 'darkgrey'
btn_fg_01 = 'white'

# User Entry:
display = Text(root, width=25, height=2, bg="black",
               fg="white", font=("Arial", 20),)


button_decimal = Button(root, text=".", width=btn_width, height=btn_height,
                        command=lambda val=".": calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_0 = Button(root, text="0", width=btn_width*2, height=btn_height,
                  command=lambda val=0: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_1 = Button(root, text="1", width=btn_width, height=btn_height,
                  command=lambda val=1: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_2 = Button(root, text="2", width=btn_width, height=btn_height,
                  command=lambda val=2: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_3 = Button(root, text="3", width=btn_width, height=btn_height,
                  command=lambda val=3: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_4 = Button(root, text="4", width=btn_width, height=btn_height,
                  command=lambda val=4: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_5 = Button(root, text="5", width=btn_width, height=btn_height,
                  command=lambda val=5: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_6 = Button(root, text="6", width=btn_width, height=btn_height,
                  command=lambda val=6: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_7 = Button(root, text="7", width=btn_width, height=btn_height,
                  command=lambda val=7: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_8 = Button(root, text="8", width=btn_width, height=btn_height,
                  command=lambda val=8: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)
button_9 = Button(root, text="9", width=btn_width, height=btn_height,
                  command=lambda val=9: calculator.num_click(val), bg=btn_bg_03, fg=btn_fg_01)

button_clear = Button(root, text=calculator.btnClearText, width=btn_width, height=btn_height,
                      command=calculator.clear_click, bg=btn_bg_02, fg=btn_fg_01)
button_negate = Button(root, text="+/-", width=btn_width, height=btn_height,
                       command=calculator.negate_click, bg=btn_bg_02, fg=btn_fg_01)
button_percentage = Button(root, text="%", width=btn_width, height=btn_height,
                           command=calculator.percentage_click, bg=btn_bg_02, fg=btn_fg_01)

button_division = Button(root, text="÷", width=btn_width, height=btn_height,
                         command=calculator.button_div, bg=btn_bg_01, fg=btn_fg_01)
button_multiplication = Button(root, text="x", width=btn_width, height=btn_height,
                               command=calculator.button_mul, bg=btn_bg_01, fg=btn_fg_01)
button_subtraction = Button(root, text="-", width=btn_width, height=btn_height,
                            command=calculator.button_sub, bg=btn_bg_01, fg=btn_fg_01)
button_addition = Button(root, text="+", width=btn_width, height=btn_height,
                         command=calculator.button_add, bg=btn_bg_01, fg=btn_fg_01)
button_equals = Button(root, text="=", width=btn_width, height=btn_height,
                       command=calculator.button_equals, bg=btn_bg_01, fg=btn_fg_01)

# Display Items on Screen:
display.grid(row=0, column=0, columnspan=4)

# Arrange Calculator Number Buttons:
button_clear.grid(row=1, column=0)
button_negate.grid(row=1, column=1)
button_percentage.grid(row=1, column=2)
button_division.grid(row=1, column=3)


button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiplication.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subtraction.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_addition.grid(row=4, column=3)

button_0.grid(row=5, column=0, columnspan=2)
button_decimal.grid(row=5, column=2)
button_equals.grid(row=5, column=3)

root.mainloop()
