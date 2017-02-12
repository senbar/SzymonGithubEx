from tkinter import *
#from division import division
from translate import Translate

class App:
    Result=0



    def __init__(self,master):
        frame = Frame(master);
        frame.pack();
        master.minsize(width=200, height=100)
        master.maxsize(width=200, height=100)
        master.resizable(width=False, height=False)

        self.dialPolyOne=Entry(master);
        self.dialPolyTwo = Entry(master);

        self.button =Button(frame, text= "DIVIDE", command=self.divide);

        self.dialPolyOne.pack();
        self.dialPolyTwo.pack();
        self.button.pack();
    def divide(self):
        dicPolynomialOne=Translate(self.dialPolyOne.get());
        dicPolynomialTwo=Translate(self.dialPolyTwo.get());
       # Result= division(dicPolynomialOne,dicPolynomialTwo);

        self.displayResult();

    def displayResult(self):
        print(self.Result);



root=Tk();

app=App(root);

root.mainloop();
