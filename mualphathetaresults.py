from all_imports import *

class ScrapeResults:
    def __init__(self, website):
        self.website = website
        self.name()
        self.getdata()
        self.writedata()

    def name(self):
        spliturl = self.website.split('/')
        self.competition = spliturl[5]
        test = spliturl[6].split('.')
        self.test = test[0]

    def getdata(self):
        try:
            self.data, = pd.read_html(self.website, header=0)
        except Exception as e:
            print("An Error Occured: No connection/No URL")

    def writedata(self):
        try:
            self.jsondata = self.data.to_json(r'data', orient="records")
            #with open("{0}-{1}.json".format(self.competition, self.test), "w") as data_file:
            #    json.dump(self.jsondata, data_file, indent=2)
            print("Made file {0}-{1}.json".format(self.competition, self.test))
        except Exception as e:
            print("An Error Occured: Failed to write data to disk")

if __name__ == "__main__":
    ScrapeResults('http://floridamao.org/Downloadable/Results/Combined02012019/Geometry_Indv.html')
