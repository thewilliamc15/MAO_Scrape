from all_imports import *


class Urls:
    def __init__(self, yearstodownload=4):
        try:
            os.remove(DATA / 'urls.csv')
        except Exception as e:
            pass
        self.forbidden = ['Sweeps', "Detail"]
        #with open(DATA / 'urls.csv', 'w') as file:
        #    writer = csv.writer(file)
        #    writer.writerow(empty)
        self.mainsite = requests.get("http://floridamao.org/PublicPages/Results.aspx")
        self.yearurl = "http://floridamao.org/PublicPages/Results.aspx?=__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ddlYear&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwULLTIwNDIzNzUwODEPZBYCZg9kFgQCAQ9kFgICAQ8WAh4EaHJlZgUoLi4vU3R5bGUvZmxvcmlkYU1BT1N0eWxlLmNzcz8xMngzOHgwMXlQTWQCAw9kFgRmDw8WAh4EVGV4dAUHUmVzdWx0c2RkAgIPZBYCAgEPEGQPFg5mAgECAgIDAgQCBQIGAgcCCAIJAgoCCwIMAg0WDhAFBDIwMjAFBDIwMjBnEAUEMjAxOQUEMjAxOWcQBQQyMDE4BQQyMDE4ZxAFBDIwMTcFBDIwMTdnEAUEMjAxNgUEMjAxNmcQBQQyMDE1BQQyMDE1ZxAFBDIwMTQFBDIwMTRnEAUEMjAxMwUEMjAxM2cQBQQyMDEyBQQyMDEyZxAFBDIwMTEFBDIwMTFnEAUEMjAxMAUEMjAxMGcQBQQyMDA5BQQyMDA5ZxAFBDIwMDgFBDIwMDhnEAUEMjAwNwUEMjAwN2dkZGS5xOv0cjQWI4T72TohLkc3Nm0jEedYO6OzFRiZGDcMRQ%3D%3D&__VIEWSTATEGENERATOR=B9E74498&__EVENTVALIDATION=%2FwEdABAj9K8qPoBfx9EtPXO%2BG8qdxqHRL00rt8adneBfK88dfVLio2QbUdKvSvCABTB%2BSyQ%2FnDkIv9Hb2TP8l7BvUDyIjq5tK9Vp9R5xlW8A28xLQ3BachIaNtchYfZovOe72Dv1RezdezhnX7w2r7Lyd6wvSVL%2FLXafUeSWAPZI1eKfE89gzBgx34lgXvyL9qkFUp8Y9R5Vo5WYu78DyuQ0fktLv0qaGBvPQamOcd4J9qF4CF722PakP0ytjvCBMiX4kpndkZJNH5gRDkzcnUBjAjhYCc%2F6fN2rYfkBzjkMO7MyjVDWhhpu34olkUGpQAEJnvWTZYh3d4UMvt21Jc3h8So4Yf7WrkzBNBzBu82dnBZpDEj0iz%2FD7dWVSFlGHBeGrHQ%3D&ctl00%24ContentPlaceHolder1%24ddlYear={0}"
        self.years = list()
        self.x = 0
        self.getyears()
        self.years = self.years[:yearstodownload]
        print(self.years)
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
