# This script will search the first page of google.com for urls

import csv
import googlesearch
import re
import time
import sys
import winsound

# Prompt the user for the search term
search_term = input('Enter a search term: ')

# Search Google for URLs related to the search term on the first page only
urls = []
search_results = googlesearch.search(search_term, num_results=10)
urls += [url for url in search_results if re.match(r'^https?://', url)]
# Update progress bar and percentage
progress = (i + 1) * 10
sys.stdout.write('\r')
sys.stdout.write("[%-100s] %d%%" % ('=' * progress, progress))
sys.stdout.flush()
time.sleep(0.1)


# Write the URLs to a CSV file with the name of the search term
filename = search_term.replace(' ', '_') + '.csv'
with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    for url in urls:
        writer.writerow([url])

# Play sound notification when done
winsound.PlaySound('C:/Users/david/audio/youve-got-mail-sound.wav', winsound.SND_FILENAME)
