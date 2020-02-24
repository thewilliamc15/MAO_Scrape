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
