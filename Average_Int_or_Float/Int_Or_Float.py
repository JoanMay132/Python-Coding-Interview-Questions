
def is_avg_whole(arr):
    # Escribe tu solución aquí y retorna el resultado 
    total=0
    for i in arr:
        total+=i

    promedio=total/len(arr)
    if promedio.is_integer(): 
        return True
    else:
        return False
print(is_avg_whole([1,1,1,1]))