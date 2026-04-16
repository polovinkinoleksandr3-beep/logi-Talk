from customtkinter import * 

set_appearance_mode("dark") 
set_default_color_theme("dark-blue")

window = CTk() 
window.title("Calculator") 
window.geometry("360x500")
window.resizable(False, False) 
entry = CTkEntry(window,
                 height = 60,
                  font = ("Arial", 25),
                   justify = "right")
entry.pack(pady = 20, padx = 20, fill = "x") 

frame = CTkFrame(window)
frame.pack(padx = 20, pady = 10, fill = "both") 

def add_0(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "+")  

def add_1(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "1")  

def add_2(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "2")  

def add_3(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "3")  

def add_4(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "4") 

def add_5(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "5") 


def add_plus(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "0")  

def add_minus(): 
    current = entry.get()
    entry.delete(0, "end") 
    entry.insert(0, current + "-") 



def clear_all():

    entry.delete(0, "end") 

def cal_resulte(): 
    try: 
        viraz = entry.get()
        result = eval(viraz)
        entry.delete(0, "end")
        entry.insert(0, str(result)) 
    except: 
        entry.delete(0, "end")
        entry.insert(0, "pomilka")

btn_C = CTkButton(frame, text = "C", width = 70, height=70, command=clear_all)
btn_C.grid(row = 0, column = 0, padx = 5, pady = 5) 

btn_plus = CTkButton(frame, text= "0", width=70, height=70, command=add_plus) 
btn_plus.grid(row = 0, column = 1, padx = 5, pady = 5) 

btn_0 = CTkButton(frame, text= "+", width=70, height=70, command=add_0) 
btn_0.grid(row = 0, column = 2, padx = 5, pady = 5) 

btn_eq = CTkButton(frame, text= "=", width=70, height=70, command = cal_resulte) 
btn_eq.grid(row = 0, column = 3, padx = 5, pady = 5) 

btn_1 = CTkButton(frame, text= "1", width=70, height=70, command=add_1) 
btn_1.grid(row = 1, column = 0, padx = 5, pady = 5) 

btn_2 = CTkButton(frame, text= "2", width=70, height=70, command=add_2) 
btn_2.grid(row = 1, column = 1, padx = 5, pady = 5) 

btn_3 = CTkButton(frame, text= "3", width=70, height=70, command=add_3) 
btn_3.grid(row = 1, column = 2, padx = 5, pady = 5)  

btn_4 = CTkButton(frame, text= "4", width=70, height=70, command=add_4) 
btn_4.grid(row = 1, column = 3, padx = 5, pady = 5) 

btn_5 = CTkButton(frame, text= "5", width=70, height=70, command=add_5) 
btn_5.grid(row = 2, column = 0, padx = 5, pady = 5) 

btn_minus = CTkButton(frame, text= "-", width=70, height=70, command=add_minus) #hi
btn_minus.grid(row = 2, column = 1, padx = 5, pady = 5) 






window.mainloop()

