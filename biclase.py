import funDiscBiClase as fd
import numpy as np

if __name__ == "__main__":
    vectores = fd.generarCMA()
    print(vectores)
    print(f"Soluciòn final: {fd.calcularFD(vectores)}")
    
    #vectorPrueba = [0,0,0]
    #dotprueba = np.dot(vectores[0][0], vectorPrueba)
    #print(dotprueba)