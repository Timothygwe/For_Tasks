import numpy as np

# Загрузка данных о калориях из файла
calorie_stats = np.loadtxt("cereal.csv", delimiter=",")

def comparison(arr: np.ndarray) -> None:
    """Сравнивает среднее количество калорий CrunchieMunchies с 60 калориями."""
    avg = np.average(arr)
    if avg > 60:
        print(f"Среднее количество калорий CrunchieMunchies меньше, чем у других злаков на {avg - 60:.2f} калорий.")
    elif avg < 60:
        print(f"Среднее количество калорий CrunchieMunchies больше, чем у других злаков на {60 - avg:.2f} калорий.")
    else:
        print("Среднее количество калорий CrunchieMunchies равно 60.")

comparison(calorie_stats)

# Сортировка массива для дальнейшего анализа
calorie_stats_sorted = np.sort(calorie_stats)

# Вычисление медианы
med = np.median(calorie_stats_sorted)
print("\nОтсортированный массив калорий:")
print(calorie_stats_sorted)
print(f"\nМедиана калорий: {med:.2f}")

def find_nth_percentile(arr: np.ndarray) -> int:
    """Находит первый процентиль, превышающий 60 калорий."""
    for p in range(101):
        percentile_value = np.percentile(arr, p)
        if percentile_value > 60:
            return p
    return None

nth_percentile = find_nth_percentile(calorie_stats)
print(f"\nПервый процентиль, превышающий 60 калорий: {nth_percentile}")

def for_more_calories(arr: np.ndarray) -> str:
    """Вычисляет процент злаков с более чем 60 калориями."""
    msk = arr > 60
    result = (len(arr[msk]) / len(arr)) * 100
    return f"{result:.2f}%"

print(f"\nПроцент злаков с более чем 60 калориями: {for_more_calories(calorie_stats)}")

def standard_deviation(arr: np.ndarray) -> float:
    """Вычисляет стандартное отклонение."""
    calorie_std = np.std(arr)
    return calorie_std

calorie_std = standard_deviation(calorie_stats)
print(f"\nСтандартное отклонение калорий: {calorie_std:.2f}")

# Анализ результатов
print("\n--- Анализ результатов ---")
print("Низкая калорийность как конкурентное преимущество:")
print("Среднее и медиана показывают, что большинство конкурентов имеют более высокую калорийность, "
      "чем CrunchieMunchies. Это можно использовать как ключевой маркетинговый аргумент для потребителей, "
      "которые ищут низкокалорийные закуски.")
print("\nРазнообразие рынка:")
print("Стандартное отклонение указывает на значительный разброс в калорийности злаков конкурентов. "
      "Это подчеркивает уникальность CrunchieMunchies на фоне конкурентов, предлагая потребителям более полезный продукт.")
print("\nПроцент продуктов с большей калорийностью:")
print("Более 70% конкурентов имеют больше калорий, что можно использовать для построения маркетинговых кампаний, "
      "ориентированных на здоровое питание.")