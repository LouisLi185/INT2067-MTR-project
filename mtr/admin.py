import json
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans


def load_stations_data(file_path='data/stations.json'):
    """
    Load station data from the specified JSON file.
    """
    path = Path(file_path)
    if not path.exists():
        print(f"{file_path} does not exist.")
        return {"stations": []}
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def plot_station_stats(station):
    """
    Plot a grouped bar chart for a given station showing counts for each age group (fixed intervals)
    separated by gender.
    """
    stats = station.get("stats", {})
    male_stats = stats.get("male", {})
    female_stats = stats.get("female", {})

    # Define age intervals (e.g., 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60+)
    intervals = [(0, 9), (10, 19), (20, 29), (30, 39), (40, 49), (50, 59), (60, 120)]
    interval_labels = [f"{low}-{high}" if high != 120 else f"{low}+" for low, high in intervals]

    # Initialize counts for each interval to 0
    male_agg = {label: 0 for label in interval_labels}
    female_agg = {label: 0 for label in interval_labels}

    # Group and aggregate male data by intervals
    for age_str, count in male_stats.items():
        age = int(age_str)
        for (low, high), label in zip(intervals, interval_labels):
            if low <= age <= high:
                male_agg[label] += count
                break

    # Group and aggregate female data by intervals
    for age_str, count in female_stats.items():
        age = int(age_str)
        for (low, high), label in zip(intervals, interval_labels):
            if low <= age <= high:
                female_agg[label] += count
                break

    # Prepare data in the predefined interval order
    male_counts = [male_agg[label] for label in interval_labels]
    female_counts = [female_agg[label] for label in interval_labels]

    x = np.arange(len(interval_labels))  # label locations
    width = 0.35  # width of each bar

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, male_counts, width, label='Male')
    rects2 = ax.bar(x + width / 2, female_counts, width, label='Female')

    # Add labels and title
    ax.set_xlabel('Age Group')
    ax.set_ylabel('Count')
    ax.set_title(f"Station {station.get('station_id')} Statistics by Age Group and Gender")
    ax.set_xticks(x)
    ax.set_xticklabels(interval_labels)
    ax.legend()

    # Add numeric labels on top of each bar.
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # vertical offset in points
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()
    plt.show()


def admin_dashboard():
    """
    Simple admin dashboard that loads station data and allows admin to visualize
    each station's statistics via charts.
    """
    data = load_stations_data()
    stations = data.get("stations", [])
    if not stations:
        print("No station data available.")
        return

    # List available stations.
    print("Available Stations:")
    for i, station in enumerate(stations, start=1):
        print(f"{i}. {station.get('station_id')}")

    choice = input("Enter the number of the station to view details (or 'all' for all stations): ").strip()
    if choice.lower() == "all":
        for station in stations:
            plot_station_stats(station)
    else:
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(stations):
                station = stations[choice_num - 1]
                plot_station_stats(station)
            else:
                print("Invalid choice number.")
        except ValueError:
            print("Invalid input. Please enter a number or 'all'.")


def perform_kmeans_analysis(n_clusters=3):
    """
    Perform KMeans clustering analysis on station demographic data.
    For each station, we compute a feature vector:
      [total_passenger_count, overall_average_age]
    """
    data = load_stations_data()
    stations = data.get("stations", [])
    if not stations:
        print("No station data available.")
        return

    features = []
    station_ids = []
    for station in stations:
        stats = station.get("stats", {})
        male_stats = stats.get("male", {})
        female_stats = stats.get("female", {})

        total_male = sum(male_stats.values())
        total_female = sum(female_stats.values())
        total_passengers = total_male + total_female

        total_age_sum = 0
        # Sum weighted ages for males
        if total_male > 0:
            total_age_sum += sum(int(age) * count for age, count in male_stats.items())
        # Sum weighted ages for females
        if total_female > 0:
            total_age_sum += sum(int(age) * count for age, count in female_stats.items())
        if total_passengers > 0:
            overall_avg_age = total_age_sum / total_passengers
        else:
            overall_avg_age = 0

        features.append([total_passengers, overall_avg_age])
        station_ids.append(station.get("station_id"))

    features = np.array(features)
    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    clusters = kmeans.fit_predict(features)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(features[:, 0], features[:, 1], c=clusters, cmap='viridis')
    # Annotate each data point with the station name.
    for i, txt in enumerate(station_ids):
        plt.annotate(txt, (features[i, 0], features[i, 1]), fontsize=9, fontweight='bold')
    plt.xlabel("Total Passenger Count")
    plt.ylabel("Overall Average Age")
    plt.title("KMeans Clustering of Stations\n(Total Passenger Count vs. Average Age)")
    plt.colorbar(scatter, label="Cluster")
    plt.show()

    # Print cluster assignments
    print("Cluster assignments:")
    for sid, cluster in zip(station_ids, clusters):
        print(f"{sid}: Cluster {cluster}")


def admin():
    """
    Admin backend with two functionalities:
    1. Visualize station statistics via charts.
    2. Perform KMeans clustering analysis.

    In the clustering analysis, two features are used:
      - Total Passenger Count
      - Overall Average Age
    Each data point in the scatter plot is labeled with the station name.
    """
    while True:
        print("\nAdmin Dashboard")
        print("1. Visualize station statistics")
        print("2. Perform KMeans clustering analysis")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            admin_dashboard()  # Visualize individual station statistics.
        elif choice == "2":
            try:
                n_clusters = int(input("Enter number of clusters for KMeans (default 3): ") or "3")
            except ValueError:
                n_clusters = 3
            perform_kmeans_analysis(n_clusters)
        elif choice == "3":
            print("Exiting admin dashboard.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    admin()
