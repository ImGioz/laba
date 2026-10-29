import unittest
from models.exceptions import ValidationError
from models.users import Athlete, Trainer


class TestGymSystem(unittest.TestCase):

    def test_bmi_calculation(self):
        athlete = Athlete("Гоша", 20, "АБ123456", 70.0, 175.0)
        expected_bmi = 70.0 / (1.75**2)
        self.assertAlmostEqual(athlete.bmi(), expected_bmi, places=2)

    def test_trainer_private_salary(self):
        trainer = Trainer("Олег", 30, "CD654321", "Фітнес", salary=1500.0)
        self.assertEqual(trainer.salary, 1500.0)

        trainer.raise_salary(500.0)
        self.assertEqual(trainer.salary, 2000.0)

        with self.assertRaises(ValidationError):
            trainer.raise_salary(-100.0)


if __name__ == "__main__":
    unittest.main()
