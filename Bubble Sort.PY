import random

# Generamos 10 números aleatorios entre 1 y 100
datos = [random.randint(1, 100) for _ in range(10)]
print(f"Original: {datos}")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(f"Ordenado (Burbuja): {bubble_sort(datos)}")