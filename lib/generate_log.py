from datetime import datetime
import os
import requests

def fetch_data():
    """
    Fetches data from an external API.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

def generate_log(data):
    """
    Validates input, generates a log filename with today's date,
    writes entries to the file, and prints a confirmation message.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    return filename

if __name__ == "__main__":
    # Fetch post data
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print(f"Fetched Post Title: {post_title}")

    # Prepare log data
    log_data = [
        "User logged in",
        "User updated profile",
        f"Report exported: {post_title}"
    ]

    # Generate log
    generate_log(log_data)
