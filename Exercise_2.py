from typing import Callable

def generator_numbers(text: str):
    
    for word in text.split():
        if word.isdigit() or word.replace('.', '', 1).isdigit():  # Перевірка, чи є слово числом
            yield float(word)

def sum_profit(text: str, operation: Callable[[str], float]) -> float:
    return sum(operation(text))