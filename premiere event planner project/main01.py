#from abstractmethod import EventPlanner, CelebrityManager
from premiere_event_planner1 import EventPlannerImpl

# Example usage:
planner = EventPlannerImpl()
planner.welcome_message()

while True:
    planner.show_options()
    choice = input("Enter your choice: ")
    planner.handle_user_choice(choice)
