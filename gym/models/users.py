import logging
from models.base import Person
from models.exceptions import ValidationError


class Athlete(Person):

    def __init__(self, name: str, age: int, passport: str, weight: float, height: float):
        super().__init__(name, age, passport)
        if weight <= 0 or height <= 0:
            raise ValidationError("Зріст та вага повинні бути більше 0!")
        self.weight = weight
        self.height = height

    def info(self) -> None:
        logging.info(
            f"Спортсмен: {self.name}, вік: {self._age}, "
            f"вага: {self.weight:.1f} кг, зріст: {self.height:.0f} см"
        )

    def bmi(self) -> float:
        return self.weight / ((self.height / 100) ** 2)

    def status(self) -> str:
        index = self.bmi()
        result = (
            "недостатня вага"
            if index < 18.5
            else ("норма" if index < 25 else "надлишкова вага")
        )
        logging.info(f"{self.name}: ІМТ {index:.1f} ({result})")
        return result

    def gain(self, kilograms: float) -> None:
        self.weight += kilograms
        logging.info(
            f"Зміна ваги на {kilograms} кг. Нова вага: {self.weight:.1f} кг"
        )


class Trainer(Person):

    def __init__(self, name: str, age: int, passport: str, specialty: str):
        super().__init__(name, age, passport)
        self.specialty = specialty
        self.clients = []

    def info(self) -> None:
        logging.info(
            f"Тренер: {self.name}, вік: {self._age}, "
            f"спеціалізація: {self.specialty}, клієнтів: {len(self.clients)}"
        )

    def add_client(self, client_name: str) -> None:
        self.clients.append(client_name)
        logging.info(f"{self.name} бере в роботу клієнта: {client_name}")

    def plan(self, workout) -> None:
        logging.info(
            f"План від тренера {self.name} (Спеціалізація: {self.specialty}):"
        )
        for exercise, sets in workout.exercises.items():
            logging.info(f"   {exercise} — {len(sets)} підходів")
