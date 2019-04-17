from all_imports import *

class ScrapeResults:
    def __init__(self, website):
        self.website = website
        self.name()

    def name(self):
        spliturl = self.website.split('/')
        self.competition = spliturl[5]
        test = spliturl[6].split('.')
        self.test = test[0]
        self.getdata()

    def getdata(self):
        try:
            self.data, = pd.read_html(self.website, header=0)
            self.writedata()
        except Exception as e:
            print("An Error Occured: No connection/No URL")

    def writedata(self):
        try:
            self.jsondata = self.data.to_json(DATA + "temp.json".format(self.competition, self.test), orient="records")
            # print("Made file {0}-{1}.json".format(self.competition, self.test))
            self.cleanupdata()
        except Exception as e:
            print("An Error Occured: Failed to write data to disk")

    def cleanupdata(self):
        with open(DATA + "temp.json") as g, open(DATA + "{0}-{1}.json".format(self.competition, self.test)) as fout:
            for l in g:
                json.dump(eval(l), fout)
        os.remove(DATA + "temp.json")
        self.savefilename()

    def savefilename(self):
        with open(LOCATION + "filenames.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(['{0}-{1}.json'.format(self.competition, self.test)])

if __name__ == "__main__":
    ScrapeResults('http://floridamao.org/Downloadable/Results/Combined02012019/Geometry_Indv.html')
