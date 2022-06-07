import numpy as np


def allFalse(listBoolean):
    """Función que analiza si la lista esta lleno de False.

    Args:
        listBoolean (List): lista al cual se le aplicara el analisis.

    Returns:
        Boolean: retorna si toda la lista tiene solamente False.
    """
    isAll = False
    for i in range(len(listBoolean)):
        if(listBoolean[i] != False):
            isAll = True
    return isAll


def generarCMA():
    """Función que registra cuantos y que vectores quiere aplicar el usuario.

    Returns:
        List: Lista de listas que contienen los vectores separados por clases.
    """
    vectores = []
    for numClase in range(2):
        alpha = []
        numeroCMA = int(
            input(f"\n¿Cuántos vectores vas a ingresar en α{numClase+1}? "))
        for i in range(numeroCMA):
            vector = []
            print(f"Vector {i+1}".center(30, '-'))
            for j in range(2):
                valor = int(input(f"Ingrese el valor [{j}]: "))
                vector.append(valor)
            vector.append(1)
            alpha.append(vector)
        vectores.append(alpha)

    print()
    return vectores


def calcularFD(vectores):
    """Calcula la función discriminante lineal.

    Args:
        vectores (List): Lista de listas con vectores separadas por clases.

    Returns:
        List: Vector para generar la función discrimante lineal.
    """
    t = 1
    aprendizaje = True
    w = [0, 0, 0]

    while (aprendizaje):

        isT = []
        print(f"-".center(40, "-"))

        for i in range(len(vectores)):

            for j in range(len(vectores[i])):

                vector = vectores[i][j]
                print(f"t = {t}: {vector} ∈ α{i+1}")
                print(f"W = {w}")
                vectorDot = np.dot(vector, w)
                print(f"Producto Punto: {vectorDot}")

                if (i == 0):
                    isAcierto = vectorDot > 0
                    if isAcierto:
                        isT.append(False)
                        print("✔\n")
                    else:
                        w = np.add(w, vector)
                        isT.append(True)
                        print("X\n")

                elif (i == 1):
                    isAcierto = vectorDot < 0
                    if isAcierto:
                        isT.append(False)
                        print("✔\n")
                    else:
                        arrayW = np.array(w)
                        arrayVector = np.array(vector)
                        w = arrayW-arrayVector
                        isT.append(True)
                        print("X\n")
                t += 1

        aprendizaje = allFalse(isT)

    return w
