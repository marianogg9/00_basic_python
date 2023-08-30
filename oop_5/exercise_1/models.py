class RobotFactory:
    name: str
    identifier: int
    color: str
    type: str

    def new_robot(self,name,identifier,color,type):
        self.name = name
        self.identifier = identifier
        self.color = color
        self.type = type
    
    def talk(self,message):
        return message

    def walk(self, message):
        return message

    robots_created = []

    def create_fighter_bots(self,num,robots_created):
        for i in range(num):
            robots_created.append(self.new_robot(name="scythe"+i, identifier="0000"+i, color="metallic", type="fighter"))

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