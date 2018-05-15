from tkinter import *
from tkinter import messagebox
from DegandRad import degrees
from DegandRad import radians
from Exp import e
from Fac import fac
from Trig import sin
from Trig import cos
from Trig import tan
from Trig import cot
from Trig import sec
from Trig import cosec
from Hyperbolic import sinh
from Hyperbolic import cosh
from Hyperbolic import tanh
from Hyperbolic import coth
from Hyperbolic import sech
from Hyperbolic import cosech
from InvTrig import invsin
from InvTrig import invcos
from InvTrig import invtan
from InvTrig import invcot
from InvTrig import invsec
from InvTrig import invcosec
from InvHyperbolic import invsinh
from InvHyperbolic import invcosh
from InvHyperbolic import invtanh
from InvHyperbolic import invcoth
from InvHyperbolic import invsech
from InvHyperbolic import invcosech
from LogAlog import ln
from LogAlog import log10
from LogAlog import lognth
from LogAlog import antilog
from QuadRoots import QuadRoots
from CandF import ceil
from CandF import floor
from Roots import sqrt
from Roots import cbrt
from Roots import nthrt
from Perc import perc
e=2.7182818284590452353602875 
π=3.14159265358979323846264338

ScientificCalculator=Tk()
ScientificCalculator.title("Scientific Calculator")
ScientificCalculator.resizable(0,0)

class calculator(Frame):
    def __init__(self, start):
        Frame.__init__(self, start)
        self.creatingeverything()

    def creatingeverything(self):
        #Developing Display
        self.screen=Entry(self, width=60, font=("Courier",22,"bold"),bg="gray1", fg="white",relief=FLAT, justify=RIGHT)
        self.screen.insert(0,"0")
        self.screen.grid(row=0, column=0, columnspan=10)


        #1st Row Buttons
        self.square=Button(self, font=("Courier",11,"bold"), text="x^2", relief=FLAT,bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("^2"))
        self.square.grid(row=1,column=0,sticky="NWNESWSE")

        self.cube=Button(self, font=("Courier",11,"bold"), text="x^3",relief=FLAT, bg='GRAY15',fg='snow',
                    command = lambda: self.displayattachment ("^3"))
        self.cube.grid(row=1,column=1,sticky="NWNESWSE")

        self.nthpower=Button(self, font=("Courier",11,"bold"), text="x^n",relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("^"))
        self.nthpower.grid(row=1,column=2,sticky="NWNESWSE")

        self.sqroot=Button(self, font=("Courier",11,"bold"), text="√x",relief=FLAT,bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("√("))
        self.sqroot.grid(row=1,column=3,sticky="NWNESWSE")

        self.cbroot=Button(self, font=("Courier",11,"bold"), text="3√x",relief=FLAT, bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("∛("))
        self.cbroot.grid(row=1,column=4,sticky="NWNESWSE")

        self.nthroot=Button(self, font=("Courier",11,"bold"), text="n√x",relief=FLAT, bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("nthrt("))
        self.nthroot.grid(row=1,column=5,sticky="NWNESWSE")

        self.clear=Button(self, font=("Courier",14,"bold"), text="AC",relief=FLAT,bg='gray60',fg='gray10',
                     command = lambda: self.autoclear())
        self.clear.grid(row=1,column=6,sticky="NWNESWSE")

        self.comma=Button(self, font=("Courier",14,"bold"), text=",",relief=FLAT, bg='gray60',fg='gray10',
                      command = lambda: self.displayattachment (","))
        self.comma.grid(row=1,column=7,sticky="NWNESWSE")

        self.perc=Button(self, font=("Courier",14,"bold"), text="%",relief=FLAT, bg='gray60',fg='gray10',
                    command = lambda: self.displayattachment ("perc("))
        self.perc.grid(row=1,column=8,sticky="NWNESWSE")

        self.divide=Button(self, font=("Courier",14,"bold"), text="÷",relief=FLAT, bg='darkorange',fg='snow',
                      command = lambda: self.displayattachment ("÷"))
        self.divide.grid(row=1,column=9,sticky="NWNESWSE")

        #2nd Row Buttons
        self.factorial=Button(self, font=("Courier",11,"bold"), text="factorial",relief=FLAT, bg='GRAY15',fg='snow',
                         command = lambda: self.displayattachment ("fac("))
        self.factorial.grid(row=2,column=0,sticky="NWNESWSE")

        self.degrees=Button(self, font=("Courier",11,"bold"), text="degrees",relief=FLAT, bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("degrees("))
        self.degrees.grid(row=2,column=1,sticky="NWNESWSE")

        self.radians=Button(self, font=("Courier",11,"bold"), text="radians",relief=FLAT, bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("radians("))
        self.radians.grid(row=2,column=2,sticky="NWNESWSE")

        self.rounding=Button(self, font=("Courier",11,"bold"), text="round",relief=FLAT, bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("round("))
        self.rounding.grid(row=2,column=3,sticky="NWNESWSE")

        self.ceiling=Button(self, font=("Courier",11,"bold"), text="ceiling",relief=FLAT,bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("ceil("))
        self.ceiling.grid(row=2,column=4,sticky="NWNESWSE")

        self.flooring=Button(self, font=("Courier",11,"bold"), text="flooring",relief=FLAT, bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("floor("))
        self.flooring.grid(row=2,column=5,sticky="NWNESWSE")

        self.quadroots=Button(self, font=("Courier",14,"bold"), text="quadratic roots",relief=FLAT,bg='GRAY20',fg='snow',
                         command = lambda: self.displayattachment ("QuadRoots("))
        self.quadroots.grid(row=2,column=6,columnspan=3,sticky="NWNESWSE")

        self.times=Button(self, font=("Courier",14,"bold"), text="×",relief=FLAT,bg='darkorange',fg='snow',
                     command = lambda: self.displayattachment ("×"))
        self.times.grid(row=2,column=9,sticky="NWNESWSE")

        #3rd Row Buttons
        self.exponential=Button(self, font=("Courier",11,"bold"), text="e^n",relief=FLAT, bg='GRAY15',fg='snow',
                           command = lambda: self.displayattachment ("e^"))
        self.exponential.grid(row=3,column=0,sticky="NWNESWSE")

        self.pi=Button(self, font=("Courier",11,"bold"), text="π",relief=FLAT,bg='GRAY15',fg='snow',
                  command = lambda: self.displayattachment ("π"))
        self.pi.grid(row=3,column=1,sticky="NWNESWSE")

        self.ln=Button(self, font=("Courier",11,"bold"), text="ln",relief=FLAT, bg='GRAY15',fg='snow',
                  command = lambda: self.displayattachment ("ln("))
        self.ln.grid(row=3,column=2,sticky="NWNESWSE")

        self.log10=Button(self, font=("Courier",11,"bold"), text="log10",relief=FLAT, bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("log10("))
        self.log10.grid(row=3,column=3,sticky="NWNESWSE")

        self.lognth=Button(self, font=("Courier",11,"bold"), text="lognth",relief=FLAT, bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("lognth("))
        self.lognth.grid(row=3,column=4,sticky="NWNESWSE")

        self.antilog=Button(self, font=("Courier",11,"bold"), text="antilog",relief=FLAT, bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("antilog("))
        self.antilog.grid(row=3,column=5,sticky="NWNESWSE")

        self.seven=Button(self, font=("Courier",14,"bold"), text="7",relief=FLAT, bg='GRAY20',fg='snow',
                    command = lambda: self.displayattachment ("7") )
        self.seven.grid(row=3,column=6,sticky="NWNESWSE")

        self.eight=Button(self, font=("Courier",14,"bold"), text="8",relief=FLAT, bg='GRAY20',fg='snow',
                     command = lambda: self.displayattachment ("8"))
        self.eight.grid(row=3,column=7,sticky="NWNESWSE")

        self.nine=Button(self, font=("Courier",14,"bold"), text="9",relief=FLAT,bg='GRAY20',fg='snow',
                    command = lambda: self.displayattachment ("9"))
        self.nine.grid(row=3,column=8,sticky="NWNESWSE")

        self.minus=Button(self, font=("Courier",14,"bold"), text="-", relief=FLAT,bg='darkorange',fg='snow',
                     command = lambda: self.displayattachment ("-"))
        self.minus.grid(row=3,column=9,sticky="NWNESWSE")

        #4th Row Buttons
        self.sin=Button(self, font=("Courier",11,"bold"), text="sin x", relief=FLAT,bg='GRAY15',fg='snow',
                   command = lambda: self.displayattachment ("sin("))
        self.sin.grid(row=4,column=0,sticky="NWNESWSE")

        self.cos=Button(self, font=("Courier",11,"bold"), text="cos x", relief=FLAT,bg='GRAY15',fg='snow',
                   command = lambda: self.displayattachment ("cos("))
        self.cos.grid(row=4,column=1,sticky="NWNESWSE")

        self.tan=Button(self, font=("Courier",11,"bold"), text="tan x", relief=FLAT,bg='GRAY15',fg='snow',
                   command = lambda: self.displayattachment ("tan("))
        self.tan.grid(row=4,column=2,sticky="NWNESWSE")

        self.cot=Button(self, font=("Courier",11,"bold"), text="cot x", relief=FLAT,bg='GRAY15',fg='snow',
                   command = lambda: self.displayattachment ("cot("))
        self.cot.grid(row=4,column=3,sticky="NWNESWSE")

        self.sec=Button(self, font=("Courier",11,"bold"), text="sec x",relief=FLAT, bg='GRAY15',fg='snow',
                   command = lambda: self.displayattachment ("sec("))
        self.sec.grid(row=4,column=4,sticky="NWNESWSE")

        self.cosec=Button(self, font=("Courier",11,"bold"), text="csc x", relief=FLAT,bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("cosec("))
        self.cosec.grid(row=4,column=5,sticky="NWNESWSE")

        self.four=Button(self, font=("Courier",14,"bold"), text="4", relief=FLAT,bg='GRAY20',fg='snow',
                    command = lambda: self.displayattachment ("4"))
        self.four.grid(row=4,column=6,sticky="NWNESWSE")

        self.five=Button(self, font=("Courier",14,"bold"), text="5", relief=FLAT,bg='GRAY20',fg='snow',
                    command = lambda: self.displayattachment ("5"))
        self.five.grid(row=4,column=7,sticky="NWNESWSE")

        self.six=Button(self, font=("Courier",14,"bold"), text="6", relief=FLAT,bg='GRAY20',fg='snow',
                   command = lambda: self.displayattachment ("7"))
        self.six.grid(row=4,column=8,sticky="NWNESWSE")

        self.plus=Button(self, font=("Courier",14,"bold"), text="+", relief=FLAT,bg='darkorange',fg='snow',
                    command = lambda: self.displayattachment ("+"))
        self.plus.grid(row=4,column=9,sticky="NWNESWSE")

        #5h Row Buttons
        self.invsin=Button(self, font=("Courier",11,"bold"), text="invsin x", relief=FLAT,bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("invsin("))
        self.invsin.grid(row=5,column=0,sticky="NWNESWSE")

        self.invcos=Button(self, font=("Courier",11,"bold"), text="invcos x",relief=FLAT, bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("invcos("))
        self.invcos.grid(row=5,column=1,sticky="NWNESWSE")

        self.invtan=Button(self, font=("Courier",11,"bold"), text="invtan x", relief=FLAT,bg='GRAY15',fg='snow',
                    command = lambda: self.displayattachment ("invtan(")  )
        self.invtan.grid(row=5,column=2,sticky="NWNESWSE")

        self.invcot=Button(self, font=("Courier",11,"bold"), text="invcot x", relief=FLAT,bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("invcot("))
        self.invcot.grid(row=5,column=3,sticky="NWNESWSE")

        self.invsec=Button(self, font=("Courier",11,"bold"), text="invsec x", relief=FLAT,bg='GRAY15',fg='snow',
                      command = lambda: self.displayattachment ("invsec("))
        self.invsec.grid(row=5,column=4,sticky="NWNESWSE")

        self.invcosec=Button(self, font=("Courier",11,"bold"), text="invcsc x", relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invcosec("))
        self.invcosec.grid(row=5,column=5,sticky="NWNESWSE")

        self.one=Button(self, font=("Courier",14,"bold"), text="1", relief=FLAT,bg='GRAY20',fg='snow',
                   command = lambda: self.displayattachment ("1"))
        self.one.grid(row=5,column=6,sticky="NWNESWSE")

        self.two=Button(self, font=("Courier",14,"bold"), text="2", relief=FLAT,bg='GRAY20',fg='snow',
                   command = lambda: self.displayattachment ("2"))
        self.two.grid(row=5,column=7,sticky="NWNESWSE")

        self.three=Button(self, font=("Courier",14,"bold"), text="3",relief=FLAT,bg='GRAY20',fg='snow',
                     command = lambda: self.displayattachment ("3"))
        self.three.grid(row=5,column=8,sticky="NWNESWSE")

        self.equals=Button(self, font=("Courier",14,"bold"), text="=", relief=FLAT,bg='darkorange',fg='snow',
                    command = lambda: self.getexpression()  )
        self.equals.grid(row=5,column=9,rowspan=3,sticky="NWNESWSE")

        #6th Row Buttons
        self.sinh=Button(self, font=("Courier",11,"bold"), text="sinh x", relief=FLAT,bg='GRAY15',fg='snow',
                    command = lambda: self.displayattachment ("sinh("))
        self.sinh.grid(row=6,column=0,sticky="NWNESWSE")

        self.cosh=Button(self, font=("Courier",11,"bold"), text="cosh x", relief=FLAT,bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("cosh("))
        self.cosh.grid(row=6,column=1,sticky="NWNESWSE")

        self.tanh=Button(self, font=("Courier",11,"bold"), text="tanh x", relief=FLAT,bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("tanh("))
        self.tanh.grid(row=6,column=2,sticky="NWNESWSE")

        self.coth=Button(self, font=("Courier",11,"bold"), text="coth x", relief=FLAT,bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("coth("))
        self.coth.grid(row=6,column=3,sticky="NWNESWSE")

        self.sech=Button(self, font=("Courier",11,"bold"), text="sech x", relief=FLAT,bg='GRAY15',fg='snow',
                     command = lambda: self.displayattachment ("sech("))
        self.sech.grid(row=6,column=4,sticky="NWNESWSE")

        self.cosech=Button(self, font=("Courier",11,"bold"), text="csch x", relief=FLAT,bg='GRAY15',fg='snow',
                       command = lambda: self.displayattachment ("cosech("))
        self.cosech.grid(row=6,column=5,sticky="NWNESWSE")

        self.dot=Button(self, font=("Courier",14,"bold"), text=".", relief=FLAT,bg='GRAY20',fg='snow',
                    command = lambda: self.displayattachment ("."))
        self.dot.grid(row=6,column=8,sticky="NWNESWSE")

        self.zero=Button(self, font=("Courier",14,"bold"), text="0", relief=FLAT,bg='GRAY20',fg='snow',
                     command = lambda: self.displayattachment ("0"))
        self.zero.grid(row=6,column=6,columnspan=2,sticky="NWNESWSE")

        #7th Row Buttons
        self.invsinh=Button(self, font=("Courier",11,"bold"), text="invsinh x", relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invsinh("))
        self.invsinh.grid(row=7,column=0,sticky="NWNESWSE")

        self.invcosh=Button(self, font=("Courier",11,"bold"), text="invcosh x",relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invcosh("))
        self.invcosh.grid(row=7,column=1,sticky="NWNESWSE")

        self.invtanh=Button(self, font=("Courier",11,"bold"), text="invtanh x",relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invtanh("))
        self.invtanh.grid(row=7,column=2,sticky="NWNESWSE")

        self.invcoth=Button(self, font=("Courier",11,"bold"), text="invcoth x", relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invcoth("))
        self.invcoth.grid(row=7,column=3,sticky="NWNESWSE")

        self.invsech=Button(self, font=("Courier",11,"bold"), text="invsech x",relief=FLAT,bg='GRAY15',fg='snow',
                        command = lambda: self.displayattachment ("invsech("))
        self.invsech.grid(row=7,column=4,sticky="NWNESWSE")

        self.invcosech=Button(self, font=("Courier",11,"bold"), text="invcsch x", relief=FLAT,bg='GRAY15',fg='snow',
                          command = lambda: self.displayattachment ("invcosech("))
        self.invcosech.grid(row=7,column=5,sticky="NWNESWSE")

        self.e=Button(self, font=("Courier",14,"bold"), text="e", relief=FLAT,bg='GRAY20',fg='snow',
                  command = lambda: self.displayattachment ("e"))
        self.e.grid(row=7,column=6,sticky="NWNESWSE")

        self.parenthesesopen=Button(self, font=("Courier",14,"bold"), text="(", relief=FLAT,bg='GRAY20',fg='snow',
                                command = lambda: self.displayattachment ("("))
        self.parenthesesopen.grid(row=7,column=7,sticky="NWNESWSE")

        self.parenthesesclose=Button(self, font=("Courier",14,"bold"), text=")", relief=FLAT,bg='GRAY20',fg='snow',
                                 command = lambda: self.displayattachment (")"))
        self.parenthesesclose.grid(row=7,column=8,sticky="NWNESWSE")


    def displayattachment (self, text):
        self.enteredtext = self.screen.get()
        self.textspan = len (self.enteredtext)
        if self.enteredtext=="0":
            self.restoretext(text)
        else:
            self.screen.insert(self.textspan, text)
    def restoretext(self,text):
        self.screen.delete(0, END)
        self.screen.insert(0, text)

    def getexpression(self):
        self.expression = self.screen.get()
        self.expression = self.expression.replace("%", "/100")
        self.expression = self.expression.replace("^2", "**2")
        self.expression = self.expression.replace("^3", "**3")
        self.expression = self.expression.replace("^", "**")
        self.expression = self.expression.replace("e^", "e(")
        self.expression = self.expression.replace("÷", "/")
        self.expression = self.expression.replace("×", "*")
        self.expression = self.expression.replace("√(", "sqrt(")
        self.expression = self.expression.replace("∛(", "cbrt(")
        
        try:
            self.answer = eval (self.expression)
            self.restoretext(self.answer)
        except:
            messagebox.showinfo("Error" , "Invalid Input")

    def autoclear(self):
        self.restoretext("0")


calculator(ScientificCalculator).grid()
ScientificCalculator.mainloop()    














