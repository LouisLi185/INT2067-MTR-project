# 🚇MTR Journey Planner with Cashback Incentives🚇

A command-line application simulating a smart transit system for the MTR network with integrated cashback incentives.

## Project Overview

This application models the MTR network using a graph-based data structure where stations are represented as nodes and connections as weighted edges (representing travel costs). The system provides optimal route calculation and implements Hong Kong's public transport subsidy scheme.

## Features

- **Secure Authentication**: User login system to ensure authorized access.
- **Optimal Route Planning**: Uses Dijkstra's algorithm to compute the most efficient journey between stations.
- **Journey Logging**: Records trip details and total costs in CSV format.
- **Cashback Incentive System**: Implements Hong Kong's public transport subsidy scheme.
  - Adult Citizens spending over HK$400 per month with an Octopus Card qualify for a subsidy.
  - One-third of expenses exceeding HK$400 is reimbursed.
  - Maximum subsidy of HK$400 per account.

## Getting Started

### Prerequisites

- Python Environment: Ensure that Python is installed and properly configured on your system. It is recommended to use the latest stable release. For additional details, please refer to the [Python official website](https://python.org).

### Installation

This project is distributed as source code only and does not include any executable files. To install and run the project, please follow these steps:

1. Download the repository as a ZIP archive from GitHub.
2. Extract the contents of the ZIP file to a directory of your choice.
3. Execute the `main.py` file using your preferred Python interpreter.

### Usage

1. **Account Management**:
- Upon startup, the system will prompt you to either log in or register a new account.
- Follow the on-screen instructions to complete the selected authentication process.

2. **Route Input**:
- After a successful login, you will be asked to input the starting station and destination station.
- Please enter the station names in English exactly as they appear on the [MTR Map](https://www.mtr.com.hk/archive/en/services/routemap.pdf).
- The system will validate your input to ensure that neither an invalid station name nor a duplicate station is entered.

3. **Route Calculation and Fee Estimation**:
- Once valid input is provided, the system will calculate the shortest route between the specified stations.
- The system will also compute the corresponding travel fees and display both the route and fee details.

4. **Additional Journey Planning**:
- After displaying the results, the system will ask if you would like to plan an additional journey.
- If you select **Yes**, you will be prompted to enter a new starting station and destination station. The travel fees for the new journey will be appended to a CSV file and aggregated with the fees from previous journeys.
- If you respond with **No**, the program will terminate, completing the session.

5. **Program Termination**:
- The system continues to allow journey planning until you either choose to exit or manually terminate the program.
## Data Structure

The MTR network is modeled as a graph where:
- Nodes represent stations
- Weighted edges represent connections between stations and their associated costs

## Algorithms

- **Dijkstra's Algorithm**: Used for calculating the optimal route between stations


## Project Team (Group 8)

- Gong Da (11536511)
- Li Haolin (11536573)
- Chan Kaman (11552292)
- Liu Chenghao (11536559)
  

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
