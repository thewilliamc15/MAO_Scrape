from all_imports import *

list = []

with open(DATA + "urls.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        list += row

for url in list:
    ScrapeResults(url)
