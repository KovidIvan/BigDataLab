from typing import Any

DEFAULT_RETURN_INDEX_BASE: float = 10.0

def calculate_overdue_fine(film_name: str, days_overdue: Any, fine_rate: float) -> tuple[float, float] | None:
    """
    Безопасно рассчитывает штраф индекс оборачиваемости.
    Функция пытается преобразовать days_overdue в float,вычисляет штраф и индекс. В случае ошибок преобразования, деления на ноль
    или неверного типа выводит текст и возвращает None.

    Args:
        film_name: Название фильма.
        days_overdue: Сырые данные о днях просрочки.
        fine_rate: Штраф за день просрочки.

    Returns:
        tuple[float, float] | None:
            - В случае успеха: кортеж (total_fine, return_index), где
              total_fine = numeric_days * fine_rate,
              return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days.
            - В случае ошибки: None.

    Обрабатываемые исключения:
        - ValueError: если days_overdue не удаётся преобразовать в float.
        - TypeError: если передан объект неподдерживаемого типа.
        - ZeroDivisionError: если days_overdue преобразуется в 0.
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{film_name}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_name}': {e}")
        return None

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_name}': {e}")
        return None

    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_name}': float division by zero")
        return None

    finally:
        print("--- Проверка транзакции возврата завершена ---")

if __name__ == "__main__":
    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
    calculate_overdue_fine("Matrix", 5, 1.5)

    calculate_overdue_fine("Inception", "пять", 2.0)

    calculate_overdue_fine("Avatar", 0, 2.5)

    calculate_overdue_fine("Interstellar", [3,], 3.0)