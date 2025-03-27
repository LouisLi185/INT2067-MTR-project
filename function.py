import heapq
import csv

# Use the converter result to use dic to store the graph
MTR_map = {
    'AsiaWorld-Expo': {'Airport': 1},
    'Airport': {'AsiaWorld-Expo': 1, 'Tsing Yi': 1},
    'Tsing Yi': {'Airport': 1, 'Kowloon': 1, 'Sunny Bay': 1, 'Lai King': 1},
    'Kowloon': {'Tsing Yi': 1, 'Hong Kong': 1, 'Olympic': 1},
    'Hong Kong': {'Kowloon': 1},
    'Sunny Bay': {'Disneyland Resort': 1, 'Tung Chung': 1, 'Tsing Yi': 1},
    'Disneyland Resort': {'Sunny Bay': 1},
    'Lo Wu': {'Sheung Shui': 1},
    'Sheung Shui': {'Lo Wu': 1, 'Fanling': 1},
    'Fanling': {'Sheung Shui': 1, 'Tai Wo': 1},
    'Tai Wo': {'Fanling': 1, 'Tai Po Market': 1},
    'Tai Po Market': {'Tai Wo': 1, 'University': 1},
    'University': {'Tai Po Market': 1, 'Fo Tan': 1},
    'Fo Tan': {'University': 1, 'Sha Tin': 1},
    'Sha Tin': {'Fo Tan': 1, 'Tai Wai': 1},
    'Tai Wai': {'Sha Tin': 1, 'Kowloon Tong': 1, 'Hin Keng': 1, 'Che Kung Temple': 1},
    'Kowloon Tong': {'Tai Wai': 1, 'Mong Kok East': 1, 'Lok Fu': 1, 'Shek Kip Mei': 1},
    'Mong Kok East': {'Kowloon Tong': 1, 'Hung Hom': 1},
    'Hung Hom': {'Mong Kok East': 1, 'Exhibition Centre': 1, 'East Tsim Sha Tsui': 1, 'Ho Man Tin': 1},
    'Exhibition Centre': {'Hung Hom': 1, 'Admiralty': 1},
    'Admiralty': {'Exhibition Centre': 1, 'Wan Chai': 1, 'Central': 1, 'Tsim Sha Tsui': 1, 'Ocean Park': 1},
    'Chai Wan': {'Heng Fa Chuen': 1},
    'Heng Fa Chuen': {'Chai Wan': 1, 'Shau Kei Wan': 1},
    'Shau Kei Wan': {'Heng Fa Chuen': 1, 'Sai Wan Ho': 1},
    'Sai Wan Ho': {'Shau Kei Wan': 1, 'Tai Koo': 1},
    'Tai Koo': {'Sai Wan Ho': 1, 'Quarry Bay': 1},
    'Quarry Bay': {'Tai Koo': 1, 'North Point': 1, 'Yau Tong': 1},
    'North Point': {'Quarry Bay': 1, 'Fortress Hill': 1},
    'Fortress Hill': {'North Point': 1, 'Tin Hau': 1},
    'Tin Hau': {'Fortress Hill': 1, 'Causeway Bay': 1},
    'Causeway Bay': {'Tin Hau': 1, 'Wan Chai': 1},
    'Wan Chai': {'Causeway Bay': 1, 'Admiralty': 1},
    'Central': {'Admiralty': 1, 'Sheung Wan': 1},
    'Sheung Wan': {'Central': 1, 'Sai Ying Pun': 1},
    'Sai Ying Pun': {'Sheung Wan': 1, 'HKU': 1},
    'HKU': {'Sai Ying Pun': 1, 'Kennedy Town': 1},
    'Kennedy Town': {'HKU': 1},
    'Tiu Keng Leng': {'Yau Tong': 1, 'Tseung Kwan O': 1},
    'Yau Tong': {'Tiu Keng Leng': 1, 'Lam Tin': 1, 'Quarry Bay': 1},
    'Lam Tin': {'Yau Tong': 1, 'Kwun Tong': 1},
    'Kwun Tong': {'Lam Tin': 1, 'Ngau Tau Kok': 1},
    'Ngau Tau Kok': {'Kwun Tong': 1, 'Kowloon Bay': 1},
    'Kowloon Bay': {'Ngau Tau Kok': 1, 'Choi Hung': 1},
    'Choi Hung': {'Kowloon Bay': 1, 'Diamond Hill': 1},
    'Diamond Hill': {'Choi Hung': 1, 'Wong Tai Sin': 1, 'Kai Tak': 1, 'Hin Keng': 1},
    'Wong Tai Sin': {'Diamond Hill': 1, 'Lok Fu': 1},
    'Lok Fu': {'Wong Tai Sin': 1, 'Kowloon Tong': 1},
    'Shek Kip Mei': {'Kowloon Tong': 1, 'Prince Edward': 1},
    'Prince Edward': {'Shek Kip Mei': 1, 'Mong Kok': 1, 'Sham Shui Po': 1},
    'Mong Kok': {'Prince Edward': 1, 'Yau Ma Tei': 1},
    'Yau Ma Tei': {'Mong Kok': 1, 'Ho Man Tin': 1, 'Jordan': 1},
    'Ho Man Tin': {'Yau Ma Tei': 1, 'Whampoa': 1, 'Hung Hom': 1, 'To Kwa Wan': 1},
    'Whampoa': {'Ho Man Tin': 1},
    'Tuen Mun': {'Siu Hong': 1},
    'Siu Hong': {'Tuen Mun': 1, 'Tin Shui Wai': 1},
    'Tin Shui Wai': {'Siu Hong': 1, 'Long Ping': 1},
    'Long Ping': {'Tin Shui Wai': 1, 'Yuen Long': 1},
    'Yuen Long': {'Long Ping': 1, 'Kam Sheung Road': 1},
    'Kam Sheung Road': {'Yuen Long': 1, 'Tsuen Wan West': 1},
    'Tsuen Wan West': {'Kam Sheung Road': 1, 'Mei Foo': 1},
    'Mei Foo': {'Tsuen Wan West': 1, 'Nam Cheong': 1, 'Lai King': 1, 'Lai Chi Kok': 1},
    'Nam Cheong': {'Mei Foo': 1, 'Austin': 1, 'Lai King': 1, 'Olympic': 1},
    'Austin': {'Nam Cheong': 1, 'East Tsim Sha Tsui': 1},
    'East Tsim Sha Tsui': {'Austin': 1, 'Hung Hom': 1},
    'To Kwa Wan': {'Ho Man Tin': 1, 'Sung Wong Toi': 1},
    'Sung Wong Toi': {'To Kwa Wan': 1, 'Kai Tak': 1},
    'Kai Tak': {'Sung Wong Toi': 1, 'Diamond Hill': 1},
    'Hin Keng': {'Diamond Hill': 1, 'Tai Wai': 1},
    'Che Kung Temple': {'Tai Wai': 1, 'Sha Tin Wai': 1},
    'Sha Tin Wai': {'Che Kung Temple': 1, 'City One': 1},
    'City One': {'Sha Tin Wai': 1, 'Shek Mun': 1},
    'Shek Mun': {'City One': 1, 'Tai Shui Hang': 1},
    'Tai Shui Hang': {'Shek Mun': 1, 'Heng On': 1},
    'Heng On': {'Tai Shui Hang': 1, 'Ma On Shan': 1},
    'Ma On Shan': {'Heng On': 1, 'Wu Kai Sha': 1},
    'Wu Kai Sha': {'Ma On Shan': 1},
    'Tung Chung': {'Sunny Bay': 1},
    'Lai King': {'Tsing Yi': 1, 'Nam Cheong': 1, 'Kwai Fong': 1, 'Mei Foo': 1},
    'Olympic': {'Nam Cheong': 1, 'Kowloon': 1},
    'Po Lam': {'Hang Hau': 1},
    'Hang Hau': {'Po Lam': 1, 'Tseung Kwan O': 1},
    'Tseung Kwan O': {'Hang Hau': 1, 'Tiu Keng Leng': 1},
    'Tsuen Wan': {'Tai Wo Hau': 1},
    'Tai Wo Hau': {'Tsuen Wan': 1, 'Kwai Hing': 1},
    'Kwai Hing': {'Tai Wo Hau': 1, 'Kwai Fong': 1},
    'Kwai Fong': {'Kwai Hing': 1, 'Lai King': 1},
    'Lai Chi Kok': {'Mei Foo': 1, 'Cheung Sha Wan': 1},
    'Cheung Sha Wan': {'Lai Chi Kok': 1, 'Sham Shui Po': 1},
    'Sham Shui Po': {'Cheung Sha Wan': 1, 'Prince Edward': 1},
    'Jordan': {'Yau Ma Tei': 1, 'Tsim Sha Tsui': 1},
    'Tsim Sha Tsui': {'Jordan': 1, 'Admiralty': 1},
    'South Horizons': {'Lei Tung': 1},
    'Lei Tung': {'South Horizons': 1, 'Wong Chuk Hang': 1},
    'Wong Chuk Hang': {'Lei Tung': 1, 'Ocean Park': 1},
    'Ocean Park': {'Wong Chuk Hang': 1, 'Admiralty': 1},

}


"""
Use Dijkstra's algorithm to calculate for the minimum route
This function will return a set containing the number of stations passed and a list with each station
please consider use:
    distance, path = min_route(start_station, end_station)
to call this function
"""
def min_route(start, end):
    # Priority queue: each element is a tuple (current_distance, current_node, path)
    queue = [(0, start, [start])]
    # Set to track visited nodes and avoid processing them again
    visited = set()

    while queue:
        current_distance, current_node, path = heapq.heappop(queue)

        # If the current node is the destination, return the results
        if current_node == end:
            return current_distance, path

        # Skip the node if it has already been processed
        if current_node in visited:
            continue
        visited.add(current_node)

        # Process each neighbor of the current node
        for neighbor, weight in MTR_map.get(current_node, {}).items():
            if neighbor not in visited:
                new_distance = current_distance + weight
                # Add the new state to the queue with the updated path
                heapq.heappush(queue, (new_distance, neighbor, path + [neighbor]))

    # If the destination is not reachable, return infinity and an empty path
    return float('inf'), []

def fee_caculate(start_station, end_station, row, row_iter):
    pass # Revise Later
'''
    """
    'row' is for replenish csv row
    'row_iter' is for replenish iteration
    To save time and make everything clear, I replace

    'for row in row_iter:
        if len(row) < 5:
            continue'

    If needed, you could add them back and delete this supplement.
    """
    # Read CSV file to get basic info
    with open("data/mtr_lines_fares.csv", 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
    # Find the first column of the start_station
    if row[0] == start_station:
        # Check if the end_station match the first one (will do iteration later!)
        if row[2] == end_station:
            return row[4]
    
    """
    We are now in the iteration. According to the CSV file, there is only 94 stations options left.
    The traversal(遍歷) process will be much simpler.
    What should do is to traverse the next 94 lines.
    """
    for _ in range(94):
        try:
            next_row = next(row_iter)
        except StopIteration:
            continue
'''