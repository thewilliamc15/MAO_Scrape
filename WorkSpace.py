from all_imports import *

with open(DATA / 'filenames.csv', newline='') as file:
    list = []
    reader = csv.reader(file, delimiter=" ")
    for row in reader:
        list += row

def score(json_filename, score, stat):
    with open(DATA / json_filename, 'rb') as input_file:
        data = json.load(input_file)
        for competitor in data["data"]:
            if competitor["Score"] == score:
                return competitor[stat]

def competitorCount(json_filename):
    with open(DATA / json_filename, 'rb') as input_file:
        data = json.load(input_file)
        count = 0
        for competitor in data["data"]:
            count += 1
        return count

def totalCompetitorCount():
    totalCount = 0
    for filename in list:
        totalCount += competitorCount(filename)
    return totalCount

def findByScore(seekscore=-30):
    try:
        people = []
        for filename in list:
            if "Bowl" not in filename and "Team" not in filename:
                scores = score(filename, seekscore, "Name")
                schoolname = score(filename, seekscore, "School")
                if scores != None:
                    people += ["From {} with a score of {}, {}. ({})".format(schoolname, seekscore, scores, filename)]
        return people
    except Exception as e:
        print(e)

def highestTScore():
    tscore = 0
    name = ""
    school = ""
    highname = ""
    score = ""
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            with open(DATA / filename, 'rb') as input_file:
                data = json.load(input_file)
                for competitor in data["data"]:
                    if competitor["T-Score"] > tscore:
                        tscore = competitor["T-Score"]
                        name = competitor["Name"]
                        school = competitor["School"]
                        score = competitor["Score"]
                        highname = filename
    print("From {}, with a score of {}, {}. T-Score: {}  ({})".format(school, score, name, tscore, highname))

def lowestTScore():
    tscore = 1000
    name = ""
    school = ""
    highname = ""
    score = ""
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            with open(DATA / filename, 'rb') as input_file:
                data = json.load(input_file)
                for competitor in data["data"]:
                    if competitor["T-Score"] < tscore:
                        tscore = competitor["T-Score"]
                        name = competitor["Name"]
                        school = competitor["School"]
                        score = competitor["Score"]
                        highname = filename
    print("From {}, with a score of {}, {}. T-Score: {}  ({})".format(school, score, name, tscore, highname))

def Range():
    biggestRange = 0
    lowestRange = 1000
    bigname = ""
    lilname = ""
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename and "PreAlg" not in filename and "Prealg" not in filename:
            with open(DATA / filename, 'rb') as input_file:
                data = json.load(input_file)
                lastindex = len(data["data"])
                for competitor in data["data"]:
                    if competitor["index"] == 0:
                        high = competitor["Score"]
                    if competitor["index"] == lastindex - 1:
                        low = competitor["Score"]
                range = high - low
                if range > biggestRange:
                    biggestRange = range
                    bigname = filename
                if range < lowestRange:
                    lowestRange = range
                    lilname = filename
    return "{} with a range of {}\n{} with a range of {}".format(bigname, biggestRange, lilname, lowestRange)

def StatsPerTest(filename):
    try:
        with open(DATA / filename, 'rb') as input_file:
            data = json.load(input_file)
            scores = []
            for competitor in data["data"]:
                scores.append(competitor["Score"])
        csvfilename = filename.split(".")
        csvfilename = csvfilename[0]
        try:
            with open(DATA / (csvfilename + "-DATA.csv"), 'w') as file:
                writer = csv.writer(file)
                all = [[competitorCount(filename)], [scores], [np.mean(scores)], [np.std(scores)]]
                writer.writerows(all)
        except Exception as e:
            pass
    except Exception as e:
        print(e)

def standardDeviationAverageByLevel(level):
    standardDevList = []
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            if level in filename:
                csvfilename = filename.split(".")
                csvfilename = csvfilename[0] + "-DATA.csv"
                data = []
                with open(DATA / csvfilename, newline='') as file:
                    reader = csv.reader(file, delimiter=" ")
                    for row in reader:
                        data += row
                standardDevList += [float(data[3])]
    # print(standardDevList)
    return float(np.mean(standardDevList))

def AverageByLevel(level):
    AverageList = []
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            if level in filename:
                csvfilename = filename.split(".")
                csvfilename = csvfilename[0] + "-DATA.csv"
                data = []
                with open(DATA / csvfilename, newline='') as file:
                    reader = csv.reader(file, delimiter=" ")
                    for row in reader:
                        data += row
                AverageList += [float(data[2])]
    # print(standardDevList)
    return float(np.mean(AverageList))

def AveragePlacingScore(level):
    AverageList = []
    for filename in list:
        if "Bowl" not in filename and "Team" not in filename:
            if level in filename:
                if "Combined" in filename:
                    with open(DATA / filename, 'rb') as input_file:
                        data = json.load(input_file)
                        for competitor in data["data"]:
                            if competitor["Rank"] == "30th":
                                 AverageList.append(competitor["Score"])
                if "Invitational" in filename:
                    with open(DATA / filename, 'rb') as input_file:
                        data = json.load(input_file)
                        for competitor in data["data"]:
                            if competitor["Rank"] == "20th":
                                 AverageList.append(competitor["Score"])
    # print(AverageList)
    return np.mean(AverageList)

divisions = ["Geometry", "Algebra_2", "Precalculus", "Statistics", "Calculus"]
for division in divisions:
    print("{} -> Standard Deviation: {} Mean: {} Average Placing Score: {}".format(division, standardDeviationAverageByLevel(division), AverageByLevel(division), AveragePlacingScore(division)))

trash = findByScore()
for person in trash:
    print(person)
print("Percent of people that get 120's: {}% ({}/{})".format((len(findByScore(120)) / totalCompetitorCount()) * 100, len(findByScore(120)), totalCompetitorCount()))
highestTScore()
lowestTScore()
print(Range())
# grabdata()
