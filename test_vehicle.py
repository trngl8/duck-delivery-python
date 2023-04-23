import unittest
from models import Vehicle


class TestVehicle(unittest.TestCase):

    def test_move(self):
        v8 = Vehicle('camaro', 8)
        v8.move(3)
        self.assertEqual(25, v8.position)


# entry point
if __name__ == '__main__':
    unittest.main()
