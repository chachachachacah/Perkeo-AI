from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import Hospital_backend  
selected_file = None

def upload_file():
    global selected_file

    file_path = filedialog.askopenfilename()
    if file_path:
        output_text.config(state=NORMAL)
        output_text.insert(END, f"File uploaded: {file_path}\n")
        selected_file = file_path

def submit_input():
    global selected_file #The more you learn

    user_prompt = user_input.get().strip()
    text = user_input.get()

    if not selected_file:
        output_text.config(state=NORMAL) #If you cant notice yes im using chatgpt shut up
        output_text.insert(END, "Please upload file first?\n")
        output_text.config(state=DISABLED)
        return
    
    output_text.config(state=NORMAL)
    output_text.insert(END, f"You: {text}\n")
    root.update()

    csv_file = Hospital_backend.converter_excel(selected_file)
    result = Hospital_backend.ai(csv_file, user_prompt)

    output_text.config(state=NORMAL)
    output_text.insert(END, "\nResult:\n")
    output_text.insert(END, result)
    output_text.config(state=DISABLED)

root = Tk()
root.title("Perkeo AI")

root.geometry("800x600")
root.minsize(600,400)

container = Frame(root)
container.pack(fill=BOTH, expand=True)

taskbar = Frame(container, height=50)
#taskbar.pack(side=LEFT, fill=Y)

taskbar_label = Label(
    taskbar,
    text="Hey this is a test",
    font=("Arial", 14, "bold")
)
taskbar.pack(padx=15, pady=10, anchor="w")

debug_label = Label(
    taskbar,
    text="Debug Mode",
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

input_bar = Frame(content_area)
input_bar.pack(fill=X,padx=10,pady=10)

user_input = Entry(
    input_bar,
    font=("Arial", 11)
)
user_input.pack(side=LEFT, fill=X, expand=True, padx=(10, 5), pady=8)
user_input.focus()


upload_button = Button(
    input_bar,
    text="Upload",
    command=upload_file
)
upload_button.pack(side=LEFT, padx=5)

submit_button = Button(
    input_bar,
    text="Submit",
    command=submit_input
)
submit_button.pack(side=LEFT, padx=5)

root.mainloop()
