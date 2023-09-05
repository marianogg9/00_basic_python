class RobotFactory:
    name: str
    identifier: int
    color: str
    type: str

    global robot_list
    robot_list = []

    def __init__(self,name,identifier,color,type):
        self.name = name
        self.identifier = identifier
        self.color = color
        self.type = type

    def new_robot(name,identifier,color,type):
        robot = RobotFactory(name,identifier,color,type)
        robot_list.append([robot.identifier + " - " + robot.name + " (" + robot.type + ") " + "- " + robot.color])
        return robot

    def robots_created():
        return robot_list

    def talk(self, message):
        return message

    def walk(self, message):
        return message

    def create_fighter_bots(num):
        for i in range(num):
            RobotFactory.new_robot(name="scythe"+str(i), identifier="0000"+str(i), color="metallic", type="fighter")
        return robot_list

class FighterRobot(RobotFactory):
    type: str = "fighter"

    def fight(self):
        return "Fight in progress ..."

    def talk(self):
        message = super().talk("Hello Sir, Please show me your ID")
        return message

    def walk(self):
        return super().walk("I am walking safely")

class CookRobot(RobotFactory):
    type: str = "cook"

    def cook(self):
        return "Cooking in progress"

    def talk(self):
        message = super().talk("What can I cook for you today?")
        return message

    def walk(self):
        return super().walk("I am walking slowly")

class FireFighterRobot(RobotFactory):
    type: str = "firefighter"

    def put_out_fire(self):
        return "Putting out the fire ..."

    def talk(self):
        message = super().talk("We are there to protect you. Please stay behind the line")
        return message

    def walk(self):
        return super().walk("I am walking fast")