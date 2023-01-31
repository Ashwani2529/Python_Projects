from tkinter import Tk,Entry,Button,StringVar
class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('315x440+0+0')
        master.config(bg='gray')
        master.resizable(False,False)
        self.equation=StringVar()
        self.entry_value=' '  
        Entry(width=17,bg='#C1CDCD',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=5)
        Button(width=9,height=4,text='(',relief='flat',bg='azure1',command=lambda:self.show('(')).place(x=0 ,y=60)
        Button(width=9,height=4,text=')',relief='flat',bg='antiquewhite2',command=lambda:self.show(')')).place(x= 80,y=60)
        Button(width=9,height=4,text='%',relief='flat',bg='blanchedalmond',command=lambda:self.show('%')).place(x=160 ,y=60)
        Button(width=9,height=4,text='1',relief='flat',bg='white',command=lambda:self.show(1)).place(x= 0,y=135)
        Button(width=9,height=4,text='2',relief='flat',bg='white',command=lambda:self.show(2)).place(x=80 ,y=135)
        Button(width=9,height=4,text='3',relief='flat',bg='white',command=lambda:self.show(3)).place(x=160 ,y=135)
        Button(width=9,height=4,text='4',relief='flat',bg='white',command=lambda:self.show(4)).place(x=0 ,y=210)
        Button(width=9,height=4,text='5',relief='flat',bg='white',command=lambda:self.show(5)).place(x=80 ,y=210)
        Button(width=9,height=4,text='6',relief='flat',bg='white',command=lambda:self.show(6)).place(x= 160,y=210)
        Button(width=9,height=4,text='7',relief='flat',bg='white',command=lambda:self.show(7)).place(x=0 ,y=285)
        Button(width=9,height=4,text='8',relief='flat',bg='white',command=lambda:self.show(8)).place(x=160 ,y=285)
        Button(width=9,height=4,text='9',relief='flat',bg='white',command=lambda:self.show(9)).place(x=80 ,y=285)
        Button(width=9,height=4,text='0',relief='flat',bg='white',command=lambda:self.show(0)).place(x=80 ,y=360)
        Button(width=9,height=4,text='.',relief='flat',bg='burlywood1',command=lambda:self.show('.')).place(x=160 ,y=360)
        Button(width=9,height=4,text='+',relief='flat',bg='azure3',command=lambda:self.show('+')).place(x=240,y=285)
        Button(width=9,height=4,text='-',relief='flat',bg='bisque4',command=lambda:self.show('-')).place(x=240 ,y=210)
        Button(width=9,height=4,text='/',relief='flat',bg='azure2',command=lambda:self.show('/')).place(x=240 ,y=60)
        Button(width=9,height=4,text='x',relief='flat',bg='aquamarine1',command=lambda:self.show('*')).place(x=240 ,y=135)
        Button(width=9,height=4,text='=',relief='flat',bg='azure2',command=self.solve).place(x=240 ,y=360)
        Button(width=9,height=4,text='C',relief='flat',bg='lightblue',command=self.clear).place(x=0 ,y=360)
          
    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)
    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)    
root=Tk()
calculator=Calculator(root)
root.mainloop()