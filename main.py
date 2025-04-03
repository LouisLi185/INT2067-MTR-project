import csv
import json
from pathlib import Path
from function import min_route, fee_calculate,MTR_map

# User class for managing user information and authentication.
class User:
    def __init__(self, username: str, password: str=None):
        self.username = username
        self.password = password

    def authenticate(self, username: str, password: str) -> bool:

        # Authenticates the user by comparing with the stored username and password.
        return self.username == username and self.password == password

    @staticmethod
    def welcome_message():
        # print welcome message
        print("=" * 50)
        print("🚇  Welcome to the Metro Travel Planner  🚇".center(50))
        print("=" * 50)
        print("\nThis system allows you to register and log in to plan your metro journeys efficiently.")

    @staticmethod
    def default_users():
        #create a json file and upload several existing users for demonstration for login
        users = {
            "louis": "12345",
            "gongda": "54321"
        }

        #write the dictionary into a json file
        path = Path('users.json')
        contents = json.dumps(users)
        path.write_text(contents)

    @staticmethod
    def register():
        #define the register function
        print("\n** Register **")
        path = Path('users.json')
        contents = path.read_text()
        users = json.loads(contents)

        while True:
            username = input("Enter a new username: ").strip()
            password = input("Enter a password: ").strip()
            users[username] = password  # load into the dictionary

            #load into the json file
            path = Path('users.json')
            contents = json.dumps(users)
            path.write_text(contents)

            print("Registration successful! You can now log in.")
            break  # finish registering

    @staticmethod
    def log_in():
        print("\n** Log In **")
        path = Path('users.json')
        contents = path.read_text()
        users = json.loads(contents)

        while True:
            username = input("Enter your username: ").strip()

            # If the username is "admin", log in directly without a password
            if username == "admin":
                print("Admin login successful! ")
                return User(username)

            password = input("Enter your password: ").strip()

            # Check that the username and password match
            if username in users and users[username] == password:
                print("Login successful!")
                print("Let's begin your planning 🚊 ")
                return User(username)   # login successful, return
            else:
                print(f"Invalid username or password. Please try again.\n")



# Journey class to store details about a single journey.
class Journey:
    def __init__(self, user: User, start: str, end: str, path: list, distance: float, fee: float):
        self.user = user
        self.start = start
        self.end = end
        self.path = path  # List of station names representing the journey path.
        self.distance = distance  # The computed distance from start to destination.
        self.fee = fee  # The travel fee for the journey.


# Function to log journey details into a CSV file.
def log_journey(journey: Journey):
    """
    Writes the journey details to a CSV file named 'journeys.csv'.
    The path is stored as a string with stations separated by '|'.
    """
    with open('data/journeys.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([journey.user.username,
                         journey.start,
                         journey.end,
                         '|'.join(journey.path),
                         journey.distance,
                         journey.fee])


#Main loop
def main():
    #print welcome message
    User.welcome_message()

    user = None        # initialize user variable
    while user is None:
        print("\n1. Log In")
        print("2. Register")
        choice = input("Choose an option (1/2): ").strip()

        if choice == "1":
            user = User.log_in()  # only when the login is successful will the loop be exited and the program will continue
        elif choice == "2":
            User.register()
        else:
            print(f"Invalid choice, please enter 1 or 2.\n")


    total_expense = 0  # Variable to keep track of the total fee for the session.
    map = []
    while True:
        # Prompt the user to input starting and destination stations.
        print(f'\n--------------Planning--------------')
        start_station = input("Enter starting station: ").strip()
        end_station = input("Enter destination station: ").strip()

        #Print an error message when the input stations are not in the map
        #or the starting station and destination station are the same
        for key in MTR_map.keys():
            map.append(key)
        if start_station not in map or end_station not in map:
            print(f'\n*** WARNING ***: ')
            print('Invalid stations, please enter existing stations.')
            continue
        else:
            if start_station == end_station:
                print(f'\n*** WARNING ***: ')
                print('Starting and destination station cannot be the same, please enter different stations.')
                continue

        # Calculate the optimal route using the imported min_route function.
        # The function returns a tuple containing the distance and the route (list of stations).
        distance, path = min_route(start_station, end_station)
        print(f'\n---Results---')
        print(f"Path:", " -> ".join(path))

        # Calculate the fee for the journey using the imported fee_calculate function.
        fee = fee_calculate(start_station, end_station)
        print(f'Calculated fee: {fee}')

        # Create a new journey record.
        journey = Journey(user, start_station, end_station, path, distance, fee)

        # Log the journey details to a CSV file.
        log_journey(journey)

        # Update the total expense with the fee for the current journey.
        total_expense += fee

        # Ask if the user wants to plan another journey.
        while True:
            try:
                more = input("Do you want to plan another journey? (y/n): ")
                if more not in ["y", "n"]:
                    raise ValueError
            except ValueError:
                print(f'\n*** WARNING ***: ')
                print("Invalid input. Please try again.")
                continue  # re-prompt the user for input

            if more == 'y':
                break  # exit the current while True and return to the main loop to continue the new journey
            else:
                print(f"\nTotal expense for this session: {total_expense}.")
                cash_back = (total_expense - 400) / 3
                if cash_back > 0:
                    print(f"Cash back is {cash_back:.2f}.")
                else:
                    print("Sorry, you don't have cash back")
                exit()


if __name__ == '__main__':
    main()