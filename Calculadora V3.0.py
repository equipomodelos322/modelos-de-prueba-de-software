import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("250x390")
ventana.resizable(False, False)
ventana.configure(bg="#202020")

expresion = ""
memoria = 0



# PANTALLA


pantalla = tk.Entry(
    ventana,
    font=("Arial", 18),
    justify="right",
    bd=2,
    bg="#303030",
    fg="white",
    insertbackground="white"
)
pantalla.place(x=20, y=20, width=210, height=40)


etiqueta_memoria = tk.Label(
    ventana,
    text="M: 0",
    font=("Arial", 9, "bold"),
    bg="#202020",
    fg="#f0a030",
    anchor="w"
)
etiqueta_memoria.place(x=20, y=62, width=210, height=12)



# AUXILIARES


def formatear(n):
    """Muestra 5 en vez de 5.0, pero conserva los decimales reales."""
    return str(int(n)) if n == int(n) else str(n)


def mostrar(texto):
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto)


def valor_en_pantalla():
    """Evalua lo que se ve en pantalla de forma segura. None si no se puede."""
    texto = pantalla.get()

    if not texto or texto == "Error":
        return None

    limpia = texto.strip()

    
    while limpia and limpia[-1] in "+-*/ ":
        limpia = limpia[:-1].strip()

    if not limpia:
        return None

    try:
        return eval(limpia)
    except (SyntaxError, ZeroDivisionError, NameError):
        return None


def actualizar_indicador():
    etiqueta_memoria.config(text="M: " + formatear(memoria))



# OPERACIONES

def numero(valor):
    global expresion

    if expresion == "Error":
        expresion = ""

    expresion += valor

    mostrar(expresion)


def operacion(op):
    global expresion

    if expresion == "" or expresion == "Error":
        return

    if expresion.strip()[-1] not in "+-*/":
        expresion += " " + op + " "

        mostrar(expresion)


def calcular():
    global expresion, memoria

    resultado = valor_en_pantalla()

    if resultado is None:
        if pantalla.get():
            expresion = "Error"
            mostrar("Error")
        return

    expresion = formatear(resultado)
    memoria = resultado
    actualizar_indicador()

    mostrar(expresion)


def borrar():
    global expresion

    expresion = ""

    pantalla.delete(0, tk.END)



# MEMORIA


def mr():
    global expresion
    try:
        expresion = formatear(memoria)
        mostrar(expresion)
    except Exception as e:
        print("Error en MR:", e)


def mc():
    global memoria
    try:
        memoria = 0
        actualizar_indicador()
    except Exception as e:
        print("Error en MC:", e)


def mp():
    global memoria
    try:
        valor = valor_en_pantalla()
        if valor is not None:
            memoria += valor
            actualizar_indicador()
    except Exception as e:
        print("Error en M+:", e)


def mm():
    global memoria
    try:
        valor = valor_en_pantalla()
        if valor is not None:
            memoria -= valor
            actualizar_indicador()
    except Exception as e:
        print("Error en M-:", e)


# CREAR BOTONES


def crear_boton(texto, comando, x, y):

    boton = tk.Button(
        ventana,
        text=texto,
        command=comando,
        font=("Arial", 10, "bold"),
        bg="#333333",
        fg="white",
        activebackground="#505050",
        activeforeground="white",
        bd=1
    )

    boton.place(
        x=x,
        y=y,
        width=40,
        height=40
    )


crear_boton("MR", mr, 20, 75)
crear_boton("MC", mc, 70, 75)
crear_boton("M+", mp, 120, 75)
crear_boton("M-", mm, 170, 75)

crear_boton("1", lambda: numero("1"), 20, 125)
crear_boton("2", lambda: numero("2"), 70, 125)
crear_boton("3", lambda: numero("3"), 120, 125)
crear_boton("+", lambda: operacion("+"), 170, 125)

crear_boton("4", lambda: numero("4"), 20, 175)
crear_boton("5", lambda: numero("5"), 70, 175)
crear_boton("6", lambda: numero("6"), 120, 175)
crear_boton("-", lambda: operacion("-"), 170, 175)

crear_boton("7", lambda: numero("7"), 20, 225)
crear_boton("8", lambda: numero("8"), 70, 225)
crear_boton("9", lambda: numero("9"), 120, 225)
crear_boton("*", lambda: operacion("*"), 170, 225)

crear_boton("0", lambda: numero("0"), 20, 275)
crear_boton("AC", borrar, 70, 275)
crear_boton("=", calcular, 120, 275)
crear_boton("/", lambda: operacion("/"), 170, 275)


ventana.mainloop()