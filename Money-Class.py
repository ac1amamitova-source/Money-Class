class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    # Строковые представления
    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    # Операторы сравнения
    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __gt__(self, other):
        return self.amount > other.amount

    # Арифметические операции
    def __add__(self, other):
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, other):
        return Money(self.amount * other.amount, self.currency)


# Создаём экземпляры класса
money1 = Money(100, "сом")
money2 = Money(50, "сом")
money3 = Money(100, "сом")
money4 = Money(200, "сом")

# Проверяем строковые представления
print("=== Строковые представления ===")
print(money1)
print(repr(money2))

# Проверяем сравнения
print("\n=== Операторы сравнения ===")
print("money1 == money3:", money1 == money3)
print("money2 < money1:", money2 < money1)
print("money4 > money1:", money4 > money1)

# Проверяем арифметические операции
print("\n=== Арифметические операции ===")
print("Сложение:", money1 + money2)
print("Вычитание:", money1 - money2)
print("Умножение:",money1*money2)