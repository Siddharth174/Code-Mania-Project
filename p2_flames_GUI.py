from tkinter import *


def check_status():
    inp1 = inp1_entry.get()
    inp1 = inp1.lower()
    inp1.replace(" ", "")
    inp1_list = list(inp1)
    inp2 = inp2_entry.get()
    inp2 = inp2.lower()
    inp2.replace(" ", "")
    inp2_list = list(inp2)
    for x in inp1_list:
        if x in inp2_list:
            inp1_list.remove(x)
            inp2_list.remove(x)
    l_sum = len(inp1_list) + len(inp2_list)
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    while len(flames) > 1:
        split_index = (l_sum % len(flames) - 1)
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[: split_index]
            flames = right + left
        else:
            flames = flames[: len(flames) - 1]
    Status_field.insert(10, flames[0])


def clear_all():
    inp1_entry.delete(0, END)
    inp2_entry.delete(0, END)
    Status_field.delete(0, END)
    inp1_entry.focus_set()


root = Tk()
root.configure(background='pink')
root.geometry("350x125")
root.title("Flames Game")
label1 = Label(root, text="First Person: ", fg='black', bg='pink')
label2 = Label(root, text="Second Person: ", fg='black', bg='pink')
label3 = Label(root, text="Relationship Status: ", fg='black', bg='red')
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=4, column=0)
inp1_entry = Entry(root)
inp2_entry = Entry(root)
Status_field = Entry(root)
inp1_entry.grid(row=1, column=1, ipadx="50")
inp2_entry.grid(row=2, column=1, ipadx="50")
Status_field.grid(row=4, column=1, ipadx="50")
button1 = Button(root, text="Submit", bg="red", fg="black", command=check_status)
button2 = Button(root, text="Clear", bg="red", fg="black", command=clear_all)
button1.grid(row=3, column=1)
button2.grid(row=5, column=1)
root.mainloop()
