from enum import Enum


class Roles(Enum):
    admin = 100
    user = 0
    operator = 1
    manager = 2
    accountant = 3


class Status(Enum):
    consideration = (1, "На рассмотрении")
    process = (2, "В обработке")
    approved = (3, "Одобрено")
    rejected = (4, "Отклонено")
