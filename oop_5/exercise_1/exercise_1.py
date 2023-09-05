# Create a script that creates a factory of robots
# Each robot has a name, an identifier and a color
# Each robot can walk
# Only Robots of type fighter can fight
# Only robots of type cook can cook
# Only robots of type firefighter know how to put out a fire
# Each robot can say one message when interacting with humans
# Fighter bots say "Hello Sir, Please show me your ID"
# Cook bots say "What can I cook for you today?"
# Firefighter bots say "We are there to protect you. Please stay behind the line"
# You need to use the oop concepts to complete this exercise

# --------- Create bots -----------
from models import RobotFactory

assert RobotFactory.new_robot(name="scythe", identifier="00001", color="metallic", type="cook")
assert RobotFactory.new_robot(name="de303", identifier="00002", color="red", type="cook")
assert RobotFactory.new_robot(name="de313", identifier="00003", color="red", type="fighter")
assert RobotFactory.new_robot(name="arm303", identifier="00004", color="red", type="firefighter")

# print(len(RobotFactory.robots_created()))
assert len(RobotFactory.robots_created()) == 4

# assert RobotFactory.new_robot(name="Arm303", identifier="00004", color="red", type="doctor") is False
assert len(RobotFactory.robots_created()) == 4


# We receive a special command and we want to be able to create an army of robots using create_fighter_bots(100)
# This should function should help us to create 100 fighter bots in the robot list with random names, identifier
# and the color metallic

assert RobotFactory.create_fighter_bots(100)
assert len(RobotFactory.robots_created()) == 104

# ---------- List bots created ----------
for robot in RobotFactory.robots_created():
  print(robot)

# Output expected:
# "00001 - Scythe (nanny) - metallic"
# "00002 - De303 (nanny) - red",
# "00003 - De313 (fighter) - red",
# "00004 - Arm303 (fighter) - red"

# Display the number of robots created with magic method
assert len(RobotFactory.robots_created()) == 104


# Now, we want to check that each bot is doing what it has been created for
# Before sending it to the customer

# Check if bot can walk and cook
cook_bot = RobotFactory.robots_created()[0]
assert cook_bot.identifier == "00001"
assert cook_bot.walk() == "I am walking slowly"
assert cook_bot.cook() == "Cooking in progress"

# Check if fighter can walk and fight
fighter_bot = RobotFactory.robots_created()[2]
assert fighter_bot.identifier == "00003"
assert fighter_bot.walk() == "I am walking safely"
assert fighter_bot.fight() == "Fight in progress ..."

# Check if firefighter can walk and put out a fire
fire_fighter_bot = RobotFactory.robots_created()[3]
assert fire_fighter_bot.identifier == "00004"
assert fire_fighter_bot.walk() == "I am walking fast"
assert fire_fighter_bot.put_out_fire() == "Putting out the fire ..."
