from abc import ABC, abstractmethod
import logging
import re
from models.exceptions import ValidationError

class IPerson(ABC):

    @abstractmethod
    def info(self) -> None:
        pass

    @abstractmethod
    def get_passport(self) -> str:
        pass


class Person(IPerson):

    def __init__(self, name: str, age: int, passport: str):
        if age < 0:
            raise ValidationError("Вік не може бути від'ємним!")
        self.name = name
        self._age = age
        self._passport = None
        self.passport = passport

    @property
    def passport(self) -> str:
        return self._passport

    @passport.setter
    def passport(self, value: str):
        if not re.match(r"^[A-ZА-ЯІЇЄ]{2}\d{6}$", value, re.IGNORECASE):
            logging.error(f"Некоректний паспорт: {value}")
            raise ValidationError(
                f"Некоректний формат паспорта: '{value}'. Очікується 2 літери та 6 цифр."
            )
        self._passport = value.upper()

    def get_passport(self) -> str:
        return self._passport

    def info(self) -> None:
        logging.info(f"Людина: {self.name}, вік: {self._age}")
