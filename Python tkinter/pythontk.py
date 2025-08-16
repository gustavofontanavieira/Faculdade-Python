import tkinter as tk

# Example: Create a simple Tkinter window
#Root -> janela
root = tk.Tk()
root.title("My Tkinter App")

#Cria uma "DIV" geraldá página root
#É usado como um widget de
#contêiner, isso significa que outros componentes
#são adicionados a ele com o objetivo de organizar outros widgets.
frame = tk.Frame(root)
frame.pack(padx=10, pady=10 )

#Cria um label e um input, dentro deles tem a função grid que serve como um CSS
tk.Label(frame, text="Name").grid(row=0, column=1, padx=5, pady=5)
name = tk.Entry(frame).grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="E-mail").grid(row=2, column=1, padx=5, pady=5)
name = tk.Entry(frame).grid(row=3, column=1, padx=5, pady=5)


tk.Button(frame, text="OK").grid(row=4, column=1, padx=5, pady=5)



root.mainloop()