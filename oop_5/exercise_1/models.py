class Robot:
    name: str
    identifier: int
    color: str
    type: str

    def __init__(self,name,identifier,color,type):
        self.name = name
        self.identifier = identifier
        self.color = color
        self.type = type
    
    def talk(self, message):
        return message

    def walk(self,message):
        if self.type == "fighter":
            message = "I am walking safely"
        else:
            if self.type == "cook":
                message = "I am walking slowly"
            else:
                message = "I am walking fast"
        return message

class RobotFactory:
    
    robots_created = []

    @classmethod # self is not needed
    def new_robot(cls,name,identifier,color,type):
        # strategy
        try:
            types = {"cook": CookRobot, "fighter": FighterRobot, "firefighter": FireFighterRobot}
            robot_class = types[type]

            robot = robot_class(name,identifier,color,type)
        except KeyError:
            return False

        cls.robots_created.append(robot) # robots_created is now a property of the class
        # add conditional exception for not allowed values
        return robot

    @classmethod
    def create_fighter_bots(cls,num):
        print("num:",num)
        for i in range(num):
            RobotFactory.new_robot(name="scythe"+str(i), identifier="0000"+str(i), color="metallic", type="fighter")
        return cls.robots_created
    
    # def __str__(self):
    #     # message = concatenation of wanted properties of the object
    #     return message

class FighterRobot(Robot):
    type: str = "fighter"

    def fight(self):
        return "Fight in progress ..."

    def talk(self):
        message = super().talk("Hello Sir, Please show me your ID")
        return message

    def walk(self):
        return super().walk("I am walking safely")

class CookRobot(Robot):
    type: str = "cook"

    def cook(self):
        return "Cooking in progress"

    def talk(self):
        message = super().talk("What can I cook for you today?")
        return message

    def walk(self):
        return super().walk("I am walking slowly")

class FireFighterRobot(Robot):
    type: str = "firefighter"

    def put_out_fire(self):
        return "Putting out the fire ..."

    def talk(self):
        message = super().talk("We are there to protect you. Please stay behind the line")
        return message

    def walk(self):
        return super().walk("I am walking fast")