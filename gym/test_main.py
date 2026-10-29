unittest з імпортом unittest
from models.exceptions import ValidationError
from models.services import PremiumSubscription, Workout
from models.users import Athlete


class TestGymSystem(unittest.TestCase):

    def test_bmi_calculation(self):
        athlete = Athlete("Іван", 20, "АБ123456", 70.0, 175.0)
        expected_bmi = 70.0 / (1.75**2)
        self.assertAlmostEqual(athlete.bmi(), expected_bmi, places=2)

    def test_invalid_passport_raises_error(self):
        with self.assertRaises(ValidationError):
            Athlete("Тест", 20, "12345Некоректний", 70.0, 175.0)

    def test_workout_volume(self):
        workout = Workout("Тест", {"Присідання": [[100.0, 5], [100.0, 5]]})
        self.assertEqual(workout.calculate(), 1000.0)


if __name__ == "__main__":
    unittest.main()
