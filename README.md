# Google-Search-URL-Scraper
"Google Search URL Scraper: A Python script that searches Google for a user-defined search term, collects URLs from the first page of search results, and saves them in a CSV file."

# Google Search URL Scraper

This script searches Google for a user-defined search term and saves the URLs from the first page of search results in a CSV file. This is useful for quickly gathering a list of relevant websites for a specific topic or keyword.

## How it works

1. The script prompts the user to enter a search term.
2. It then uses the `googlesearch` library to search Google for URLs related to the search term on the first page only.
3. The script filters out any non-URL results using a regular expression.
4. The URLs are saved in a CSV file with the name of the search term (spaces replaced with underscores).
5. A sound notification is played when the script is done.

## Prerequisites

Before you can run this script, you need to have Python installed on your system. You can download Python from [the official website](https://www.python.org/downloads/).

## Installation

1. Download or clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Install the required libraries by running the following command: pip install -r requirements.txt

## Running the script

1. In the terminal or command prompt, navigate to the directory where the script is located.
2. Run the following command:
3. Enter your desired search term when prompted.
4. The script will search Google and save the URLs from the first page of search results in a CSV file in the same directory as the script.
5. A sound notification will play when the script is done.

## Notification Sound

Note: If you want to change the sound notification, replace the file path in the `winsound.PlaySound()` function with your desired WAV file path.

