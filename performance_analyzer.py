import requests
import time
import pandas as pd

# --- Configuration ---

# The block explorers we will be testing
EXPLORERS = {
    'Blockonomics': 'https://www.blockonomics.co/api/search?q=',
    'Blockchain.com': 'https://www.blockchain.com/btc/', # Note: Needs different endpoints for different search types
    'BTC.com': 'https://btc.com/'
}

# Test data
TEST_DATA = {
    'transaction': 'a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d',
    'address': '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
    'block': '904512'
}

# Number of times to run each test to get an average
NUM_RUNS = 5

# --- Main Script ---

def measure_latency(url):
    """Measures the latency of a single HTTP GET request."""
    try:
        start_time = time.time()
        response = requests.get(url, timeout=15)
        end_time = time.time()
        response.raise_for_status()  # Raise an exception for bad status codes
        return (end_time - start_time) * 1000  # Return latency in milliseconds
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def run_tests():
    """Runs the performance tests for all explorers and all data types."""
    results = []

    print("Starting performance analysis...")

    for explorer_name, base_url in EXPLORERS.items():
        print(f"\nTesting {explorer_name}...")
        for search_type, value in TEST_DATA.items():
            latencies = []
            for i in range(NUM_RUNS):
                # Construct the correct URL for each explorer and search type
                if explorer_name == 'Blockonomics':
                    url = f"{base_url}{value}"
                elif explorer_name == 'Blockchain.com':
                    url = f"{base_url}{search_type}/{value}"
                elif explorer_name == 'BTC.com':
                    url = f"{base_url}{value}"
                else:
                    continue

                print(f"  - Run {i+1}/{NUM_RUNS} for {search_type} '{value[:10]}...'", end='')
                latency = measure_latency(url)
                if latency is not None:
                    latencies.append(latency)
                    print(f" -> {latency:.2f} ms")
                else:
                    print(" -> Failed")

            if latencies:
                avg_latency = sum(latencies) / len(latencies)
                results.append({
                    'Explorer': explorer_name,
                    'SearchType': search_type.capitalize(),
                    'AverageLatency': avg_latency
                })

    return pd.DataFrame(results)

if __name__ == "__main__":
    performance_data = run_tests()

    if not performance_data.empty:
        # Save the results to a CSV file
        output_file = 'performance_data.csv'
        performance_data.to_csv(output_file, index=False)
        print(f"\nPerformance data saved to {output_file}")
        print("\n--- Results Summary ---")
        print(performance_data)
    else:
        print("\nNo performance data was collected.")
