from all_imports import *

import datetime

def grabdata():
    getUrls = Urls()
    list = []
    with open(DATA / "urls.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            list += row
    for url in list:
        ScrapeResults(url)

start = datetime.datetime.now()
print(start)
grabdata()
end = datetime.datetime.now()
print(end)
print(end - start)
