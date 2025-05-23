def mergeSort(arr):
    if len(arr)==1:
        return arr
    medio=len(arr)//2
    izquierda_array=arr[:medio]
    derecha_array=arr[medio:]
    
    ordenamiento_izquierda_array=mergeSort(izquierda_array)
    ordenamiento_derecha_array=mergeSort(derecha_array)

    return  Merge(ordenamiento_izquierda_array,ordenamiento_derecha_array)

def Merge(izquierda_array,derecha_array):
    arr_resultado=[]
    while len(izquierda_array)>0 and len(derecha_array)>0:
        if izquierda_array[0]>derecha_array[0]:
            arr_resultado.append(derecha_array[0])
            derecha_array.pop(0)
        else:
            arr_resultado.append(izquierda_array[0])
            izquierda_array.pop(0) 
    while len(izquierda_array)> 0:
        arr_resultado.append(izquierda_array[0])
        izquierda_array.pop(0)
    while len(derecha_array)>0:
        arr_resultado.append(derecha_array[0])
        derecha_array.pop(0)
    return arr_resultado             

areglo=[10,20,54,89,78,41,100,1,3,5,25]
areglo_ord=mergeSort(areglo)

print("lista original ",areglo)
print("lista ordenada: ",areglo_ord)