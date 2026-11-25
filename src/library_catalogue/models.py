from dataclasses import dataclass


@dataclass
class Book():
    id: str
    title: str
    category: str
    year: int
    author: str
    #isbn: str изменить на другой параметр
    