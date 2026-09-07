import time
from typing import Callable, Any, List, Dict, Union
import functools

PERFORMANCE_LOG_PREFIX: str = "[PERF_LOG]"
TIME_DECIMALS: int = 8

def performance_logger(func: Callable) -> Callable:
    """
    Декоратор для замера времени выполнения и логирования.
    Args:
        func (Callable): Целевая функция.
    Returns:
        Callable: Обёрнутая функция
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {elapsed:.{TIME_DECIMALS}f} сек.")
        return result
    return wrapper

@performance_logger
def get_sorted_report(sales_data: List[Dict[str, Union[str, float]]]) -> List[Dict[str, Union[str, float]]]:
    """
    Сортирует категории по убыванию выручки.
    Args:
        sales_data (List[Dict[str, Union[str, float]]]): Список словарей, каждый содержит ключи category и total_sales.
    Returns:
        List[Dict[str, Union[str, float]]]: Отсортированный по убыванию total_sales список.
    """
    return sorted(sales_data, key=lambda item: item["total_sales"], reverse=True)

if __name__ == "__main__":
    test_sets = [
        [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55}
        ],
        [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00}
        ],
        [
            {"category": "Drama", "total_sales": 500.00}
        ]
    ]

    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")
    for idx, data in enumerate(test_sets, start=1):
        print(f"--- ТЕСТ {idx} ---")
        sorted_data = get_sorted_report(data)
        print("Топ категорий по выручке:")
        for rank, item in enumerate(sorted_data, start=1):
            print(f"{rank}. {item['category']}: {item['total_sales']}")
        print()  
