
---

# 🚇 MTR Journey Planner with Cashback Incentives 🚇

A command-line application simulating a smart transit system for the MTR network with integrated cashback incentives.

---

## Project Overview

This application models the MTR network using a graph-based data structure where stations are represented as nodes and connections as weighted edges (representing travel costs). The system provides optimal route calculation and implements Hong Kong's public transport subsidy scheme.

### Features

- **Secure Authentication**: User login system to ensure authorized access.
- **Optimal Route Planning**: Uses Dijkstra's algorithm to compute the most efficient journey between stations.
- **Journey Logging**: Records trip details and total costs in CSV format.
- **Cashback Incentive System**: Implements Hong Kong's public transport subsidy scheme.
  - Adult Citizens spending over HK$400 per month with an Octopus Card qualify for a subsidy.
  - One-third of expenses exceeding HK$400 is reimbursed.
  - Maximum subsidy of HK$400 per account.

---

## Getting Started

### Prerequisites

- **Python Environment**: Ensure that Python is installed and properly configured on your system. It is recommended to use the latest stable release. For additional details, please refer to the [Python official website](https://python.org).

### Installation

1. **Download** the repository as a ZIP archive from GitHub.
2. **Extract** the contents of the ZIP file to a directory of your choice.
3. **Run** the application by executing the `main.py` file with your preferred Python interpreter.

### Usage

1. **Account Management**:
   - Upon startup, the system will prompt you to either log in or register a new account.
   - Follow the on-screen instructions to complete the chosen authentication process.

2. **Route Input**:
   - After a successful login, you will be asked to input the starting station and destination station.
   - Enter the station names in English exactly as they appear on the [MTR Map](https://www.mtr.com.hk/archive/en/services/routemap.pdf).
   - The system validates your input to ensure that the station names exist and are not duplicated.

3. **Route Calculation and Fee Estimation**:
   - When valid input is provided, the system calculates the shortest route between the specified stations.
   - The travel fee is computed based on the calculated path and is displayed along with the route details.

4. **Additional Journey Planning**:
   - After displaying the results, you can choose to plan another journey.
   - If you select **Yes**, you will be prompted for a new starting station and destination station. The travel fees for subsequent journeys will be appended to a CSV file and aggregated.
   - If you select **No**, the program terminates and the session summary is displayed.

5. **Program Termination**:
   - The application continues to allow journey planning until you choose to exit or manually terminate the program.

---

## Data Structure & Algorithms

- **Graph Model**: Stations are modeled as nodes and connections as weighted edges.
- **Dijkstra's Algorithm**: Utilized to calculate the optimal route between stations.

---

## Project Team (Group 8)

- Gong Da (11536511)
- Li Haolin (11536573)
- Chan Kaman (11552292)
- Liu Chenghao (11536559)

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## How to Run the Project

1. **Clone or Download** the repository.
2. **Extract** the files (if downloaded as a ZIP archive).
3. **Open** a terminal or command prompt in the project directory.
4. **Run** the project using the command:
   ```bash
   python main.py
   ```
5. **Follow** the on-screen prompts to log in/register and plan your journey.

---

## Test Cases

Below are sample test cases that illustrate the expected user interactions and outputs:

### Test Case 1: Login and Journey Planning

```
==================================================
    🚇  Welcome to the Metro Travel Planner  🚇     
==================================================

This system allows you to register and log in to plan your metro journeys efficiently.

1. Log In
2. Register
Choose an option (1/2): 1

** Log In **
Enter your username: gongda
Enter your password: 123456
Invalid username or password. Please try again.

Enter your username: gongda
Enter your password: 54321
Login successful!
Let's begin your planning 🚊
``` 
### Test Case 2: Journey Planning
``` 
--------------Planning--------------
Enter starting station: HKU
Enter destination station: University

---Results---
Path: HKU -> Sai Ying Pun -> Sheung Wan -> Central -> Admiralty -> Exhibition Centre -> Hung Hom -> Mong Kok East -> Kowloon Tong -> Tai Wai -> Sha Tin -> Fo Tan -> University
Calculated fee: 20.9
Do you want to plan another journey? (y/n): y

--------------Planning--------------
Enter starting station: EdUHK
Enter destination station: Loa Angles

*** WARNING ***: 
Invalid stations, please enter existing stations.

--------------Planning--------------
Enter starting station: EdUHK
Enter destination station: Los Angles
``` 
### Test Case 3: Cash Back

``` 
---Results---
Path: EdUHK -> Los Angles
Calculated fee: 1000.0
Do you want to plan another journey? (y/n): n
Total expense for this session: 1020.9.
Cash back is 206.97.
```

### Explanation of the Test Cases

- **Authentication Flow**:  
  - The user first attempts to log in with an incorrect password and then successfully logs in with the correct credentials.
  
- **Journey Planning**:  
  - **Case 1**: The user enters a valid starting station ("HKU") and a valid destination ("University"). The system computes an optimal path and displays a calculated fee.
  - **Case 2**: The user attempts to enter invalid station names ("EdUHK" to "Loa Angles"). The system warns about invalid stations.
  - **Case 3**: The user corrects the destination ("Los Angles") for a new journey. The system computes the route with a higher fee and asks if another journey is to be planned.

- **Session Summary**:  
  - At the end of the session, the total expense and applicable cashback are displayed.

---

