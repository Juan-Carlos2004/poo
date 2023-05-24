import tkinter as tk
import numpy as np
import random
from PIL import Image, ImageTk
#crear ventana
ventana = tk.Tk()
ventana.title("Black jack")
ventana.geometry("1400x800")
#tablero------------------------------------------------
tablero= Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/blackjackmesa.png')
tablero = tablero.resize((1400,800))
imagentk = ImageTk.PhotoImage(tablero)

etiquetaImagen = tk.Label(ventana,image=imagentk)
etiquetaImagen.grid(row=1,column=1)
#posisiones---------------------------------------------------
#-------------------------------------------------------------+
#baraja = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
#baraja = baraja.resize((150,200))
#imagentk2 = ImageTk.PhotoImage(baraja)

#etiquetaImagen2 = tk.Label(ventana,image=imagentk2)
#etiquetaImagen2.place(x = 1050,y =10)
#---------------------------------------------------
etiquetacuentaplayer = tk.Label(ventana,text ="cuentaplayer")
etiquetacuentaplayer.place(x = 40,y =600)
#---------------------------------------------------
etiquetacuentacasa = tk.Label(ventana,text ="cuentacasa")
etiquetacuentacasa.place(x = 40,y =650)
#-------------------------------------------------------
etiquetaganador = tk.Label(ventana,text ="ganador")
etiquetaganador.place(x = 40,y =700)
#---------------------------------------------------
primeracartaplayer = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
primeracartaplayer = primeracartaplayer.resize((150,200))
primeracartaplayertk2 = ImageTk.PhotoImage(primeracartaplayer)

etiquetaprimeracartaplayer = tk.Label(ventana,image=primeracartaplayertk2)
etiquetaprimeracartaplayer.place(x = 150,y =490)
#---------------------------------------------------
segundacartaplayer = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
segundacartaplayer = segundacartaplayer.resize((150,200))
segundacartaplayertk2 = ImageTk.PhotoImage(segundacartaplayer)

etiquetaSegundacartaplayer = tk.Label(ventana,image=segundacartaplayertk2)
etiquetaSegundacartaplayer.place(x = 350,y =490)
#---------------------------------------------------
TerceraCartaPlayer = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
TerceraCartaPlayer = TerceraCartaPlayer.resize((150,200))
TerceraCartaPlayertk2 = ImageTk.PhotoImage(TerceraCartaPlayer)

EtiquetaTerceraCartaPlayerTK = tk.Label(ventana,image=TerceraCartaPlayertk2)
EtiquetaTerceraCartaPlayerTK.place(x = 550,y =490)
#---------------------------------------------------
CuartaCartaPlayer = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
CuartaCartaPlayer = TerceraCartaPlayer.resize((150,200))
CuartaCartaPlayertk2 = ImageTk.PhotoImage(TerceraCartaPlayer)

EtiquetaCuartacartaPlayerTK = tk.Label(ventana,image=CuartaCartaPlayertk2)
EtiquetaCuartacartaPlayerTK.place(x = 750,y =490)
#casa------------------------------------------------------
#---------------------------------------------------
primeracartaCasa = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
primeracartaCasa = primeracartaCasa.resize((150,200))
primeracartaCasatk2 = ImageTk.PhotoImage(primeracartaCasa)

etiquetaprimeracartaCasa = tk.Label(ventana,image=primeracartaCasatk2)
etiquetaprimeracartaCasa.place(x = 150,y =50)
#---------------------------------------------------
segundacartaCasa = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
segundacartaCasa = segundacartaCasa.resize((150,200))
segundacartaCasatk2 = ImageTk.PhotoImage(segundacartaCasa)

etiquetaSegundacartaCasa = tk.Label(ventana,image=segundacartaCasatk2)
etiquetaSegundacartaCasa.place(x = 350,y =50)
#---------------------------------------------------
TerceraCartaCasa = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
TerceraCartaCasa = TerceraCartaCasa.resize((150,200))
TerceraCartaCasatk2 = ImageTk.PhotoImage(TerceraCartaCasa)

EtiquetaTerceraCartaCasaTK = tk.Label(ventana,image=TerceraCartaCasatk2)
EtiquetaTerceraCartaCasaTK.place(x = 550,y =50)
#---------------------------------------------------
CuartaCartaCasa = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/baraja.png')
CuartaCartaCasa = TerceraCartaCasa.resize((150,200))
CuartaCartaCasatk2 = ImageTk.PhotoImage(TerceraCartaCasa)

EtiquetaCuartacartaCasaTK = tk.Label(ventana,image=CuartaCartaCasatk2)
EtiquetaCuartacartaCasaTK.place(x = 750,y =50)
#cartas----------------------------------------------------
#picas----------------------------------------------------------
picas1 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/1picas.png')
picas1 = picas1.resize((150,200))
picas1TK = ImageTk.PhotoImage(picas1)
picas11 = picas1TK
picas11 = 1
#----------------------------
picas2 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/2picas.png')
picas2 = picas2.resize((150,200))
picas2Tk = ImageTk.PhotoImage(picas2)
picas11 = picas1TK
picas11 = 1
#-----------------------------
picas3 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/3picas.png')
picas3 = picas3.resize((150,200))
picas3Tk = ImageTk.PhotoImage(picas3)
picas11 = picas1TK
picas11 = 1
#-----------------------------
picas4 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/4picas.png')
picas4 = picas4.resize((150,200))
picas4Tk = ImageTk.PhotoImage(picas4)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas5 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/5picas.png')
picas5 = picas5.resize((150,200))
picas5Tk = ImageTk.PhotoImage(picas5)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas6 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/6picas.png')
picas6 = picas6.resize((150,200))
picas6Tk = ImageTk.PhotoImage(picas6)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas7 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/7picas.png')
picas7 = picas7.resize((150,200))
picas7Tk = ImageTk.PhotoImage(picas7)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas8 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/8picas.png')
picas8 = picas8.resize((150,200))
picas8Tk = ImageTk.PhotoImage(picas8)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas9 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/9picas.png')
picas9 = picas9.resize((150,200))
picas9Tk = ImageTk.PhotoImage(picas9)
picas11 = picas1TK
picas11 = 1
#---------------------------------------
picas10 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/10picas.png')
picas10 = picas10.resize((150,200))
picas10Tk = ImageTk.PhotoImage(picas10)
picas11 = picas1TK
picas11 = 1
#treboles-------------------------------------------------------
#---------------------------------------------------------------
trebol1 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/1trebol.png')
trebol1 = trebol1.resize((150,200))
trebol1Tk = ImageTk.PhotoImage(trebol1)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol2 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/2trebol.png')
trebol2 = trebol2.resize((150,200))
trebol2Tk = ImageTk.PhotoImage(trebol2)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol3 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/3trebol.png')
trebol3 = trebol3.resize((150,200))
trebol3Tk = ImageTk.PhotoImage(trebol3)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol4 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/4trebol.png')
trebol4 = trebol4.resize((150,200))
trebol4Tk = ImageTk.PhotoImage(trebol4)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol5 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/5trebol.png')
trebol5 = trebol5.resize((150,200))
trebol5Tk = ImageTk.PhotoImage(trebol5)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol6 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/6trebol.png')
trebol6 = trebol6.resize((150,200))
trebol6Tk = ImageTk.PhotoImage(trebol6)
trebol11 = trebol1Tk
trebol11 = 1
#---------------------------------------
trebol7 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/7trebol.png')
trebol7 = trebol7.resize((150,200))
trebol7Tk11 = ImageTk.PhotoImage(trebol7)
trebol11 = trebol1Tk
trebol11 = 1
#----------------------------
trebol8 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/8trebol.png')
trebol8 = trebol8.resize((150,200))
trebol8Tk = ImageTk.PhotoImage(trebol8)
trebol11 = trebol1Tk
trebol11 = 1
#-----------------------------
trebol9 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/9trebol.png')
trebol9 = trebol9.resize((150,200))
trebol9Tk = ImageTk.PhotoImage(trebol9)
trebol11 = trebol1Tk
trebol11 = 1
#-----------------------------
trebol10 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/10trebol.png')
trebol10 = trebol10.resize((150,200))
trebol10Tk = ImageTk.PhotoImage(trebol10)
trebol11 = trebol1Tk
trebol11 = 1
#diamantes---------------------------------------
#---------------------------------------
diamantes1 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/1diamantes.png')
diamantes1 = diamantes1.resize((150,200))
diamantes1Tk = ImageTk.PhotoImage(diamantes1)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes2 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/2diamantes.png')
diamantes2 = diamantes2.resize((150,200))
diamantes2Tk = ImageTk.PhotoImage(diamantes2)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes3 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/3diamantes.png')
diamantes3 = diamantes3.resize((150,200))
diamantes3Tk = ImageTk.PhotoImage(diamantes3)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes4 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/4diamantes.png')
diamantes4 = diamantes4.resize((150,200))
diamantes4Tk = ImageTk.PhotoImage(diamantes4)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes5 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/5diamantes.png')
diamantes5 = diamantes5.resize((150,200))
diamantes5Tk = ImageTk.PhotoImage(diamantes5)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes6 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/6diamantes.png')
diamantes6 = diamantes6.resize((150,200))
diamantes6Tk = ImageTk.PhotoImage(diamantes6)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes7 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/7diamantes.png')
diamantes7 = diamantes7.resize((150,200))
diamantes7Tk = ImageTk.PhotoImage(diamantes7)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes8 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/8diamantes.png')
diamantes8 = diamantes8.resize((150,200))
diamantes8Tk = ImageTk.PhotoImage(diamantes8)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes9 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/9diamantes.png')
diamantes9 = diamantes9.resize((150,200))
diamantes9Tk = ImageTk.PhotoImage(diamantes9)
diamantes11 = diamantes1Tk
diamantes11 = 1
#---------------------------------------
diamantes10 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/10diamantes.png')
diamantes10 = diamantes10.resize((150,200))
diamantes10Tk = ImageTk.PhotoImage(diamantes10)
diamantes11 = diamantes1Tk
diamantes11 = 1
#corazonez---------------------------------------
#------------------------------------------------
corazon1 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/1corazon.png')
corazon1 = corazon1.resize((150,200))
corazon1Tk = ImageTk.PhotoImage(corazon1)
diamantes11
#---------------------------------------
corazon2 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/2corazon.png')
corazon2 = corazon2.resize((150,200))
corazon2Tk = ImageTk.PhotoImage(corazon2)
#---------------------------------------
corazon3 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/3corazon.png')
corazon3 = corazon3.resize((150,200))
corazon3Tk11 = ImageTk.PhotoImage(corazon3)
#----------------------------
corazon4 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/4corazon.png')
corazon4 = corazon4.resize((150,200))
corazon4Tk = ImageTk.PhotoImage(corazon4)
#-----------------------------
corazon5 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/5corazon.png')
corazon5 = corazon5.resize((150,200))
corazon5Tk13 = ImageTk.PhotoImage(corazon5)
#-----------------------------
corazon6 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/6corazon.png')
corazon6 = corazon6.resize((150,200))
corazonTK6 = ImageTk.PhotoImage(corazon6)
#---------------------------------------
corazon7 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/7corazon.png')
corazon7 = corazon7.resize((150,200))
corazon7TK = ImageTk.PhotoImage(corazon7)
#---------------------------------------
corazon8 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/8corazon.png')
corazon8 = corazon8.resize((150,200))
corazon8TK = ImageTk.PhotoImage(corazon8)
#---------------------------------------
corazon9 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/9corazon.png')
corazon9 = corazon9.resize((150,200))
corazon9Tk = ImageTk.PhotoImage(corazon9)
#---------------------------------------
corazon10 = Image.open('C:/Users/1/Documents/Uaq trabajos/BlackJackPy/10corazon.png')
corazon10 = corazon10.resize((150,200))
corazon10Tk = ImageTk.PhotoImage(corazon10)
#---------------------------------------
#logica---------------------------------------
mazo = np.array ([picas1TK,picas2Tk,picas3Tk,picas4Tk,picas5Tk,picas6Tk,picas7Tk,picas8Tk,picas8Tk,picas10Tk,corazon1Tk,corazon2Tk,corazon3Tk11,corazon4Tk,corazon5Tk13,corazonTK6,corazon7TK,corazon8TK,corazon9Tk,corazon10Tk,trebol1Tk,trebol2Tk,trebol3Tk,trebol4Tk,trebol5Tk,trebol6Tk,trebol7Tk11,trebol8Tk,trebol9Tk,trebol10Tk,diamantes1Tk,diamantes2Tk,diamantes3Tk,diamantes4Tk,diamantes5Tk,diamantes6Tk,diamantes7Tk,diamantes8Tk,diamantes9Tk,diamantes10Tk])
valormazo = np.array([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10])
bandera = 1
def comenzar():
        global cuentaplayer
        global cuentacasa
        i= random.randint(0,40)
        a= random.randint(0,40)
        etiquetaprimeracartaplayer.config(image=mazo[i])
        etiquetaprimeracartaCasa.config(image=mazo[a])
        cuentaplayer = valormazo [i]
        cuentacasa = valormazo [a]
def tomar1():
    global bandera
    global cuentaplayer1
    global cuentacasa1
    #global repartidas
   
    #if (bandera == 2):
        
    i= random.randint(0,40)
    a= random.randint(0,40)
        #repartidas = np.array()
    etiquetaSegundacartaplayer.config(image=mazo[i])
    etiquetaSegundacartaCasa.config(image=mazo[a])
    cuentaplayer1 = valormazo [i]
    cuentacasa1 = valormazo [a]
        #bandera = bandera+1
def tomar2():
    global cuentaplayer2
    global cuentacasa2  
    i= random.randint(0,40)
    a= random.randint(0,40)
        
    EtiquetaTerceraCartaPlayerTK.config(image=mazo[i])
    EtiquetaTerceraCartaCasaTK.config(image=mazo[a])
    cuentaplayer2 = valormazo [i]
    cuentacasa2 = valormazo [a]
def tomar3():
    global cuentaplayer3
    global cuentacasa3
    i= random.randint(0,40)
    a= random.randint(0,40)
    EtiquetaCuartacartaPlayerTK.config(image=mazo[i])
    EtiquetaCuartacartaCasaTK.config(image=mazo[a])
    cuentaplayer3 = valormazo [i]
    cuentacasa3 = valormazo [a]
def reiniciar():
    etiquetaprimeracartaplayer.config(image=TerceraCartaPlayertk2)
    etiquetaprimeracartaCasa.config(image=TerceraCartaPlayertk2)
    etiquetaSegundacartaplayer.config(image=TerceraCartaPlayertk2)
    etiquetaSegundacartaCasa.config(image=TerceraCartaPlayertk2)
    EtiquetaTerceraCartaPlayerTK.config(image=TerceraCartaPlayertk2)
    EtiquetaTerceraCartaCasaTK.config(image=TerceraCartaPlayertk2)
    EtiquetaCuartacartaPlayerTK.config(image=TerceraCartaPlayertk2)
    EtiquetaCuartacartaCasaTK.config(image=TerceraCartaPlayertk2)
def finalizar():
    global cuentaplayer
    global cuentaplayer1
    global cuentaplayer2
    global cuentaplayer3
    #print(cuentaplayer,cuentaplayer1,cuentaplayer2,cuentaplayer3,)
    cuentafianlplayer = cuentaplayer+cuentaplayer2+cuentaplayer3+cuentaplayer1
    print(cuentafianlplayer)
    cuentaplayer  = 0
    cuentaplayer1 = 0
    cuentaplayer2 = 0
    cuentaplayer3 = 0
    global cuentacasa
    global cuentacasa1
    global cuentacasa2
    global cuentacasa3
    #print(cuentacasa,cuentacasa1,cuentacasa2,cuentacasa3,)
    cuentafianlcasa = cuentacasa+cuentacasa2+cuentacasa3+cuentacasa1
    print(cuentafianlcasa)
    cuentacasa  = 0
    cuentacasa1 = 0
    cuentacasa2 = 0
    cuentacasa3 = 0
    etiquetacuentaplayer.config(text = "Cuenta player: "+str(cuentafianlplayer))
    etiquetacuentacasa.config(text = "Cuenta casa: "+str(cuentafianlcasa))
boton1 = tk.Button(ventana, text="Tomar",command=tomar1)
boton1.place(x = 100,y =100)
boton2 = tk.Button(ventana, text="Tomar2",command=tomar2)
boton2.place(x = 100,y =200)
boton3 = tk.Button(ventana, text="Tomar3",command=tomar3)
boton3.place(x = 100,y =300)
boton4 = tk.Button(ventana, text="comenzar",command=comenzar)
boton4.place(x = 100,y =10)
boton5 = tk.Button(ventana, text="reiniciar",command=reiniciar)
boton5.place(x = 100,y =400)
boton6 = tk.Button(ventana, text="finalizar",command=finalizar)
boton6.place(x = 100,y =500)
#Label
ventana.mainloop()