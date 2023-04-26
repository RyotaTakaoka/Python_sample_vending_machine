import tkinter as tk
import tkinter.messagebox as tkmsg


daikin = 0
otsuri = 0
select_number = 0

def juice_click():
    global select_number

    select_number = 1
    calculation_sec(select_number)

def tea_click():
    global select_number
    
    select_number = 2
    calculation_sec(select_number)

def water_click():
    global select_number

    select_number = 3
    calculation_sec(select_number)

def otsuri_click():
    global otsuri

    tkmsg.showinfo("精算", "おつりは{}円です".format(otsuri))
    ret = tkmsg.askyesno("終了", "プログラムを終了します")
    rireki1.insert(tk.END, ">>おつりを排出しました。残金0円\n")
    otsuri = 0
    if ret == True:
        root.destroy()

def calculation_sec(number):
    global daikin, otsuri
    
    daikin += otsuri
    otsuri = 0
    daikin += int(entry1.get())
    rireki1.insert(tk.END, ">>合計{}円\n".format(daikin))
    if number == 1:
        if daikin >= 100:
            otsuri = daikin - 100
            rireki1.insert(tk.END, ">>ジュースを排出します\n")
            rireki1.insert(tk.END, ">>残金{}円\n".format(otsuri))
            rireki1.see("end")
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, 0)
            daikin = 0
        else:
            rireki1.insert(tk.END, ">>投入金額が不足しています\n")
            rireki1.see("end")
            
    elif number == 2:
        if daikin >= 80:
            otsuri = daikin - 80
            rireki1.insert(tk.END, ">>お茶を排出します\n")
            rireki1.insert(tk.END, ">>残金{}円\n".format(otsuri))
            rireki1.see("end")
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, 0)
            daikin = 0
        else:
            rireki1.insert(tk.END, ">>投入金額が不足しています\n")
            rireki1.see("end")

    elif number == 3:
        if daikin >= 50:
            otsuri = daikin - 50
            rireki1.insert(tk.END, ">>水を排出します\n")
            rireki1.insert(tk.END, ">>残金{}円\n".format(otsuri))
            rireki1.see("end")
            entry1.delete(0, tk.END)
            entry1.insert(tk.END, 0)
            daikin = 0
        else:
            rireki1.insert(tk.END, ">>投入金額が不足しています\n")
            rireki1.see("end")

    
root = tk.Tk()
root.geometry("520x700")
root.title("自動販売機プログラム")

canvas = tk.Canvas(root, width=520, height=700, bg="white")
canvas.place(x=0, y=0)

button1 = tk.Button(root, text="ジュース", font=("Helvetica", 20), command=juice_click)
button1.place(x=50, y=80)

button2 = tk.Button(root, text="お茶", font=("Helvetica", 20), command=tea_click)
button2.place(x=250, y=80)

button3 = tk.Button(root, text="水", font=("Helvetica", 20), command=water_click)
button3.place(x=400, y=80)

button4 = tk.Button(root, text="おつり", font=("Helvetica", 32), command=otsuri_click)
button4.place(x=50, y=270)

label1 = tk.Label(root, text="１００円", font=("Helvetica", 20))
label1.place(x=60, y=140)

label2 = tk.Label(root, text="８０円", font=("Helvetica", 20))
label2.place(x=245, y=140)

label3 = tk.Label(root, text="５０円", font=("Helvetica", 20))
label3.place(x=380, y=140)

label4 = tk.Label(root, text="金額入力", font=("Helvetica", 28))
label4.place(x=300, y=240)

entry1 = tk.Entry(width=4, font=("Helvetica", 48), bg="gray", fg="white")
entry1.place(x=300, y=290)

rireki1 = tk.Text(root, font=("Helvetica", 14), bg="gray", fg="white")
rireki1.place(x=30, y=430, width=460, height=240)

entry1.insert(tk.END, 0)
            
root.mainloop()

        
