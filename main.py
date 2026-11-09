
import timeit
from statistics import mean

from search_algorithms import (
    boyer_moore_search,
    kmp_search,
    rabin_karp_search,
)


# Алгоритми для порівняння
algorithms = {
    "Боєра-Мура": boyer_moore_search,
    "Кнута-Морріса-Пратта": kmp_search,
    "Рабіна-Карпа": rabin_karp_search,
    "Python str.find()": str.find,
}

# Читаємо статті
with open("стаття 1.txt", encoding="utf-8-sig") as file:
    text_1 = file.read()

with open("стаття 2.txt", encoding="utf-8-sig") as file:
    text_2 = file.read()

# Підрядки для пошуку
patterns = [
    "підібраний алгоритм пошуку",
    "))*",
    "Для найбільш ефективного використання",
    "1536"
]

articles = [
    ("Стаття 1", text_1),
    ("Стаття 2", text_2),
]

# ===== Пошук і вимірювання =====

for article_name, text in articles:

    print(f"\n========== {article_name} ==========")

    for pattern in patterns:

        print(f'\nПошук рядка: "{pattern}"')

        times = {}
        positions = {}
        all_measurements = {}

        for name, algorithm in algorithms.items():

            positions[name] = algorithm(text, pattern)

            # П'ять серій по п'ять запусків
            measurements = timeit.repeat(
                lambda: algorithm(text, pattern), repeat=5, number=5)

            # Час одного запуску в кожній серії, мс
            single_times = []

            for value in measurements:
                single_times.append(value / 5 * 1000)

            all_measurements[name] = single_times

            # Середній час одного пошуку
            avg_time = mean(single_times)
            times[name] = avg_time

        fastest_time = min(times.values())

        print(
            f"{'Алгоритм':25} {'Поз.':>7} {'Серія 1':>10} {'Серія 2':>10} {'Серія 3':>10} "
            f"{'Серія 4':>10} {'Серія 5':>10} {'Середнє':>10} {'x':>8}"
        )

        for name in algorithms:

            ratio = times[name] / fastest_time
            values = all_measurements[name]

            print(
                f"{name:25} {positions[name]:7} "
                f"{values[0]:10.4f} {values[1]:10.4f} {values[2]:10.4f} {values[3]:10.4f} "
                f"{values[4]:10.4f} {times[name]:10.4f} {ratio:7.2f}x"
            )
