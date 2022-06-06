import funDiscBiClase as fd
import numpy as np

if __name__ == "__main__":
    vectores = fd.generarCMA()
    print(vectores)
    funDiscLineal = fd.calcularFD(vectores)
    print(f"Soluciòn final: {funDiscLineal}")
