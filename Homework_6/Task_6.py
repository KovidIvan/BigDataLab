number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
operator = input("Введите оператор (+, -, /, *): ")
match operator:
    case "+":
        result = number_1 + number_2
        print(f"Результат: {result}")
    case "-":
        result = number_1 - number_2
        print(f"Результат: {result}")
    case "*":
        result = number_1 * number_2
        print(f"Результат: {result}")
    case "/":
        result = number_1 / number_2
        print(f"Результат: {result}")