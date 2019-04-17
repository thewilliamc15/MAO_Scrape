from all_imports import *

class Urls:
    def __init__(self):
        self.mainsite = requests.get("http://floridamao.org/PublicPages/Results.aspx")
        self.scrape()

    def scrape(self):
        soup = BeautifulSoup(self.mainsite.text, 'html.parser')
        a = soup.find_all('a')
        print(a)
