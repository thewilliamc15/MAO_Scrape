from all_imports import *

def grabdata():
    getUrls = Urls(14)
    list = []
    with open(DATA / "urls.csv", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        for row in reader:
            list += row
    for url in list:
        ScrapeResults(url)

def lengthyears():
    years = list()
    site = requests.get("http://floridamao.org/PublicPages/Results.aspx")
    soup = BeautifulSoup(site.text, 'html.parser')
    options = soup.find_all('option')
    for item in options:
        years.append(item.get('value'))
    return len(years)

# These no longer work :( ever since i removed ijson
# Keeping them for ideas
"""
def place(json_filename, place, stat):
    with open(DATA / json_filename, 'rb') as input_file:
        objects = ijson.items(input_file, 'item')
        actual = (o for o in objects if o['Rank'] == place)
        for item in actual:
            item = dict(item)
            for items in item:
                if items == stat:
                    return item[items]

def scoring(json_filename, score, stat):
    with open(DATA / json_filename, 'rb') as input_file:
        objects = ijson.items(input_file, 'item')
        actual = (o for o in objects if o['Score'] == score)
        for item in actual:
            item = dict(item)
            for items in item:
                if items == stat:
                    return item[items]

numberof120s = 0
lowestscore = 120
total = 0
firstscore = 120
lowfile = ""
try:
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            firstscore = place(filename, "1st", "Score")
            if firstscore != None:
                if firstscore < lowestscore:
                    lowfile = filename
                    lowestscore = firstscore
                if firstscore == 120:
                    numberof120s += 1
                total += 1
            scores = score(filename, -30, "Name")
            schoolname = score(filename, -30, "School")
            if scores != None:
                print("From {} with a score of -30, {}. ({})".format(schoolname, scores, filename))
except Exception as e:
    pass

print("Percent of tests with 120's:{}%\nLowest First Place:{}({})".format((numberof120s / total) * 100, lowestscore, lowfile))
"""
