[![Open in Visual Studio Code](https://img.shields.io/badge/Open%20in-Visual%20Studio%20Code-blue?logo=visual-studio-code&logoColor=white)](vscode://vscode.git/clone?url=https://github.com/LouisLi185/INT2067-MTR-project)

# MTR Journey Planner with Cashback Incentives

A command-line application simulating a smart transit system for the MTR network with integrated cashback incentives.

## Project Overview

This application models the MTR network using a graph-based data structure where stations are represented as nodes and connections as weighted edges (representing travel costs). The system provides optimal route calculation and implements Hong Kong's public transport subsidy scheme.

## Features

- **Secure Authentication**: User login system to ensure authorized access
- **Optimal Route Planning**: Uses Dijkstra's algorithm to compute the most efficient journey between stations
- **Journey Logging**: Records trip details and costs in CSV format
- **Cashback Incentive System**: Implements Hong Kong's public transport subsidy scheme
  - Citizens spending over HK$400 per month qualify for a subsidy
  - One-third of expenses exceeding HK$400 is reimbursed
  - Maximum subsidy of HK$400 per account

## Getting Started

### Prerequisites

[List any prerequisites or dependencies here]

### Installation

[Provide installation instructions here]

### Usage

[Provide basic usage instructions here]

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
