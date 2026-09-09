MAX_RENTAL_BATCH_LIMIT: float = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, discount: float = 0.0) -> tuple[float, bool]:
    """
    Рассчитывает итоговую стоимость аренды фильмов с учётом скидки, проверяет превышение максимального лимита автоодобрения.
    quantity: Количество дисков в партии.
    rental_rate: Стоимость аренды одного диска.
    discount: Размер скидки в десятых.
    По умолчанию скидки нет (0.0).

    Returns:
        tuple[float, bool]:
            final_sum (float): Итоговая сумма партии.
            is_limit_exceeded (bool): True если final_sum превышает лимит.
    """
    final_sum = quantity * rental_rate * (1 - discount)
    final_sum = round(final_sum, 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded

films = [
    ("Academy Dinosaur", 30, 2.99, 0.0),
    ("Affair Prejudice", 40, 4.99, 0.1),
    ("Agent Truman", 10, 1.99, 0.0),
    ("African Egg", 50, 3.50, 0.2),
]
print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
for i, (name, qty, rate, disc) in enumerate(films, start=1):
    total, exceeded = calculate_rental_batch(qty, rate, disc)
    print(f"Партия {i} ({name}): Сумма {total}$. Превышение лимита: {exceeded}")