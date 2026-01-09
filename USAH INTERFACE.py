from tkinter import *
from tkinter import ttk

root = Tk()
root.title("perkeo ai")

root.geometry("800x500")
root.minsize(600,400)

container = Frame(root, bg="#f5f5f5")
container.pack(fill=BOTH, expand=True)

taskbar = Frame(container, bg="#eaeaea", height=50)
taskbar.pack(side=LEFT, fill=Y)

taskbar_label = Label(
    taskbar,
    text="Hey this is a test",
    bg="#eaeaea",
    font=("Arial", 14, "bold")
)
taskbar.pack(padx=15, pady=10, anchor="w")

debug_label = Label(
    taskbar,
    text="debug",
    bg="#0d92d3"

)
debug_label.pack(side=RIGHT, padx=10)

content_area = Frame(container, bg="#ffffff")
content_area.pack(side=LEFT, fill=BOTH, expand=True)

output_frame =Frame(content_area, bg="#ffffff")
output_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

output_text = Text(
    output_frame,
    wrap=WORD,
    state=DISABLED
)
output_text.pack(side=LEFT, fill=BOTH,  expand=True)

scrollbar = Scrollbar(output_frame, command=output_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)
output_text.config(yscrollcommand=scrollbar.set)

input_bar = Frame(content_area, bg="#dddddd")
input_bar.pack(fill=X,padx=10,pady=10)

user_input = Entry(
    input_bar,
    font=("Arial", 11)
)
user_input.pack(fill=X, padx=10, pady=8)
user_input.focus()

root.mainloop()