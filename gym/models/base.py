from abc import ABC, abstractmethod
import logging
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
        self._passport = passport

    def get_passport(self) -> str:
        return self._passport

    def info(self) -> None:
        logging.info(f"Людина: {self.name}, вік: {self._age}")
