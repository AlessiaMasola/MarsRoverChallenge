from Plateau import Plateau
from Rover import Rover
    
# The program gets the imput from a text file and outputs the solution to the command line.
def main():

    cardinals = ["N", "S", "E", "W"]

    # Open the input file
    input = open('input.txt', "r")
    # The first line of the input is the plateau size
    plateau_size = map(int, input.readline().split())
    plateau = Plateau(plateau_size[0],plateau_size[1])

    # Keep reading the file until there is nothing left to read
    while 1: 
        # From this point in the file, each pair of consecutive lines 
        # Will be the position and instruction for a new rover.
        rover_position = input.readline().split()
        rover_instructions = input.readline().strip()

        if not rover_position or not rover_instructions:
            break

        # Check if the rover information is valid
        if (not(0 <= int(rover_position[0]) <= plateau.x) or not(0 <= int(rover_position[1]) <= plateau.y)):
            print "The rover is out of the plateau!"
            continue
        elif (rover_position[2] not in cardinals):
            print "The direction of the rover is not valid!"
            continue
        
        # Process the position and instructions information, and dislplay the rover's final position
        rover = Rover(int(rover_position[0]), int(rover_position[1]), rover_position[2])
        rover.rover_move(plateau, rover_instructions)
        
        print rover.x, rover.y, rover.direction

    # Close the input file
    input.close()

if __name__ == "__main__":
    main()
