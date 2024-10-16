import numpy as np
import time
from scipy.spatial import distance

# 1. Дан случайный массив, поменять знак у элементов, значения которых между 3 и 8
def change_massive(arr: np.ndarray) -> None:
    arr[3:8] = arr[3:8] * -1
    print("Измененный массив:", arr)

arr = np.arange(10)
print("Исходный массив:", arr)
change_massive(arr)

# 2. Заменить максимальный элемент случайного массива на 0
def change_max(arr: np.ndarray) -> None:
    index = np.where(arr == np.max(arr))
    arr[index] = 0
    print("Массив после замены максимального элемента на 0:", arr)

change_max(arr)

# 3. Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B.
arr1 = np.arange(24).reshape(8, 3)
arr2 = np.arange(4, 8).reshape(2, 2)

def get_all_values(arr1: np.ndarray, arr2: np.ndarray) -> list:
    matching_rows = []
    for arr_2row in arr2:
        for arr1_row in arr1:
            if all(item in arr1_row for item in arr_2row):
                matching_rows.append(arr1_row)
    return matching_rows

print("Строки из A, содержащие элементы из каждой строки в B:")
print(get_all_values(arr1, arr2))

# 4. Дана 10x3 матрица, найти строки из неравных значений.
arr = np.array([[1, 2, 3, 2, 3, 4, 5, 3, 5, 3],
                [1, 2, 3, 4, 5, 6, 7, 7, 6, 5],
                [2 for i in range(10)]])

def check_all_values(arr: np.ndarray) -> np.ndarray:
    indecis = []
    for row in arr:
        indecis.append(not(np.all([row[0] == row])))
    return arr[indecis]

print("Строки с неравными значениями:")
print(check_all_values(arr))

# 5. Удалить те строки, которые повторяются.
arr2d = np.array([[i for i in range(10)],
                  [i for i in range(10)],
                  [i for i in range(10)],
                  [10 for i in range(10)],
                  [5 for i in range(10)]])

def del_strings(arr: np.ndarray) -> np.ndarray:
    unique_arr = np.unique(arr, axis=0)
    return unique_arr

print("Уникальные строки:")
print(del_strings(arr2d))

# 6. Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы.
def diagonal(arr: np.ndarray) -> int:
    if arr.ndim != 2:
        raise ValueError("Входной массив должен быть двумерным.")

    min_dim = min(arr.shape)
    
    counter = 1
    for i in range(min_dim):
        if arr[i][i] != 0:
            counter *= arr[i][i]
    
    return counter

def diagonal_with_numpy(arr: np.ndarray) -> int:
    diagonal_elements = np.diagonal(arr)
    result = np.prod(diagonal_elements[diagonal_elements != 0])
    return result

X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]])
print("Произведение ненулевых элементов на диагонали (с NumPy):", diagonal_with_numpy(X))

# 7. Проверить мультимножества.
def multi_set(x: list[int], y: list[int]) -> bool:
     return sorted(x) == sorted(y)

def np_multi_set(x: np.ndarray, y: np.ndarray) -> bool:
     return np.all(np.sort(x) == np.sort(y))

print("Проверка мультимножеств (с NumPy):", np_multi_set(np.array([1, 2, 2, 4]),np.array([4, 2, 1, 2])))

# 8. Найти максимальный элемент в векторе x среди элементов перед которыми стоит ноль.
def zero_before(arr: np.ndarray) -> int:
     sp = []
     before_el = None
     for el in arr:
          if before_el == 0:
               sp.append(el)
          before_el = el
     return max(sp) if sp else None

def zero_before_np(arr: np.ndarray) -> int:
    mask = np.roll(arr, shift=1) == 0
    mask[0] = False  
    elements_after_zero = arr[mask]
    return int(np.max(elements_after_zero)) if elements_after_zero.size > 0 else None 

print("Максимальный элемент после нуля (с NumPy):", zero_before_np(np.array([6, 2, 0, 3, 0, 0, 5])))

# Задача на кодирование длин серий (Run-length encoding).
def run_length_encoding(arr: list[int]) -> tuple[list[int], list[int]]:
     list_for_values = []
     list_for_count = []
     
     previous_value = None
     count = 0
     
     for value in arr:
         if value != previous_value:
             if previous_value is not None:
                 list_for_values.append(previous_value)
                 list_for_count.append(count)
             previous_value = value
             count = 1
         else:
             count += 1

     # Добавляем последнее значение и его количество
     if previous_value is not None:
         list_for_values.append(previous_value)
         list_for_count.append(count)

     return (list_for_values,list_for_count)

print("Run-length encoding:", run_length_encoding([2, 2, 2, 3, 3, 3]))

def run_length_encoding_np(arr: list[int]) -> tuple[np.ndarray]:
     arr_np = np.array(arr)
     arr_1 ,arr_2 = np.unique(arr_np ,return_counts=True)
     return (arr_1 ,arr_2)

print("Run-length encoding (с NumPy):", run_length_encoding_np([3 ,4 ,5 ,6 ,3 ,2 ,3]))

# Вычисление матрицы евклидовых расстояний между объектами.
np.random.seed(0)

X = np.random.rand(100 ,4)  
Y = np.random.rand(200 ,4)  

def manual_euclidean_distance(x: list[list[float]], y: list[list[float]]) -> list[list[float]]:
    m ,n = len(x), len(x[0])
    p ,q = len(y), len(y[0])
    dist_matrix = [[0] * p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            dist_matrix[i][j] = sum((x[i][k] - y[j][k]) ** 2 for k in range(n)) ** (1/2)
    
    return dist_matrix

start_time = time.time()
distances_manual = manual_euclidean_distance(X.tolist(), Y.tolist())
end_time = time.time()
print(f"Ручное вычисление евклидова расстояния (без NumPy) выполнено за: {end_time - start_time:.6f} секунд")

def manual_euclidean_distance_with_np(x: np.ndarray ,y: np.ndarray) -> np.ndarray:
    m ,n = x.shape
    p ,q = y.shape
    dist_matrix = np.zeros((m ,p))
    
    for i in range(m):
        for j in range(p):
            dist_matrix[i,j] = np.sqrt(np.sum((x[i] - y[j]) ** 2))
    
    return dist_matrix

start_time = time.time()
distances_np = manual_euclidean_distance_with_np(X ,Y)
end_time = time.time()
print(f"Ручное вычисление евклидова расстояния (с NumPy) выполнено за: {end_time - start_time:.6f} секунд")

start_time = time.time()
distances_cdist = distance.cdist(X ,Y ,'euclidean')
end_time = time.time()
print(f"Вычисление cdist из scipy выполнено за: {end_time - start_time:.6f} секунд")

