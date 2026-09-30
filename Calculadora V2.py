import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("250x350")
ventana.resizable(False, False)
ventana.configure(bg="grey")

expresion = ""

pantalla = tk.Entry(
    ventana,
    font=("Arial", 18),
    justify="right",
    bd=2
)

pantalla.place(x=40, y=45, width=160, height=35)


def numero(valor):
    global expresion

    expresion += valor

    pantalla.delete(0, tk.END)
    pantalla.insert(0, expresion)


def operacion(op):
    global expresion

    if expresion != "":
        if expresion[-1] not in "+-*/":
            expresion += " " + op + " "

            pantalla.delete(0, tk.END)
            pantalla.insert(0, expresion)


def calcular():
    global expresion

    if expresion != "":
        try:
            resultado = eval(expresion)

            if resultado == int(resultado):
                resultado = int(resultado)

            pantalla.delete(0, tk.END)
            pantalla.insert(0, str(resultado))

            expresion = str(resultado)

        except ZeroDivisionError:
            pantalla.delete(0, tk.END)
            pantalla.insert(0, "Error")
            expresion = ""

        except:
            pantalla.delete(0, tk.END)
            pantalla.insert(0, "Error")
            expresion = ""


def borrar():
    global expresion

    expresion = ""

    pantalla.delete(0, tk.END)


boton1 = tk.Button(ventana, text="1", command=lambda: numero("1"))
boton2 = tk.Button(ventana, text="2", command=lambda: numero("2"))
boton3 = tk.Button(ventana, text="3", command=lambda: numero("3"))

boton4 = tk.Button(ventana, text="4", command=lambda: numero("4"))
boton5 = tk.Button(ventana, text="5", command=lambda: numero("5"))
boton6 = tk.Button(ventana, text="6", command=lambda: numero("6"))

boton7 = tk.Button(ventana, text="7", command=lambda: numero("7"))
boton8 = tk.Button(ventana, text="8", command=lambda: numero("8"))
boton9 = tk.Button(ventana, text="9", command=lambda: numero("9"))

boton0 = tk.Button(ventana, text="0", command=lambda: numero("0"))

boton_suma = tk.Button(
    ventana,
    text="+",
    command=lambda: operacion("+")
)

boton_resta = tk.Button(
    ventana,
    text="-",
    command=lambda: operacion("-")
)

boton_multiplicacion = tk.Button(
    ventana,
    text="*",
    command=lambda: operacion("*")
)

boton_division = tk.Button(
    ventana,
    text="/",
    command=lambda: operacion("/")
)

boton_igual = tk.Button(
    ventana,
    text="=",
    command=calcular
)

boton_ac = tk.Button(
    ventana,
    text="AC",
    command=borrar
)

boton1.place(x=40, y=100, width=30, height=30)
boton2.place(x=80, y=100, width=30, height=30)
boton3.place(x=120, y=100, width=30, height=30)
boton_suma.place(x=160, y=100, width=30, height=30)

boton4.place(x=40, y=140, width=30, height=30)
boton5.place(x=80, y=140, width=30, height=30)
boton6.place(x=120, y=140, width=30, height=30)
boton_resta.place(x=160, y=140, width=30, height=30)

boton7.place(x=40, y=180, width=30, height=30)
boton8.place(x=80, y=180, width=30, height=30)
boton9.place(x=120, y=180, width=30, height=30)
boton_multiplicacion.place(x=160, y=180, width=30, height=30)

boton0.place(x=40, y=220, width=30, height=30)
boton_ac.place(x=80, y=220, width=30, height=30)
boton_igual.place(x=120, y=220, width=30, height=30)
boton_division.place(x=160, y=220, width=30, height=30)

ventana.mainloop()