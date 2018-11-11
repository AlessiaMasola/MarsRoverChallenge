import unittest
from main import main
from Plateau import Plateau
from Rover import Rover

class TestRoverMethods(unittest.TestCase):


    def test_rotate_left(self):
        roverTest = Rover(1, 2, "W")
        self.assertEqual(roverTest.rotateL(), "S")
    
    def test_rotate_right(self):
        roverTest = Rover(3, 2, "S")
        self.assertEqual(roverTest.rotateR(), "W")

    def test_move_rover(self):
        instructionsTest = "LMLMLMLMM"
        instructionsTest1 = "LMLMLMLMP"
        instructionsTest2 = "LMMMMMMMMMMMMMMMMMMMMMMM"
        roverMoveTest = Rover(1, 2, "N")
        plateauTest = Plateau(5, 5)
        self.assertEqual(roverMoveTest.rover_move(plateauTest, instructionsTest), (1, 3, "N"))
        self.assertEqual(roverMoveTest.rover_move(plateauTest, instructionsTest1), "Invalid instruction!")
        self.assertEqual(roverMoveTest.rover_move(plateauTest, instructionsTest2), "The plateau is too small for your instructions! :(")

    def test_set_rover_position(self):
        roverTest = Rover(0, 0, "N")
        plateauTest = Plateau(5, 5)
        self.assertEqual(roverTest.set_rover_position(plateauTest, 4, 2, "W"), (4, 2, "W"))
        self.assertEqual(roverTest.set_rover_position(plateauTest, 7, 3, "E"), "Cannot set the position of the rover outside the plateau!")
        self.assertEqual(roverTest.set_rover_position(plateauTest, 2, 3, "A"), "Invalid direction!")

    def test_get_rover_position(self):
        roverTest = Rover(1, 5, "S")
        self.assertEqual(roverTest.get_rover_position(), (1, 5, "S"))

if __name__ == '__main__':
    unittest.main()