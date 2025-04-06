import csv
import json
from pathlib import Path
from mtr.function import min_route, fee_calculate, MTR_map
from mtr.admin import admin


# User class for managing user information and authentication.
class User:
    def __init__(self, username: str, password: str = None, gender: str = None, age: int = None):
        self.username = username
        self.password = password
        self.gender = gender
        self.age = age

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
        # create a json file and upload several existing users for demonstration for login
        # Simple default users with gender and age
        users = {
            "louis": {"password": "12345", "gender": "male", "age": 30},
            "gongda": {"password": "54321", "gender": "male", "age": 40}
        }
        # write the dictionary into a json file
        path = Path('data/users.json')
        contents = json.dumps(users, indent=4)
        path.write_text(contents)

    @staticmethod
    def register():
        # define the register function
        print("\n** Register **")
        path = Path('data/users.json')
        # If file does not exist, create an empty dict
        if path.exists():
            contents = path.read_text()
            users = json.loads(contents)
        else:
            users = {}

        while True:
            username = input("Enter a new username: ").strip()
            # Check if username already exists
            if username in users:
                print("Username already exists. Please try a different username.")
                continue
            password = input("Enter a password: ").strip()
            # New: ask for gender and age
            # Print an error message when the input is invalid and let user re-enter the gender
            while True:
                gender = input("Enter your gender (m/f): ").strip().lower()  # simple english comment
                if gender not in ["m", "f"]:
                    print("Invalid gender. Please try again.")
                    continue
                else:
                    break

            # Print an error message when the input is invalid and let user re-enter the age
            while True:
                try:
                    age = int(input("Enter your age: ").strip())  # simple english comment
                    break
                except ValueError:
                    print("Invalid age. Please enter a number.")
                    continue

            # Store user info into the dictionary
            users[username] = {
                "password": password,
                "gender": gender,
                "age": age
            }

            # load into the json file
            path.write_text(json.dumps(users, indent=4))
            print("Registration successful! You can now log in.")
            break  # finish registering

    @staticmethod
    def log_in():
        print("\n** Log In **")
        path = Path('data/users.json')
        contents = path.read_text()
        users = json.loads(contents)

        while True:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            # Check that the username and password match
            if username in users and users[username]["password"] == password:
                if username == "admin":
                    print("Admin login successfully!")
                    admin()
                    exit()

                print("Login successful!")
                print("Let's begin your planning 🚊 ")
                user_info = users[username]
                # Pass gender and age to User instance
                return User(username, password, user_info.get("gender"), user_info.get("age"))
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


def update_station_stats(station_id: str, gender: str, age: int):
    """
    Update station stats for given station_id.
    Increase the count of the given gender and age by 1.
    If station or the age entry does not exist, create it.
    """
    path = Path('data/stations.json')
    if path.exists():
        data = json.loads(path.read_text())
    else:
        data = {"stations": []}

    # Look for the station
    station_found = False
    for station in data["stations"]:
        if station.get("station_id") == station_id:
            station_found = True
            # Ensure stats exist for both genders
            if "stats" not in station:
                station["stats"] = {"male": {}, "female": {}}
            if gender not in station["stats"]:
                station["stats"][gender] = {}
            # Age is stored as string key
            age_key = str(age)
            if age_key in station["stats"][gender]:
                station["stats"][gender][age_key] += 1
            else:
                station["stats"][gender][age_key] = 1
            break

    if not station_found:
        # Create new station record
        new_station = {
            "station_id": station_id,
            "stats": {
                "male": {},
                "female": {}
            }
        }
        # Initialize count for the given gender and age
        new_station["stats"][gender][str(age)] = 1
        data["stations"].append(new_station)

    path.write_text(json.dumps(data, indent=4))


# Main loop
def main():
    # print welcome message
    User.welcome_message()

    user = None  # initialize user variable
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
    while True:
        # Prompt the user to input starting and destination stations.
        print(f'\n--------------Planning--------------')
        start_station = input("Enter starting station: ").strip()
        end_station = input("Enter destination station: ").strip()

        # Print an error message when the input stations are not in the map
        # or the starting station and destination station are the same
        map_list = list(MTR_map.keys())
        if start_station not in map_list or end_station not in map_list:
            print(f'\n*** WARNING ***: ')
            print('Invalid stations, please enter existing stations.')
            continue
        if start_station == end_station:
            print(f'\n*** WARNING ***: ')
            print('Starting and destination station cannot be the same, please enter different stations.')
            continue

        # Calculate the optimal route using the imported min_route function.
        # The function returns a tuple containing the distance and the route (list of stations).
        distance, path = min_route(start_station, end_station)
        print(f'\n---Results---')
        print("Path:", " -> ".join(path))

        # Calculate the fee for the journey using the imported fee_calculate function.
        fee = fee_calculate(start_station, end_station)
        print(f'Calculated fee: {fee}')

        # Create a new journey record.
        journey = Journey(user, start_station, end_station, path, distance, fee)

        # Log the journey details to a CSV file.
        log_journey(journey)

        # Update station statistics for starting and destination stations using the user's gender and age.
        update_station_stats(start_station, user.gender, user.age)
        update_station_stats(end_station, user.gender, user.age)

        # Update the total expense with the fee for the current journey.
        total_expense += fee

        # Ask if the user wants to plan another journey.
        while True:
            more = input("Do you want to plan another journey? (y/n): ").strip().lower()
            if more not in ["y", "n"]:
                print(f'\n*** WARNING ***: ')
                print("Invalid input. Please try again.")
                continue  # re-prompt the user for input

            if more == 'y':
                break  # exit the current while loop and continue planning journeys
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
