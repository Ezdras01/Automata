import networkx as nx  # Importamos una biblioteca para trabajar con gráficos
import matplotlib.pyplot as plt  # Importamos una biblioteca para dibujar gráficos

# Esta función recoge los datos de los estados del autómata
def datos_estados():
    global estados
    numero_estados = input('Dame el número de estados del autómata: ')
    while not numero_estados.isdecimal() or numero_estados == "":
        numero_estados = input('Ingrese un número entero positivo: ')
    while int(numero_estados) < 1:
        numero_estados = input('Ingrese un número entero mayor que 0: ')
    for i in range(1, int(numero_estados) + 1):
        estados.append("q" + str(i))

# Esta función recoge los datos del alfabeto del autómata
def datos_alfabeto():
    global alfabeto
    numero_alfabeto = input('Dame el número de símbolos del alfabeto: ')
    while not numero_alfabeto.isdecimal() or numero_alfabeto == "":
        numero_alfabeto = input('Ingrese un número entero positivo: ')
    while int(numero_alfabeto) < 1:
        numero_alfabeto = input('Ingrese un número entero mayor que 0: ')
    while len(alfabeto) != int(numero_alfabeto):
        entrada_alfabeto = input('Ingrese un símbolo del alfabeto: ')
        if len(entrada_alfabeto) != 1 or entrada_alfabeto in alfabeto or entrada_alfabeto == "":
            print("Ingrese un símbolo válido y diferente a los anteriores")
            continue
        alfabeto.append(entrada_alfabeto)

# Esta función recoge las transiciones del autómata
def datos_transicion():
    global tabla_transiciones
    global funcion_transicion
    transiciones = list()
    for estado1 in estados:
        for valor in alfabeto:
            estado2 = input(f"Dame la transición de {estado1} cuando el valor es {valor}: ")
            while not (estado2 in estados):
                estado2 = input(f"Dame un estado existente en el autómata para la transición de {estado1} cuando el valor es {valor}: ")
            funcion_transicion.append(estado1 + ";" + estado2 + ";" + valor)
            transiciones.append(estado2)
        tabla_transiciones[estado1] = transiciones
        transiciones = []

# Esta función recoge el estado inicial del autómata
def datos_inicio():
    global estado_inicial
    estado_inicial = input('Dame el estado inicial: ')
    while not (estado_inicial in estados):
        estado_inicial = input('Dame un estado existente en el autómata: ')

# Esta función recoge los estados de aceptación del autómata
def datos_aceptacion():
    global estados
    global estados_aceptacion
    validacion = False
    while not validacion:
        validacion = True
        entrada_aceptacion = input('Dame los estados de aceptación (separados por comas): ')
        estados_aceptacion = list(entrada_aceptacion.split(","))
        for estado in estados_aceptacion:
            estado.strip()
            if not (estado in estados):
                validacion = False
                estados_aceptacion = []
                break

# Esta función recoge la cadena que queremos reconocer
def datos_lenguaje():
    validacion = False
    while not validacion:
        validacion = True
        lenguaje = input("Dame la cadena que quieres reconocer: ")
        for caracter in lenguaje:
            if not (caracter in alfabeto):
                validacion = False
    cadena = list(lenguaje)
    return cadena

# Esta función obtiene el estado siguiente basado en el estado actual y el valor
def transicion(edo_inicial, valor):
    estados_transitorios = tabla_transiciones[edo_inicial]
    edo_final = estados_transitorios[alfabeto.index(valor)]
    return edo_final

# Esta función dibuja el autómata
def dibujar_automata():
    automata = nx.DiGraph()
    etiquetas_transiciones = dict()
    for transicion in funcion_transicion:
        estado1, estado2, valor = transicion.strip().split(";")
        automata.add_edge(estado1, estado2, label=str(valor))
        etiquetas_transiciones[(estado1, estado2)] = valor

    # Dibujar el autómata
    pos = nx.spring_layout(automata)
    nx.draw_networkx(automata, pos=pos, node_size=500)
    nx.draw_networkx_edge_labels(automata, pos=pos, edge_labels=etiquetas_transiciones)
    plt.show()

# Función principal del programa
def main():
    datos_estados()  # Recoge los estados
    print(estados)
    datos_alfabeto()  # Recoge el alfabeto
    print(alfabeto)
    datos_transicion()  # Recoge las transiciones
    print(tabla_transiciones)
    datos_inicio()  # Recoge el estado inicial
    print(estado_inicial)
    datos_aceptacion()  # Recoge los estados de aceptación
    print(estados_aceptacion)
    dibujar_automata()  # Dibuja el autómata
    otro = "s"
    while otro == "s":
        cadena = datos_lenguaje()  # Recoge la cadena que queremos reconocer
        estado_final = estado_inicial
        for caracter in cadena:
            estado_final = transicion(estado_final, caracter)
            print(estado_final)
        if estado_final in estados_aceptacion:
            print("Cadena aceptada")
        else:
            print("Cadena no aceptada")
        otro = input("¿Quieres verificar otra cadena (s/n)?: ")
        while not (otro == "s" or otro == "n"):
            otro = input("¿Quieres verificar otra cadena (s/n)?: ")

# Variables globales
if __name__ == '__main__':
    estados = list()
    alfabeto = list()
    tabla_transiciones = dict()
    funcion_transicion = list()
    estado_inicial = ""
    estados_aceptacion = list()
    main()
