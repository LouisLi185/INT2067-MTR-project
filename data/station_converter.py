"""
A CSV file from https://data.gov.hk/sc-data/dataset/mtr-data-routes-fares-barrier-free-facilities was used as station data.
However, since the graph data type is the best way to handle this topic, this program is designed to read the CSV
and convert it to a graph data type.
It may not be necessary to set the real distance between each station.
Hence, we set all distances between stations to 1 to simplify the problem.
"""

import csv

# Define CSV field names
fieldnames = ["Line_Code", "Direction", "Station_Code", "Station_ID", "Chinese_Name", "English_Name", "Sequence"]

# Create a list to store unique line codes and a list for station records with the selected direction ("DT")
line_list = []
stations_data = []

# Read the CSV file and build the line list and station data (only for direction "DT")
with open("mtr_lines_and_stations.csv", newline="", encoding="utf-8") as csvfile:
    csvreader = csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in csvreader:
        if row["Direction"] == "DT":  # Process only one direction for simplicity
            stations_data.append(row)
            # Add each line code (split by comma if necessary) to the line list
            for line in row["Line_Code"].split(","):
                if line not in line_list:
                    line_list.append(line)

# Organize station data by line and sort each line's stations by their sequence number
lines_stations = {}  # key: line code, value: list of (sequence, English_Name)
for row in stations_data:
    for line in row["Line_Code"].split(","):
        if line in line_list:
            if line not in lines_stations:
                lines_stations[line] = []
            try:
                seq = int(row["Sequence"])
            except ValueError:
                seq = 0  # Default to 0 if conversion fails
            lines_stations[line].append((seq, row["English_Name"]))

# Sort the stations on each line based on sequence
for line in lines_stations:
    lines_stations[line].sort(key=lambda x: x[0])

# Build the subway map graph:
# Each station is a node; adjacent stations (on the same line) are connected with a distance of 1.
subway_map = {}
for line, stations in lines_stations.items():
    for i in range(len(stations) - 1):
        station1 = stations[i][1]
        station2 = stations[i + 1][1]
        if station1 not in subway_map:
            subway_map[station1] = {}
        if station2 not in subway_map:
            subway_map[station2] = {}
        # Create bidirectional edges with a distance of 1
        subway_map[station1][station2] = 1
        subway_map[station2][station1] = 1

# Output the subway_map in the specified format
print("MTR_map = {")
for station, neighbors in subway_map.items():
    print(f"    '{station}': {neighbors},")
print("}")
