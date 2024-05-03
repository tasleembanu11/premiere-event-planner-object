from abc import ABC, abstractmethod
import sys
class EventPlanner(ABC):
    def __init__(self):
        self.events = {}

    @abstractmethod
    def add_event(self):
        pass

    @abstractmethod
    def view_events(self):
        pass

    @abstractmethod
    def update_event(self, event_name):
        pass

    @abstractmethod
    def delete_event(self, event_name):
        pass

class CelebrityManager:
    def __init__(self):
        self.celebrity_list = ["feroze khan", "wahaj ali", "hania amir", "salman khan","sharukh khan","yash","punithraj kumar","prabhas","darshan","sudeep"]

    def add_celebrity(self, celebrity_name):
        self.celebrity_list.append(celebrity_name)
        print(f"Celebrity '{celebrity_name}' added successfully.")

    def update_celebrity(self, old_name, new_name):
        if old_name in self.celebrity_list:
            index = self.celebrity_list.index(old_name)
            self.celebrity_list[index] = new_name
            print(f"Celebrity '{old_name}' updated to '{new_name}' successfully.")
        else:
            print(f"Celebrity '{old_name}' not found.")
    def delete_celebrity(self, celebrity_name):
                if celebrity_name in self.celebrity_list:
                    self.celebrity_list.remove(celebrity_name)
                    print(f"Celebrity '{celebrity_name}' deleted successfully.")
                else:
                    print(f"Celebrity '{celebrity_name}' not found.")

    def view_celebrities(self):
        if not self.celebrity_list:
            print("No celebrities found.")
        else:
            print("Celebrity List:")
            for index, name in enumerate(self.celebrity_list, 1):
                print(f"{index}. {name}")

class EventPlannerImpl(EventPlanner):
    def __init__(self):
        super().__init__()
        self.celebrity_manager = CelebrityManager()

    def welcome_message(self):
        print("Welcome to the Event Planner!")

    def show_options(self):
        print("Options:")
        print("1. Add Event")
        print("2. View Events")
        print("3. Update Event")
        print("4. Delete Event")
        print("5. Add Celebrity")
        print("6. Update Celebrity")
        print("7. View Celebrities")
        print("8. Delete Celebrity")
        print("9.Exit")

    def handle_user_choice(self, choice):
        if choice == "1":
            self.add_event()
        elif choice == "2":
            self.view_events()
        elif choice == "3":
            event_to_update = input("Enter the name of the event you want to update: ")
            self.update_event(event_to_update)
        elif choice == "4":
            event_to_delete = input("Enter the name of the event you want to delete: ")
            self.delete_event(event_to_delete)
        elif choice == "5":
            celebrity_name = input("Enter the name of the celebrity you want to add: ")
            self.celebrity_manager.add_celebrity(celebrity_name)
        elif choice == "6":
            old_name = input("Enter the name of the celebrity you want to update: ")
            new_name = input("Enter the new name: ")
            self.celebrity_manager.update_celebrity(old_name, new_name)
        elif choice == "7":
            self.celebrity_manager.view_celebrities()
        elif choice == "8":
            celebrity_to_delete = input("Enter the name of the celebrity you want to delete: ")
            self.celebrity_manager.delete_celebrity(celebrity_to_delete)
        elif choice == "9":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

    def add_event(self):
        event_name = input("Enter the event name: ")
        event_date = input("Enter the event date (MM/DD/YYYY): ")
        event_guests = int(input("Enter the number of celebrities: "))

        selected_celebrities = []
        print("Choose celebrities from the list:")
        self.celebrity_manager.view_celebrities()
        for i in range(event_guests):
            choice = int(input(f"Choose celebrity {i+1} (1-{len(self.celebrity_manager.celebrity_list)}): "))
            if 1 <= choice <= len(self.celebrity_manager.celebrity_list):
                selected_celebrities.append(self.celebrity_manager.celebrity_list[choice - 1])
            else:
                print("Invalid celebrity number. Please try again.")
                return

        self.events[event_name] = {"date": event_date, "guests": selected_celebrities}
        print(f"Event '{event_name}' added successfully.")

    def view_events(self):
        if not self.events:
            print("No events found.")
        else:
            print("Upcoming Events:")
            for event, details in self.events.items():
                print(f"Event: {event}")
                print(f"Date: {details['date']}")
                print("Celebrities:")
                for celebrity in details['guests']:
                    print(celebrity)
                print("-" * 2)

    def update_event(self, event_name):
        if event_name in self.events:
            print(f"Updating event '{event_name}':")
            self.add_event()  # Reusing add_event() to update
            del self.events[event_name]
            print(f"Event '{event_name}' updated successfully.")
        else:
            print(f"Event '{event_name}' does not exist.")

    def delete_event(self, event_name):
        if event_name in self.events:
            del self.events[event_name]
            print(f"Event '{event_name}' deleted successfully.")
        else:
            print(f"Event '{event_name}' does not exist.")

# Example usage:
planner = EventPlannerImpl()
planner.welcome_message()

while True:
    planner.show_options()
    choice = input("Enter your choice: ")
    planner.handle_user_choice(choice)
