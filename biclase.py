import funDiscBiClase as fd
import numpy as np

vectores = fd.generarCMA()
print(vectores)
funDiscLineal = fd.calcularFD(vectores)
print(f"Soluciòn final: {funDiscLineal}")
