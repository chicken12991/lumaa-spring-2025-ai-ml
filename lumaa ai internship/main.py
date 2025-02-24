import tkinter as tk
import compare as cm
#This is the front end ofmy program, it is very bear bones and uses tkinter elements
def button1():
    print(text_box.get("1.0", "end"))
    query = text_box.get("1.0", "end")
    if len(query) < 2:
        text_box2.config(state = "normal")
        text_box2.delete("1.0", "end")
        text_box2.insert(tk.INSERT,"please inset a longer query to the text box above")
        text_box2.config(state = "disabled")
    else:
        try:
            result = cm.main(query)
    
            text_box2.config(state = "normal")
            text_box2.delete("1.0", "end")
            text_box2.insert(tk.INSERT,result)
            text_box2.config(state = "disabled")
        except:
            text_box2.config(state = "normal")
            text_box2.delete("1.0", "end")
            text_box2.insert(tk.INSERT,"try a different query")
            text_box2.config(state = "disabled")


    

root = tk.Tk()
result = ""
root.geometry("1200x800")
label = tk.Label(root, text="Welcome to my movie reccomender! Try  a bunch of searches :)")
button = tk.Button(root, text="Search", command=button1)
text_box = tk.Text(root, height=1, width=50)
text_box2 = tk.Text(root, height=35, width=120)
text_box2.config(state = "disabled")




label.pack()
button.pack()
text_box.pack()
text_box2.pack()
root.mainloop()
