import re
import tkinter as tk
from tkinter import scrolledtext
from turtle import color, left

simbolos = {
    '=': r'=','+': r'\+','-': r'-','': r'\ ','/': r'\/',
    '(': r'\(',')': r'\)','{': r'\{','}': r'\}',':': r':',';': r';',
}

parentesis_inicio = r'\('  
parentesis_cierre = r'\)'
llave_incio = r'\{'
llave_cierre = r'\}'
cadena = r'\".*?\"'
id = r'\b[a-zA-Z]+(?=\s*\()'
punto_coma = r';'
palabras_reserva = r'\b(programa|int|read|end|print)\b'
variables = r'\b(int|float|boolean|string)\s+([a-zA-Z_, ]+)\b'



def analizador_lexico():
    texto = texto_inicio.get("1.0", "end-1c")
    texto_salida.delete("1.0", tk.END) 

    pablabras_reservadas = re.findall(palabras_reserva, texto)

    cadenas = re.findall(cadena, texto)

    ids = re.findall(id, texto)

    variabless = re.findall(variables, texto)

    coma_encontrado = re.findall(punto_coma, texto)

    parenInicio_encontrados = re.findall(parentesis_inicio, texto)

    parenCierre_encontrados = re.findall(parentesis_cierre, texto)

    llave_Inicio_encontradas = re.findall(llave_incio, texto)

    llave_cierre_encontradas = re.findall(llave_cierre, texto)


    ids = [i for i in ids if i not in pablabras_reservadas]
    reservadas = list(set(pablabras_reservadas))
    vars = [i[1] for i in variabless]

    simbolos_encontrados = set()
    for simbolo, patron in simbolos.items():
        encontrado = re.findall(patron, texto)
        if encontrado:
            simbolos_encontrados.add(simbolo)

    output = f"""Palabras reservadas: {reservadas}
Cadenas: {cadenas}
Ids: {ids, vars}
Símbolos: {', '.join(simbolos_encontrados)}

Número de 'punto y coma': {len(coma_encontrado)}
Paréntesis de apertura: {len(parenInicio_encontrados)}
Paréntesis de cierre: {len(parenCierre_encontrados)}
Llaves de apertura: {len(llave_Inicio_encontradas)}
Llaves de cierre: {len(llave_cierre_encontradas)}"""

    double_parentheses = re.findall(r'\(\(|\)\)', texto)
    if double_parentheses:
        output += f"\nParéntesis dobles nodefinidos: {', '.join(double_parentheses)}"

    texto_salida.insert(tk.END, output)

ventana = tk.Tk()
ventana.geometry('800x400')
ventana.config(bg="#12657f")
texto_inicio = scrolledtext.ScrolledText(ventana, width=40, height=25)
texto_inicio.pack(side="left", anchor="e")
texto_inicio.pack(pady=10)
texto_inicio.configure(insertbackground="black")
texto_inicio.pack()
texto_salida = scrolledtext.ScrolledText(ventana, width=40, height=25)
texto_salida.pack(side="right", anchor="e")
texto_salida.pack(pady=10)
boton = tk.Button(ventana, text="Analizar", command=analizador_lexico)
boton.pack(pady=150)

ventana.mainloop()