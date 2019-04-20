from all_imports import *


class Urls:
    def __init__(self):
        try:
            os.remove(DATA / 'urls.csv')
        except Exception as e:
            pass
        #with open(DATA / 'urls.csv', 'w') as file:
        #    writer = csv.writer(file)
        #    writer.writerow(empty)
        self.mainsite = requests.get("http://floridamao.org/PublicPages/Results.aspx")
        self.yearurl = "http://floridamao.org/PublicPages/Results.aspx?=__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ddlYear&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTIwNDIzNzUwODEPZBYCZg9kFgQCAQ9kFgICAQ8WAh4EaHJlZgUnLi4vU3R5bGUvZmxvcmlkYU1BT1N0eWxlLmNzcz83eDM2eDE3eVBNZAIDD2QWBGYPDxYCHgRUZXh0BQdSZXN1bHRzZGQCAg9kFgICAQ8QZA8WDWYCAQICAgMCBAIFAgYCBwIIAgkCCgILAgwWDRAFBDIwMTkFBDIwMTlnEAUEMjAxOAUEMjAxOGcQBQQyMDE3BQQyMDE3ZxAFBDIwMTYFBDIwMTZnEAUEMjAxNQUEMjAxNWcQBQQyMDE0BQQyMDE0ZxAFBDIwMTMFBDIwMTNnEAUEMjAxMgUEMjAxMmcQBQQyMDExBQQyMDExZxAFBDIwMTAFBDIwMTBnEAUEMjAwOQUEMjAwOWcQBQQyMDA4BQQyMDA4ZxAFBDIwMDcFBDIwMDdnZGRkjOPKhOTsvwezWeNqxqzZuGecOx4THT%2FUqxDZAsCFNMk%3D&__VIEWSTATEGENERATOR=B9E74498&__EVENTVALIDATION=%2FwEdAA%2Fe0LFHuFLSAewtKoes5KjtxqHRL00rt8adneBfK88dfT%2BcOQi%2F0dvZM%2FyXsG9QPIiOrm0r1Wn1HnGVbwDbzEtDcFpyEho21yFh9mi857vYO%2FVF7N17OGdfvDavsvJ3rC9JUv8tdp9R5JYA9kjV4p8Tz2DMGDHfiWBe%2FIv2qQVSnxj1HlWjlZi7vwPK5DR%2BS0u%2FSpoYG89BqY5x3gn2oXgIXvbY9qQ%2FTK2O8IEyJfiSmd2Rkk0fmBEOTNydQGMCOFgJz%2Fp83ath%2BQHOOQw7szKNUNaGGm7fiiWRQalAAQme9ZNliHd3hQy%2B3bUlzeHxKjjmFyhU55jQ%2FzxegTQUWmyz0C2KMoyt%2BEsaYOv8Xw6u3g%3D%3D&ctl00%24ContentPlaceHolder1%24ddlYear={0}"
        self.years = list()
        self.x = 0
        self.getyears()
        for year in self.years:
            self.scrape(year)

    def getyears(self):
        soup = BeautifulSoup(self.mainsite.text, 'html.parser')
        options = soup.find_all('option')
        for item in options:
            self.years.append(item.get('value'))

    def scrape(self, year):
        site = requests.get(self.yearurl.format(year))
        soup = BeautifulSoup(site.text, 'html.parser')
        a = soup.find_all('a')
        for item in a:
            if item.get("href").startswith("../Downloadable/Results/"):
                if "Sweeps" not in item.get("href"):
                    url = item.get('href')[2:]
                    url = url.replace(' ', '%20')
                    url = "http://floridamao.org" + url
                    self.saveurl(url)

    def saveurl(self, url):
        row = [url]
        if self.x == 0:
            with open(DATA / 'urls.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(row)
                self.x = 1
        elif self.x == 1:
            with open(DATA / 'urls.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(row)
