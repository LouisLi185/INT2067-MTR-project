import csv
from function import min_route, fee_caculate


# User class for managing user information and authentication.
class User:
    def __init__(self, username: str, password: str):
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

        path = Path('users.json')
        contents = json.dumps(users)
        path.write_text(contents)



    @staticmethod
    def register():
        print("\n** Register **")
        path = Path('users.json')
        contents = path.read_text()
        users = json.loads(contents)

        while True:
            username = input("Enter a new username: ").strip()
            password = input("Enter a password: ").strip()
            users[username] = password  # load into the dictionary

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
                return User(username)   # login successful, return
            else:
                print("Invalid username or password. Please try again.")


    @staticmethod
    def welcome_message():
        # print welcome message
        print("=" * 50)
        print("🚇  Welcome to the Metro Travel Planner  🚇".center(50))
        print("=" * 50)
        print("\nThis system allows you to register and log in to plan your metro journeys efficiently.")

    @staticmethod
    def default_users():
        """create a json file and upload several existing users for demonstration for login"""
        users = {
            "louis": "12345",
            "gongda": "54321"
        }

        path = Path('users.json')
        contents = json.dumps(users)
        path.write_text(contents)



    @staticmethod
    def register():
        print("\n** Register **")
        path = Path('users.json')
        contents = path.read_text()
        users = json.loads(contents)

        while True:
            username = input("Enter a new username: ").strip()
            password = input("Enter a password: ").strip()
            users[username] = password  # load into the dictionary

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
                return User(username)   # login successful, return
            else:
                print("Invalid username or password. Please try again.")



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


def main():
    # Initialize a sample user (this can be extended to a proper user database).
    user = User("admin", "password")

    # Prompt the user for login credentials.
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    # Check if the provided credentials are correct.
    if not user.authenticate(input_username, input_password):
        print("Authentication failed!")
        return
    print("Authentication successful!")

    total_expense = 0  # Variable to keep track of the total fee for the session.

    while True:
        # Prompt the user to input starting and destination stations.
        start_station = input("Enter starting station: ")
        end_station = input("Enter destination station: ")

        # Calculate the optimal route using the imported min_route function.
        # The function returns a tuple containing the distance and the route (list of stations).
        distance, path = min_route(start_station, end_station)
        print(f"Path:", " -> ".join(path))

        # Calculate the fee for the journey using the imported fee_caculate function.
        fee = fee_caculate(start_station, end_station)
        print(f"Calculated fee: {fee}")

        # Create a new journey record.
        journey = Journey(user, start_station, end_station, path, distance, fee)

        # Log the journey details to a CSV file.
        log_journey(journey)

        # Update the total expense with the fee for the current journey.
        total_expense += fee

        # Ask if the user wants to plan another journey.
        more = input("Do you want to plan another journey? (y/n): ")
        if more.lower() != 'y':
            break

    print(f"Total expense for this session: {total_expense}")


if __name__ == '__main__':
    main()
