import logging
from models.exceptions import ValidationError
from models.services import Equipment, PremiumSubscription, Workout
from models.users import Athlete, Trainer
from utils.file_reader import load_data_from_file

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("app.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)


def main():
    logging.info("=== Запуск програми ===")

    try:
        data = load_data_from_file("input_data.json")

        ath_d = data["athlete"]
        athlete = Athlete(
            ath_d["name"],
            ath_d["age"],
            ath_d["passport"],
            ath_d["weight"],
            ath_d["height"],
        )
        athlete.info()
        athlete.status()
        athlete.gain(ath_d["gain_kg"])

        wrk_d = data["workout"]
        workout = Workout(athlete.name, wrk_d["exercises"])
        workout.calculate()

        sub_d = data["subscription"]
        subscription = PremiumSubscription(
            athlete.name, sub_d["days"], sub_d["price"], sub_d["discount"]
        )
        for _ in range(sub_d["visits_to_make"]):
            subscription.visit()
        subscription.price_per_visit()

        eq_d = data["equipment"]
        equipment = Equipment(eq_d["title"], eq_d["max_weight"])
        equipment.take(athlete.name)
        equipment.check_weight(eq_d["check_weight_1"])
        equipment.check_weight(eq_d["check_weight_2"])
        equipment.release()

        tr_d = data["trainer"]
        trainer = Trainer(
            tr_d["name"], tr_d["age"], tr_d["passport"], tr_d["specialty"]
        )
        trainer.add_client(athlete.name)
        trainer.add_client(tr_d["second_client"])
        trainer.plan(workout)

    except ValidationError as ve:
        logging.error(f"Помилка валідації: {ve}")
    except Exception as ex:
        logging.critical(f"Незпередбачена помилка: {ex}")


if __name__ == "__main__":
    main()
