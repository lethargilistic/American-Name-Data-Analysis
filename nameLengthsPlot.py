import matplotlib.pyplot as plt

def average(numList):
    return sum(numList) / len (numList)

def readInYear(year):
    filename = "yob" + str(year) + ".txt"
    namesFile = open(filename, "r")
    nameEntries = namesFile.readlines()

    mLengths = []
    fLengths = []

    #Get each line
    for entry in nameEntries:
        #Separate each line's parts (name, sex, count)
        entry = entry.split(",")
        #Find out sex
        if entry[1] is "F":
            #Add the lengths
            fLengths.append(len(entry[0]))
        else: # is "M"
            mLengths.append(len(entry[0]))

    #Print lengths of first three names in year for test purposes
    #print(fLengths[0], fLengths[1], fLengths[2],":",mLengths[0], mLengths[1], mLengths[2],)
    return average(fLengths), average(mLengths)

def processData():
    femaleLen = []
    maleLen = []
    years = []
    year = 1880
    while year <= 2013:
        years.append(year)
        fAvg, mAvg = readInYear(year)
        femaleLen.append(fAvg)
        maleLen.append(mAvg)
        #print(fAvg,mAvg)
        #print()
        
        year += 1
    return femaleLen, maleLen, years

def plotData(femaleLen, maleLen, years):
    plt.plot(years, femaleLen)
    plt.plot(years, maleLen)
    plt.title("Name lengths in the United States (1880-2013)")
    plt.ylabel("Name length (letters)")
    plt.xlabel("Year")
    plt.show()
    
def main():
    femaleLen, maleLen, years = processData()
    plotData(femaleLen, maleLen, years)
    
    #The average overall lengths of both sexes' names
    #print(average(femaleLen))
    #print(average(maleLen))

main()
