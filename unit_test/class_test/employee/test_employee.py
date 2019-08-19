import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_salary = Employee("Ahmad Irfan", "Mohammad Shukri", 65000)

    def test_given_default_raise(self):
        self.my_salary.give_raise()
        self.assertEqual(self.my_salary.salary, 70000)
    
    def test_given_custom_raise(self):
        self.my_salary.give_raise(10000)
        self.assertEqual(self.my_salary.salary, 75000)

if __name__ == '__main__':
    unittest.main()