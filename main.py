'''

import Tkinter'''
'''import tkMessageBox''''''

window = Tkinter.Tk()

ventana = Tkinter.Button(window, text="Enrique es puto")

ventana.pack()

window.mainloop()
'''
'''
top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()'''

from RoundRobin2 import * 

roundRobin = RoundRobin2()
roundRobin.calendario()
print roundRobin.printTabla()

