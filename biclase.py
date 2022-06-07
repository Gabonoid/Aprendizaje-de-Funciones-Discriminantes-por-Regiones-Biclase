import funDiscBiClase as fd

vectores = fd.generarCMA()
print(vectores)
funDiscLineal = fd.calcularFD(vectores)
print(f"Solución final: {funDiscLineal}")
