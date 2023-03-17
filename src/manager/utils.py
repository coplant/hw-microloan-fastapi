from enum import Enum


class Status(Enum):
    process = (1, "В обработке")
    approved = (2, "Одобрено")
    rejected = (3, "Отклонено")
