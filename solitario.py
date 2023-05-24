import tkinter as tk
from PIL import Image, ImageTk
#crear ventana
ventana = tk.Tk()
ventana.title("Solitario")
ventana.geometry("1300x800")
imagenSource = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/blackjack-table.jpg')
imagenSource = imagenSource.resize((1300,800))
imagentk = ImageTk.PhotoImage(imagenSource)

etiquetaImagen = tk.Label(ventana,image=imagentk)
etiquetaImagen.grid(row=1,column=1)
#Label
ventana.mainloop()