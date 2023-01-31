import tkinter as tk
import time
root=tk.Tk()
root.geometry('400×250')
root.title('Digital Clock')
root.tk_setPalette('black')
def cleard():
	mon.config(fg='#c3c3c3')
	tue.config(fg='#c3c3c3')
	wed.config(fg='#c3c3c3')
	thur.config(fg='#c3c3c3')
	fri.config(fg='#c3c3c3')
	sat.config(fg='#c3c3c3')
	sun.config(fg='#c3c3c3')
def upt():
	hours=time.strftime('%H')
	minutes=time.strftime('%M')
	seconds=time.strftime('%S')
	timelb.config(text=f'{hours}:{minutes}:  {seconds}')
	root.after(1000,upt)
	date=time.strftime('%d')
	month=time.strftime('%m')
	year=time.strftime('%Y') 
	amtpm=time.strftime('%p')
	datel.config(text=f'{date}-{month}-{year}')
	ampm.config(text=amtpm)
	day=time.strftime('%a')
	cleard()
	days[day].config(fg='white',font=('Bold',12))
	root.after(1000,upt)

clockframe=tk.Frame(root)
daysframe=tk.Frame(clockframe)
mon=tk.Label(daysframe,text='MON')
mon.pack(side=tk.LEFT,padx=10)
tue=tk.Label(daysframe,text='TUE')
tue.pack(side=tk.LEFT,padx=10)
wed=tk.Label(daysframe,text='WED')
wed.pack(side=tk.LEFT,padx=10)
thur=tk.Label(daysframe,text='THU')
thur.pack(side=tk.LEFT,padx=10)
fri=tk.Label(daysframe,text='FRI')
fri.pack(side=tk.LEFT,padx=10)
sat=tk.Label(daysframe,text='SAT')
sat.pack(side=tk.LEFT,padx=10)
sun=tk.Label(daysframe,text='SUN')
sun.pack(side=tk.LEFT,padx=10)
daysframe.pack(pady=10)
days={'Mon': mon,
      'Tue':tue,
      'Wed':wed,
      'Thur':thur,
      'Fri':fri,
      'Sat':sat,
      'Sun':sun}


timelb=tk.Label(clockframe,font=('DS-Digital',50))
timelb.pack(pady=10)
clockframe.pack()
dateframe=tk.Label(clockframe)
datel=tk.Label(dateframe,font=('DS-Digital',15))
datel.pack(side=tk.LEFT)
ampm=tk.Label(dateframe,font=('DS-Digital',15))
ampm.pack(side=tk.RIGHT)
dateframe.pack(pady=10,fill=tk.X)
upt()
root.mainloop()