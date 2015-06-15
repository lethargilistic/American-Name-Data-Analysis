def readInYear(year, namesYear, namesCount):
    filename = "years/yob" + str(year) + ".txt"
    namesFile = open(filename, "r")
    nameEntries = namesFile.readlines()

    print(year)

    for entry in nameEntries:
        entry = entry.rstrip()
        entry = entry.split(",")
        if entry[2] == "5":
            if entry[0] not in namesYear:
                namesYear.update({entry[0] : year})
        if entry[0] in namesCount:
            namesCount.update({entry[0] : namesCount.get(entry[0]) + 1})
        else:
            namesCount.update({entry[0] : 1})

def processData(startYear, endYear):
    uniqueNamesYear = dict()  #Earliest year the name appears
    uniqueNamesTotal = dict() #Total number of times the name appears

    year = startYear

    while year <= endYear:
        readInYear(year, uniqueNamesYear, uniqueNamesTotal)
        year += 1

    finaldict = dict()
    for name in uniqueNamesYear:
        if name in uniqueNamesTotal and uniqueNamesTotal[name] == 1:
            finaldict.update({name : uniqueNamesYear[name]})

    for name in finaldict:
        print(name, finaldict[name], uniqueNamesTotal[name])

def main():
    start = 1880 #Possibly user input
    end = 2013
    processData(start, end)
    
main()
