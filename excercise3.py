class Book:
    def __init__(self, isbn, title, authors, production_price):
        self._isbn = isbn
        self._title = title
        self._authors = authors
        self._production_price = production_price

    def __repr__(self):
        return f"Book(ISBN={self._isbn}, title={self._title}, authors={self._authors}, production_price={self._production_price})"

    # getters
    def get_isbn(self):
        return self._isbn

    def get_title(self):
        return self._title

    def get_authors(self):
        return self._authors

    def get_production_price(self):
        return self._production_price

    # setters
    def set_title(self, title):
        self._title = title

    def set_authors(self, authors):
        self._authors = authors

    def set_production_price(self, production_price):
        self._production_price = production_price

    def get_purchase_price(self):
        return self._production_price * 2


class ResearchBook(Book):
    def __init__(self, isbn, title, authors, production_price, field):
        super().__init__(isbn, title, authors, production_price)
        self._field = field

    def __repr__(self):
        return f"ResearchBook(ISBN={self.get_isbn()}, title={self.get_title()}, authors={self.get_authors()}, production_price={self.get_production_price()}, field={self._field})"

    # getter
    def get_field(self):
        return self._field

    # setter
    def set_field(self, field):
        self._field = field


class ChildrenBook(Book):
    def __init__(
        self, isbn, title, authors, production_price, age_limit, profit_percentage
    ):
        super().__init__(isbn, title, authors, production_price)
        self._age_limit = age_limit
        self._profit_percentage = profit_percentage

    def __repr__(self):
        return f"ChildrenBook(ISBN={self.get_isbn()}, title={self.get_title()}, authors={self.get_authors()}, production_price={self.get_production_price()}, age_limit={self._age_limit}, profit_percentage={self._profit_percentage})"

    # getters
    def get_age_limit(self):
        return self._age_limit

    def get_profit_percentage(self):
        return self._profit_percentage

    # setters
    def set_age_limit(self, age_limit):
        self._age_limit = age_limit

    def set_profit_percentage(self, profit_percentage):
        self._profit_percentage = profit_percentage

    def get_purchase_price(self):
        return self._production_price + (
            self._production_price * self._profit_percentage / 100
        )


# question 2
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return math.sqrt(self.x**2 + self.y**2) < math.sqrt(
            other.x**2 + other.y**2
        )

    def __le__(self, other):
        return self == other or self < other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # question 3


# 10
class Person:
    def __init__(self, first_name, last_name, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year


# 11
from dataclasses import dataclass


@dataclass
class PersonDC:
    first_name: str
    last_name: str
    birth_year: int


# 12
person_1 = Person("John", "Doe", 1990)
person_2 = Person("John", "Doe", 1990)
# 13
person_dc_1 = PersonDC("John", "Doe", 1990)
person_dc_2 = PersonDC("John", "Doe", 1990)
