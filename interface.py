
import tkinter as tk
import rational as rat
from tkinter import messagebox
import logger as log

def interface():
    def delete():
        ent_enter.delete(0, tk.END)
    def delete_one():
        str = ent_enter.get()
        ent_enter.delete(len(str) - 1)
    def equally():
        value = ent_enter.get()
        str1 = "-+0123456789.*/)(" 
        if ent_enter.get()[0] not in str1:
            ent_enter.delete(0, tk.END)
            messagebox.showerror("Ошибка!", "Вводить можно только числа!!!")
        result = rat.rational(value)
        ent_enter.delete(0, tk.END)
        ent_enter.insert(0, f'{result}')
        log.result_log(value, result)
    
    def calc(key):
        value = ent_enter.get()  
        ent_enter.delete(0, tk.END)
        ent_enter.insert(0, f'{value}{key}')
    calculate = tk.Tk()
    calculate.title('Калькулятор')
    calculate.rowconfigure(0, minsize=5, weight=1)
    calculate.columnconfigure(0, minsize=5 , weight=1)
    frm_text = tk.Frame(
        master=calculate,
        relief=tk.FLAT,
        borderwidth=3
    )
    frm_text.pack()
    lbl_enter = tk.Label(
        master = frm_text,
        text = 'Введите выражение',
        bg='white',
        width=40, height=2)
    lbl_enter.pack()
    ent_enter = tk.Entry(master = calculate, width=40)
    ent_enter.pack()
    frm_button = tk.Frame(master = calculate, 
        relief = tk.SUNKEN, 
        borderwidth=3
    )
    frm_button.pack()
    btn_delete = tk.Button(master = frm_button, text = 'C', width=5, height=2, command= delete)
    btn_delete.grid(row=0, column=0)
    btn_delete_one = tk.Button(master = frm_button, text = '<=', width=5, height=2, command= delete_one)
    btn_delete_one.grid(row=0, column=1)
    btn_equelly = tk.Button(master = frm_button, text = 'Вычислить', width=12, height=2, command= equally)
    btn_equelly.grid(row=0, column=2, columnspan=2)
    btn_list = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '+',
        '', '0', '.', '-',
        '(', ')'
    ]
    r = 1 
    c = 0
    for i in btn_list:
        cmd = lambda x = i: calc(x)
        tk.Button(master = frm_button, text = i, command=cmd, width=5, height=2).grid(row = r, column=c)
        c += 1
        if c > 3:
            c = 0
            r +=1
    calculate.mainloop()


