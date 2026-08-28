import lettergen
from tkinter import *
from tkinter import ttk, filedialog

is_fullscreen = False

letter_slot_1, letter_slot_2, letter_slot_3, letter_slot_4, letter_slot_5, letter_slot_6, letter_slot_7, letter_slot_8, letter_slot_9, letter_slot_10, letter_slot_11, letter_slot_12, letter_slot_13, letter_slot_14, letter_slot_15, letter_slot_16, letter_slot_17, letter_slot_18, letter_slot_19, letter_slot_20, letter_slot_21, letter_slot_22, letter_slot_23, letter_slot_24, letter_slot_25, letter_slot_26, letter_slot_27, letter_slot_28, letter_slot_29, letter_slot_30, letter_slot_31, letter_slot_32, letter_slot_33, letter_slot_34, letter_slot_35, letter_slot_36, symbol_slot_1, symbol_slot_2, symbol_slot_3, symbol_slot_4, symbol_slot_5, symbol_slot_6, symbol_slot_7, symbol_slot_8, symbol_slot_9, symbol_slot_10, symbol_slot_11, symbol_slot_12, symbol_slot_13, symbol_slot_14, symbol_slot_15, symbol_slot_16, symbol_slot_17, symbol_slot_18, symbol_slot_19, symbol_slot_20, symbol_slot_21, symbol_slot_22, symbol_slot_23, symbol_slot_24, symbol_slot_25, symbol_slot_26, symbol_slot_27, symbol_slot_28, symbol_slot_29, symbol_slot_30, symbol_slot_31, symbol_slot_32, symbol_slot_33, symbol_slot_34, symbol_slot_35, symbol_slot_36 = [lettergen.no_value() for _ in range(72)]

def chooseslots():
    global letter_slot_1, letter_slot_2, letter_slot_3, letter_slot_4, letter_slot_5, letter_slot_6, letter_slot_7, letter_slot_8, letter_slot_9, letter_slot_10, letter_slot_11, letter_slot_12, letter_slot_13, letter_slot_14, letter_slot_15, letter_slot_16, letter_slot_17, letter_slot_18, letter_slot_19, letter_slot_20, letter_slot_21, letter_slot_22, letter_slot_23, letter_slot_24, letter_slot_25, letter_slot_26, letter_slot_27, letter_slot_28, letter_slot_29, letter_slot_30, letter_slot_31, letter_slot_32, letter_slot_33, letter_slot_34, letter_slot_35, letter_slot_36, symbol_slot_1, symbol_slot_2, symbol_slot_3, symbol_slot_4, symbol_slot_5, symbol_slot_6, symbol_slot_7, symbol_slot_8, symbol_slot_9, symbol_slot_10, symbol_slot_11, symbol_slot_12, symbol_slot_13, symbol_slot_14, symbol_slot_15, symbol_slot_16, symbol_slot_17, symbol_slot_18, symbol_slot_19, symbol_slot_20, symbol_slot_21, symbol_slot_22, symbol_slot_23, symbol_slot_24, symbol_slot_25, symbol_slot_26, symbol_slot_27, symbol_slot_28, symbol_slot_29, symbol_slot_30, symbol_slot_31, symbol_slot_32, symbol_slot_33, symbol_slot_34, symbol_slot_35, symbol_slot_36
    letter_slot_1, letter_slot_2, letter_slot_3, letter_slot_4, letter_slot_5, letter_slot_6, letter_slot_7, letter_slot_8, letter_slot_9, letter_slot_10, letter_slot_11, letter_slot_12, letter_slot_13, letter_slot_14, letter_slot_15, letter_slot_16, letter_slot_17, letter_slot_18, letter_slot_19, letter_slot_20, letter_slot_21, letter_slot_22, letter_slot_23, letter_slot_24, letter_slot_25, letter_slot_26, letter_slot_27, letter_slot_28, letter_slot_29, letter_slot_30, letter_slot_31, letter_slot_32, letter_slot_33, letter_slot_34, letter_slot_35, letter_slot_36 = [lettergen.choose_letter() for _ in range(36)]
    symbol_slot_1, symbol_slot_2, symbol_slot_3, symbol_slot_4, symbol_slot_5, symbol_slot_6, symbol_slot_7, symbol_slot_8, symbol_slot_9, symbol_slot_10, symbol_slot_11, symbol_slot_12, symbol_slot_13, symbol_slot_14, symbol_slot_15, symbol_slot_16, symbol_slot_17, symbol_slot_18, symbol_slot_19, symbol_slot_20, symbol_slot_21, symbol_slot_22, symbol_slot_23, symbol_slot_24, symbol_slot_25, symbol_slot_26, symbol_slot_27, symbol_slot_28, symbol_slot_29, symbol_slot_30, symbol_slot_31, symbol_slot_32, symbol_slot_33, symbol_slot_34, symbol_slot_35, symbol_slot_36 = [lettergen.choose_symbol() for _ in range(36)]
    lettergen.reset_lists()

def updateslots():
    text_l_1 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_1 + ' ' + symbol_slot_2 + ' ' + symbol_slot_3), font=('Ink Free', 12))
    text_l_1.grid(row=0, column=1, sticky='nsew')

    text_l_2 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_4 + ' ' + symbol_slot_5 + ' ' + symbol_slot_6), font=('Ink Free', 12))
    text_l_2.grid(row=0, column=2, sticky='nsew')

    text_l_3 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_7 + ' ' + symbol_slot_8 + ' ' + symbol_slot_9), font=('Ink Free', 12))
    text_l_3.grid(row=0, column=3, sticky='nsew')

    text_l_4 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_10 + ' ' + symbol_slot_11 + ' ' + symbol_slot_12), font=('Ink Free', 12))
    text_l_4.grid(row=0, column=4, sticky='nsew')

    text_l_5 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_13 + ' ' + symbol_slot_14 + ' ' + symbol_slot_15), font=('Ink Free', 12))
    text_l_5.grid(row=0, column=5, sticky='nsew')

    text_l_6 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_16 + ' ' + symbol_slot_17 + ' ' + symbol_slot_18), font=('Ink Free', 12))
    text_l_6.grid(row=0, column=6, sticky='nsew')
    
    text_l_7 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_19 + ' ' + symbol_slot_20 + ' ' + symbol_slot_21), font=('Ink Free', 12))
    text_l_7.grid(row=1, column=0, sticky='nsew')

    text_l_8 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_1, font=('Ink Free', 12))
    text_l_8.grid(row=1, column=1, sticky='nsew')

    text_l_9 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_2, font=('Ink Free', 12))
    text_l_9.grid(row=1, column=2, sticky='nsew')

    text_l_10 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_3, font=('Ink Free', 12))
    text_l_10.grid(row=1, column=3, sticky='nsew')

    text_l_11 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_4, font=('Ink Free', 12))
    text_l_11.grid(row=1, column=4, sticky='nsew')

    text_l_12 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_5, font=('Ink Free', 12))
    text_l_12.grid(row=1, column=5, sticky='nsew')

    text_l_13 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_6, font=('Ink Free', 12))
    text_l_13.grid(row=1, column=6, sticky='nsew')

    text_l_14 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_22 + ' ' + symbol_slot_23 + ' ' + symbol_slot_24), font=('Ink Free', 12))
    text_l_14.grid(row=2, column=0, sticky='nsew')

    text_l_15 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_7, font=('Ink Free', 12))
    text_l_15.grid(row=2, column=1, sticky='nsew')

    text_l_16 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_8, font=('Ink Free', 12))
    text_l_16.grid(row=2, column=2, sticky='nsew')

    text_l_17 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_9, font=('Ink Free', 12))
    text_l_17.grid(row=2, column=3, sticky='nsew')

    text_l_18 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_10, font=('Ink Free', 12))
    text_l_18.grid(row=2, column=4, sticky='nsew')

    text_l_29 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_11, font=('Ink Free', 12))
    text_l_29.grid(row=2, column=5, sticky='nsew')

    text_l_20 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_12, font=('Ink Free', 12))
    text_l_20.grid(row=2, column=6, sticky='nsew')

    text_l_21 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_25 + ' ' + symbol_slot_26 + ' ' + symbol_slot_27), font=('Ink Free', 12))
    text_l_21.grid(row=3, column=0, sticky='nsew')

    text_l_22 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_13, font=('Ink Free', 12))
    text_l_22.grid(row=3, column=1, sticky='nsew')

    text_l_23 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_14, font=('Ink Free', 12))
    text_l_23.grid(row=3, column=2, sticky='nsew')

    text_l_24 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_15, font=('Ink Free', 12))
    text_l_24.grid(row=3, column=3, sticky='nsew')

    text_l_25 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_16, font=('Ink Free', 12))
    text_l_25.grid(row=3, column=4, sticky='nsew')

    text_l_26 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_17, font=('Ink Free', 12))
    text_l_26.grid(row=3, column=5, sticky='nsew')

    text_l_27 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_18, font=('Ink Free', 12))
    text_l_27.grid(row=3, column=6, sticky='nsew')

    text_l_28 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_28 + ' ' + symbol_slot_29 + ' ' + symbol_slot_30), font=('Ink Free', 12))
    text_l_28.grid(row=4, column=0, sticky='nsew')

    text_l_39 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_19, font=('Ink Free', 12))
    text_l_39.grid(row=4, column=1, sticky='nsew')

    text_l_30 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_20, font=('Ink Free', 12))
    text_l_30.grid(row=4, column=2, sticky='nsew')

    text_l_31 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_21, font=('Ink Free', 12))
    text_l_31.grid(row=4, column=3, sticky='nsew')

    text_l_32 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_22, font=('Ink Free', 12))
    text_l_32.grid(row=4, column=4, sticky='nsew')

    text_l_33 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_23, font=('Ink Free', 12))
    text_l_33.grid(row=4, column=5, sticky='nsew')

    text_l_34 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_24, font=('Ink Free', 12))
    text_l_34.grid(row=4, column=6, sticky='nsew')

    text_l_35 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_31 + ' ' + symbol_slot_32 + ' ' + symbol_slot_33), font=('Ink Free', 12))
    text_l_35.grid(row=5, column=0, sticky='nsew')

    text_l_36 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_25, font=('Ink Free', 12))
    text_l_36.grid(row=5, column=1, sticky='nsew')

    text_l_37 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_26, font=('Ink Free', 12))
    text_l_37.grid(row=5, column=2, sticky='nsew')

    text_l_38 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_27, font=('Ink Free', 12))
    text_l_38.grid(row=5, column=3, sticky='nsew')

    text_l_49 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_28, font=('Ink Free', 12))
    text_l_49.grid(row=5, column=4, sticky='nsew')

    text_l_40 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_29, font=('Ink Free', 12))
    text_l_40.grid(row=5, column=5, sticky='nsew')

    text_l_41 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_30, font=('Ink Free', 12))
    text_l_41.grid(row=5, column=6, sticky='nsew')

    text_l_42 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = (symbol_slot_34 + ' ' + symbol_slot_35 + ' ' + symbol_slot_36), font=('Ink Free', 12))
    text_l_42.grid(row=6, column=0, sticky='nsew')

    text_l_43 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_31, font=('Ink Free', 12))
    text_l_43.grid(row=6, column=1, sticky='nsew')

    text_l_44 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_32, font=('Ink Free', 12))
    text_l_44.grid(row=6, column=2, sticky='nsew')

    text_l_45 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_33, font=('Ink Free', 12))
    text_l_45.grid(row=6, column=3, sticky='nsew')

    text_l_46 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_34, font=('Ink Free', 12))
    text_l_46.grid(row=6, column=4, sticky='nsew')

    text_l_47 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_35, font=('Ink Free', 12))
    text_l_47.grid(row=6, column=5, sticky='nsew')

    text_l_48 = Label(cypher_frame,relief= 'solid' ,bd = 1,  bg='#f7d3a3', fg='#7b2a19', text = letter_slot_36, font=('Ink Free', 12))
    text_l_48.grid(row=6, column=6, sticky='nsew')

def updategrid():
    chooseslots()
    updateslots()

def import_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        tab2_text.delete("1.0", END)
        tab2_text.insert(END, content)

def export_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        content = tab2_text.get("1.0", "end-1c")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

window = Tk()
window.title('Foxy Encryptor')

style = ttk.Style()
style.theme_use('clam')

style.configure('TNotebook.Tab', 
                background='#f7d3a3', 
                foreground='#7b2a19', 
                font=('Ink Free', 11, 'bold'),
                padding=[10, 4])

style.map('TNotebook.Tab', 
          background=[('selected', '#7b2a19')], 
          foreground=[('selected', '#f7d3a3')])

style.configure('TNotebook', background='#f7d3a3')

notebook = ttk.Notebook(window)

# Tab 1
tab1 = Frame(notebook)
notebook.add(tab1, text="Create Cypher")

tab1.columnconfigure(0, weight=1)
tab1.rowconfigure(0, weight=1)
tab1.columnconfigure(1, weight=1)
tab1.rowconfigure(1, weight=1)

cypher_frame = Frame(tab1, bg='#f7d3a3')
cypher_frame.grid(row=0, column=0, sticky='nsew', columnspan=2, rowspan=2)

for i in range(7):
    cypher_frame.columnconfigure(i, weight=1)
    cypher_frame.rowconfigure(i, weight=1)

updategrid()

run_button = Button(cypher_frame, text='Regenerate', command=updategrid, font=('Ink Free', 12), bg='#f7d3a3', fg='#7b2a19', activebackground='#7b2a19', activeforeground='#f7d3a3')
run_button.grid(column=0, row=0, sticky='nsew')

# Tab 2
tab2 = Frame(notebook, bg='#f7d3a3')
notebook.add(tab2, text="Import / Export")

button_frame = Frame(tab2, bg='#f7d3a3')
button_frame.pack(pady=10)

import_button = Button(
    button_frame, 
    text="Import File", 
    command=import_file, 
    font=('Ink Free', 12), 
    bg='#f7d3a3', 
    fg='#7b2a19', 
    activebackground='#7b2a19', 
    activeforeground='#f7d3a3'
)
import_button.pack(side=LEFT, padx=5)

export_button = Button(
    button_frame, 
    text="Export File", 
    command=export_file, 
    font=('Ink Free', 12), 
    bg='#f7d3a3', 
    fg='#7b2a19', 
    activebackground='#7b2a19', 
    activeforeground='#f7d3a3'
)
export_button.pack(side=LEFT, padx=5)

tab2_text = Text(tab2, wrap="word", bg='#f7d3a3', fg='#7b2a19', font=('Ink Free', 12), bd=1, relief='solid')
tab2_text.pack(fill=BOTH, expand=True, padx=15, pady=(0, 10))

notebook.pack(expand=True, fill=BOTH)

def toggle_fullscreen(event=None):
   global is_fullscreen
   is_fullscreen = not is_fullscreen
   window.attributes("-fullscreen", is_fullscreen)

toggle_fullscreen()
window.bind("<F11>", toggle_fullscreen)

window.mainloop()
