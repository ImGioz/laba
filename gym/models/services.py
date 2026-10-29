import logging
from models.exceptions import ValidationError

class Subscription:

    def __init__(self, owner: str, days: int, price: float):
        if days < 0 or price < 0:
            raise ValidationError("Дні та ціна не можуть бути від'ємними!")
        self.owner = owner
        self.days = days
        self._price = price
        self.visits = 0

    def visit(self) -> None:
        if self.days == 0:
            logging.warning("Абонемент закінчився!")
            return
        self.days -= 1
        self.visits += 1
        logging.info(
            f"Візит №{self.visits}, залишилось днів в абонементі: {self.days}"
        )

    def price_per_visit(self) -> float:
        if self.visits == 0:
            logging.warning("Візитів ще не було")
            return 0.0
        cost = self._price / self.visits
        logging.info(f"Ціна одного візиту: {cost:.0f} грн")
        return cost


class PremiumSubscription(Subscription):

    def __init__(self, owner: str, days: int, price: float, discount: float):
        super().__init__(owner, days, price)
        self.discount = discount

    def price_per_visit(self) -> float:
        if self.visits == 0:
            logging.warning("Візитів ще не було")
            return 0.0
        price = self._price * (1 - self.discount / 100)
        cost = price / self.visits
        logging.info(f"Ціна одного візиту зі знижкою: {cost:.0f} грн")
        return cost


class Workout:

    def __init__(self, name: str, exercises: dict):
        self.name = name
        self.exercises = exercises
        self.total_volume = 0.0

    @staticmethod
    def volume(sets: list) -> float:
        return sum(weight * reps for weight, reps in sets)

    def calculate(self) -> float:
        self.total_volume = 0.0
        for exercise, sets in self.exercises.items():
            vol = self.volume(sets)
            self.total_volume += vol
            logging.info(f"Вправа {exercise}: {vol:.0f} кг")
        logging.info(f"Загальний об'єм тренування: {self.total_volume:.0f} кг")
        return self.total_volume


class Equipment:

    def __init__(self, title: str, max_weight: float):
        self.title = title
        self.max_weight = max_weight
        self.busy = False

    def take(self, athlete_name: str) -> None:
        if self.busy:
            logging.warning(f"Тренажер {self.title} вже зайнятий!")
            return
        self.busy = True
        logging.info(f"{athlete_name} займає тренажер: {self.title}")

    def release(self) -> None:
        self.busy = False
        logging.info(f"Тренажер {self.title} вільний")

    def check_weight(self, weight: float) -> bool:
        if weight > self.max_weight:
            logging.warning(
                f"Забагато для {self.title}: максимум {self.max_weight} кг"
            )
            return False
        logging.info(
            f"Вага {weight} кг підходить для тренажера {self.title}"
        )
        return True
