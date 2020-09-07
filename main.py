# codekey is the encrypting module coded by me.
import codekey
# decode is the decrypting module also coded by me.
import decode
# tkinter is the module that enables programmers to make GUIs in python.
from tkinter import *
# defining the action-on-submit function for encryption.
def code_submit():
    code_store = text_box.get(1.0, "end")
    window_1.destroy()
    # creating a window to display the code.
    code_submit_window = Toplevel(window)
    code_submit_window.title("PyDcoder_Adjustable-GUI by __ilprofessore ")
    code_submit_window.geometry("200x200")
    code_submit_window.iconbitmap("icon/image.ico")
    code_submit_window.resizable(height=False, width=False)
    # the following line is solely responsible for using the 'codekey' module to mode the text.
    code_store = codekey.code_module(code_store)
    # creating the necessary labels and buttons.
    Label(code_submit_window, text="").pack()
    _my_label = Label(code_submit_window, text="Encryption", padx=5, pady=5, font=("arial", "12"), bg="grey", fg="blue")
    _my_label.pack(padx=5, pady=5)
    Label(code_submit_window, text="ctrl+a", fg="red").pack()
    Label(code_submit_window, text="ctrl+c", fg="red").pack()
    Label(code_submit_window, text="").pack()
    final_display = Entry(code_submit_window, width=25)
    final_display.pack()
    b1 = Button(code_submit_window, text="exit", fg="red", command=code_submit_window.destroy, padx=10, pady=5)
    b1.pack(padx=10, pady=10)
    final_display.insert(0, code_store)

    code_submit_window.mainloop()

# defining the action-on-submit function for decryption.
def decode_submit():
    decode_store = text_box_.get(1.0, "end")
    window_2.destroy()
    # creating a window to display the decode.
    decode_submit_window = Toplevel(window)
    decode_submit_window.title("PyDcoder_Adjustable-GUI by __ilprofessore ")
    decode_submit_window.geometry("200x200")
    decode_submit_window.iconbitmap("icon/image.ico")
    decode_submit_window.resizable(height=False, width=False)
    # the below line is solely responsible for using the 'decode' module to decode the encryption.
    decode_store = decode.decode_module(decode_store)
    # creating necessary labels and buttons.
    Label(decode_submit_window, text="").pack()
    __my_label = Label(decode_submit_window, text="Decryption", padx=5, pady=5, font=("arial", "12"), bg="grey", fg="blue")
    __my_label.pack(padx=5, pady=5)
    Label(decode_submit_window, text="ctrl+a", fg="red").pack()
    Label(decode_submit_window, text="ctrl+c", fg="red").pack()
    Label(decode_submit_window, text="").pack()
    final__display = Entry(decode_submit_window, width=25)
    final__display.pack()
    b1_ = Button(decode_submit_window, text="exit", fg="red", command=decode_submit_window.destroy, padx=10, pady=5)
    b1_.pack(padx=10, pady=10)
    final__display.insert(0, decode_store)

    decode_submit_window.mainloop()
# defining the decryption window function.
def decoder():
    global window_2
    global text_box_
    window_2 = Toplevel(window)
    window_2.title("PyDcoder_Adjustable-GUI by __ilprofessore ")
    window_2.geometry("400x400")
    window_2.iconbitmap("icon/image.ico")
    window_2.resizable(height=False, width=False)
    # making all the necessary stuff for the decryption window.
    header_ = "Welcome to PyDcoder_Adjustable-GUI Decryptor"
    line_1_ = "paste the encryption created by coder" \
              "\nany mistake in the encryption text" \
              "\nwill render the decode useless" \
              "\ncareful with this step."
    line_1_ = line_1_.upper()
    my_label_ = Label(window_2, text=header_, padx=5, pady=5, font=("arial", "12"), bg="grey", fg="blue")
    my_label_.pack(padx=5, pady=5)
    Label(window_2, text=line_1_, padx=5, pady=5, font=("arial", "10"), fg="red").pack(padx=5, pady=5)
    # i know, it's a shitty scroll bar; i just copied and pasted it.
    scrollbar = Scrollbar(window_2)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_box_ = Text(window_2, height=11, width=47, font=("arial", "12"))
    text_box_.pack()
    # scrollbar configured!; i hate scrollbars in python3 tkinter.
    scrollbar.config(command=text_box.yview)
    but = Button(window_2, text="submit", padx=20, pady=5, fg="green", command=decode_submit)
    but.pack(padx=10, pady=20)

    window_2.mainloop()

# defining the encryption window function.
def coder():
    global window_1
    global text_box
    window_1 = Toplevel(window)
    window_1.title("PyDcoder_Adjustable-GUI by __ilprofessore ")
    window_1.geometry("400x400")
    window_1.iconbitmap("icon/image.ico")
    window_1.resizable(height=False, width=False)
    # making all the necessary stuff for the encryption window.
    header = "Welcome to PyDcoder_Adjustable-GUI Encryptor"
    line_1 = "only plain text along with spaces, commas" \
             "\nand fullstops are to be used;" \
             "\nnumbers and/or special characters" \
             "\nare not allowed."
    line_1 = line_1.upper()
    my_label = Label(window_1, text=header, padx=5, pady=5, font=("arial", "12"), bg="grey", fg="blue")
    my_label.pack(padx=5, pady=5)
    Label(window_1, text=line_1, padx=5, pady=5, font=("arial", "10"), fg="red").pack(padx=5, pady=5)
    # i know, it's a shitty scroll bar; i just copied and pasted it.
    scrollbar = Scrollbar(window_1)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_box = Text(window_1, height=11, width=47, font=("arial", "12"))
    text_box.pack()
    var = "all the text will be automatically converted to lowercase upon encryption."
    text_box.insert(1.0, var)
    # scrollbar configured!; i hate scrollbars in python3 tkinter.
    scrollbar.config(command=text_box.yview)
    butt = Button(window_1, text="submit", padx=20, pady=5, fg="magenta", command=code_submit)
    butt.pack(padx=10, pady=20)

    window_1.mainloop()

# creating the main window.
window = Tk()
window.title("PyDcoder_Adjustable-GUI by __ilprofessore ")
window.geometry("400x350")
window.iconbitmap("icon/image.ico")
window.resizable(height=False, width=False)
# making the necessary labels and buttons.
_header = "Welcome to PyDcoder_Adjustable-GUI Home"
Label(window, text="").pack()
my__label = Label(window, text=_header, padx=5, pady=5, font=("arial", "12"), bg="grey", fg="blue")
my__label.pack(padx=5, pady=5)
Label(window, text="made by __ilprofessore", padx=5, pady=5, font=("arial", "8"), fg="red").pack()
Label(window, text="").pack()
Label(window, text="").pack()
Button(window, text="Encrypt text", padx=30, pady=10, fg="magenta", command=coder).pack(padx=10, pady=10)
Label(window, text="").pack()
Button(window, text="Decrypt text", padx=30, pady=10, fg="green", command=decoder).pack(padx=10, pady=10)

window.mainloop()
