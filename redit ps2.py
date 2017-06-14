# Enter your code for RectangularRoom in this box
class RectangularRoom(object):
    """
   A RectangularRoom represents a rectangular region containing clean or dirty
   tiles.
 
   A room has a width and a height and contains (width * height) tiles. At any
   particular time, each of these tiles is either clean or dirty.
   """
    def __init__(self, width, height):
        """
       Initializes a rectangular room with the specified width and height.
 
       Initially, no tiles in the room have been cleaned.
 
       width: an integer > 0
       height: an integer > 0
       """
        self.width = width
        self.height = height
        self.clean = []
   
    def cleanTileAtPosition(self, pos):
        """
       Mark the tile under the position POS as cleaned.
 
       Assumes that POS represents a valid position inside this room.
 
       pos: a Position
       """
        x = math.floor(pos.x)
        y = math.floor(pos.y)
        if (x, y) in self.clean:
            return self.clean
        else:
            self.clean.append((x,y))
            return self.clean
       
    def isTileCleaned(self, m, n):
        """
       Return True if the tile (m, n) has been cleaned.
 
       Assumes that (m, n) represents a valid tile inside the room.
 
       m: an integer
       n: an integer
       returns: True if (m, n) is cleaned, False otherwise
       """
        posX = math.floor(m)
        posY = math.floor(n)
        pos = (posX, posY)
 
        if pos in self.clean:
            return True
        else:
            return False
   
    def getNumTiles(self):
        """
       Return the total number of tiles in the room.
 
       returns: an integer
       """
        return self.width * self.height
       
 
    def getNumCleanedTiles(self):
        """
       Return the total number of clean tiles in the room.
 
       returns: an integer
       """
        return len(self.clean)
   
    def getRandomPosition(self):
        """
       Return a random position inside the room.
 
       returns: a Position object.
       """
        randX = random.choice(range(self.width))
        randY = random.choice(range(self.height))
        return Position(randX, randY)
 
    def isPositionInRoom(self, pos):
        """
       Return True if pos is inside the room.
 
       pos: a Position object.
       returns: True if pos is in the room, False otherwise.
       """
        if pos.x < self.width and pos.x >= 0:
            if pos.y < self.height and pos.y >= 0:
                return True
 
        else:
            return False
        
# Enter your code for RectangularRoom (from the previous problem)
#  and Robot in this box
class RectangularRoom(object):
    """
   A RectangularRoom represents a rectangular region containing clean or dirty
   tiles.

   A room has a width and a height and contains (width * height) tiles. At any
   particular time, each of these tiles is either clean or dirty.
   """
    def __init__(self, width, height):
        """
       Initializes a rectangular room with the specified width and height.

       Initially, no tiles in the room have been cleaned.

       width: an integer > 0
       height: an integer > 0
       """
        self.width = width
        self.height = height
        self.clean = []

    def cleanTileAtPosition(self, pos):
        """
       Mark the tile under the position POS as cleaned.

       Assumes that POS represents a valid position inside this room.

       pos: a Position
       """
        x = math.floor(pos.x)
        y = math.floor(pos.y)
        if (x, y) in self.clean:
            return self.clean
        else:
            self.clean.append((x,y))
            return self.clean

    def isTileCleaned(self, m, n):
        """
       Return True if the tile (m, n) has been cleaned.

       Assumes that (m, n) represents a valid tile inside the room.

       m: an integer
       n: an integer
       returns: True if (m, n) is cleaned, False otherwise
       """
        posX = math.floor(m)
        posY = math.floor(n)
        pos = (posX, posY)

        if pos in self.clean:
            return True
        else:
            return False

    def getNumTiles(self):
        """
       Return the total number of tiles in the room.

       returns: an integer
       """
        return self.width * self.height


    def getNumCleanedTiles(self):
        """
       Return the total number of clean tiles in the room.

       returns: an integer
       """
        return len(self.clean)

    def getRandomPosition(self):
        """
       Return a random position inside the room.

       returns: a Position object.
       """
        randX = random.choice(range(self.width))
        randY = random.choice(range(self.height))
        return Position(randX, randY)

    def isPositionInRoom(self, pos):
        """
       Return True if pos is inside the room.

       pos: a Position object.
       returns: True if pos is in the room, False otherwise.
       """
        if pos.x < self.width and pos.x >= 0:
            if pos.y < self.height and pos.y >= 0:
                return True

        else:
            return False

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed=speed
        self.room=room
        self.pos=room.getRandomPosition()
        
        room.cleanTileAtPosition(self.pos)
        self.direction=random.randint(0,360)
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos.x=position.x
        self.pos.y=position.y

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction=direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
# Enter your code for Robot (from the previous problem)
#  and StandardRobot in this box
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed=speed
        self.room=room
        self.pos=room.getRandomPosition()

        room.cleanTileAtPosition(self.pos)
        self.direction=random.randint(0,360)
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos.x=position.x
        self.pos.y=position.y

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction=direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        pos = self.getRobotPosition()
        newpos = pos.getNewPosition(self.getRobotDirection(), self.speed)
        if self.room.isPositionInRoom(newpos):
            self.setRobotPosition(newpos)
            if not self.room.isTileCleaned(math.floor(newpos.getX()),math.floor(newpos.getY())):
                self.room.cleanTileAtPosition(newpos)
        else:
            self.setRobotDirection(random.randint(0,360))

# Enter your code for runSimulation in this box.
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    trialsList = []
    
    # Run num_trials amount of tests
    for trial in range(num_trials):
    #### Create room
        room = RectangularRoom(width,height)
        botList = []
    #### Create bots and add them to the botList
        for n in range(num_robots):
            botList.append(robot_type(room,speed))
            #print botList
        #anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        steps = 0
    #### While the room is not cleaned enough: Let all bots have another 'turn'
        while (1.0*room.getNumCleanedTiles()/room.getNumTiles()) <= min_coverage:
            #print room.getNumCleanedTiles()
            #print steps
            for bot in botList:
                #print bot
                #anim.update(room, bots)
                bot.updatePositionAndClean()
            steps += 1
    #### Add test to trialsList
        trialsList.append(steps)
        #anim.done()
    # return mean-value of all values in trialsList
    return float(sum(trialsList)) / len(trialsList)

# Enter your code for Robot and RandomWalkRobot in this box
class Robot(object):
    """
    Represents a robot cleaning a particular room.
 
    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.
 
    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.
 
        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.position = room.getRandomPosition()
        self.direction = random.randint(0, 359)
        self.room = room
        self.speed = speed
        room.cleanTileAtPosition(self.position)
 
    def getRobotPosition(self):
        """
        Return the position of the robot.
 
        returns: a Position object giving the robot's position.
        """
        return self.position
   
    def getRobotDirection(self):
        """
        Return the direction of the robot.
 
        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
 
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.
 
        position: a Position object.
        """
        self.position = position
 
    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.
 
        direction: integer representing an angle in degrees
        """
        self.direction = direction
 
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.
 
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
 
# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.
 
        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        if self.room.isPositionInRoom(self.position.getNewPosition(self.direction, self.speed)):
            self.position = self.position.getNewPosition(self.direction, self.speed)
            self.room.cleanTileAtPosition(self.position)
        self.direction = random.randint(0, 359)
   