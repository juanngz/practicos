def altura(arr, grado):
    m = len(arr) - 1    # mayor índice ocupado (no es un recorrido del árbol)
    while m >= 0 and arr[m] is None:
        m -= 1
    if m < 0:
        return -1          # árbol vacío
    h = 0
    while m > 0:           # subir por padres hasta la raíz
        m = (m - 1) // grado
        h += 1
    return h               # raíz sola = altura 0


def preorden(arr, k, i=0, visitados=None):
    if visitados is None:
        visitados = []
    if i >= len(arr) or arr[i] is None:
        return visitados
    visitados.append(arr[i])
    for j in range(1, k + 1):
        preorden(arr, k, k * i + j, visitados)
    return visitados

def main():
    # ejemplo: grado = 3
    arr = ['A', 'B', 'C', 'D', 'E', None, 'F', None, None, None, 'G', None, None]    #2
    arr2 = ['A', 'B']    #1
    arr3 = ['A']    #0
    # a)
    print(altura(arr, 3))
    print(altura(arr2, 3))
    print(altura(arr3, 3))
    # b)
    print(preorden(arr, 3))

main()
