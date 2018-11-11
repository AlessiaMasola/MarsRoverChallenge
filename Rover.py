from Plateau import Plateau

class Rover(object):

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    # Rotate the direction of the rover 90 degrees to the left
    def rotateL(self):
        if (self.direction == "N"):
            self.direction = "W"
            return self.direction
        elif (self.direction == "E"):
            self.direction = "N"
            return self.direction
        elif (self.direction == "S"):
            self.direction = "E"
            return self.direction
        else:
            self.direction = "S"
            return self.direction

    # Rotate the direction of the rover 90 degrees to the right
    def rotateR(self):
        if (self.direction == "N"):
            self.direction = "E"
            return self.direction
        elif (self.direction == "E"):
            self.direction = "S"
            return self.direction
        elif (self.direction == "S"):
            self.direction = "W"
            return self.direction
        else:
            self.direction = "N"
            return self.direction

    # Move the rover forward of 1 unit
    def rover_move(self, plateau, instructions):
        for i in range(len(instructions)):
            if (instructions[i] == "L"):
                self.rotateL()
            elif (instructions[i] == "R"):
                self.rotateR()
            elif (instructions[i] == "M"):
                if ((self.direction == "N") and (self.y < plateau.y)):
                    self.y += 1
                elif ((self.direction == "E") and (self.x < plateau.x)):
                    self.x += 1
                elif ((self.direction == "S") and (self.y > 0)):
                    self.y -= 1
                elif ((self.direction == "W") and (self.x > 0)):
                    self.x -= 1
                else:
                    return "The plateau is too small for your instructions! :("
            else:
                return "Invalid instruction!"
        return (self.x, self.y, self.direction)
    
    # Setter
    def set_rover_position(self, plateau, x, y, d):
        if ((x <= plateau.x and x >= 0) and (y <= plateau.y and y >= 0) \
                    and (d == "N" or d == "S" or d == "E" or d == "W")):
            self.x = x
            self.y = y
            self.direction = d
            return (self.x, self.y, self.direction)
        elif (d != "N" and d != "S" and d != "E" and d != "W"):
            return "Invalid direction!"
        else:
            return "Cannot set the position of the rover outside the plateau!"
        
    # Getter
    def get_rover_position(self):
        return (self.x, self.y, self.direction)
    