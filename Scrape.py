from all_imports import *

class ScrapeResults:
    def __init__(self, website):
        self.website = website
        self.name()

    def name(self):
        spliturl = self.website.split('/')
        self.competition = spliturl[5].replace("%20", "_")
        test = spliturl[6].split('.')
        self.test = test[0].replace("%20", "_")
        print("{0}-{1}.json".format(self.competition, self.test))
        self.getdata()

    def getdata(self):
        try:
            self.data, = pd.read_html(self.website, header=0)
            self.writedata()
        except Exception as e:
            # print(repr(e))
            pass

    def writedata(self):
        try:
            self.jsondata = self.data.to_json(DATA / "{0}-{1}.json".format(self.competition, self.test), orient="table")
            # print("Made file {0}-{1}.json".format(self.competition, self.test))
            self.cleanupdata()
        except Exception as e:
            print(repr(e))

    def cleanupdata(self):
        with open(DATA / "{0}-{1}.json".format(self.competition, self.test)) as f:
            json_string = f.read()
        try:
            parsed_json = json.loads(json_string)
            formatted_json = json.dumps(parsed_json, indent = 4, sort_keys=True)
            with open(DATA / "{0}-{1}.json".format(self.competition, self.test), "w") as f:
                f.write(formatted_json)
            self.savefilename()
        except Exception as e:
            print(repr(e))

    def savefilename(self):
        try:
            row = ['{0}-{1}.json'.format(self.competition, self.test)]
            with open(DATA / "filenames.csv", "a", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=",")
                writer.writerow(row)
        except Exception as e:
            print(repr(e))
