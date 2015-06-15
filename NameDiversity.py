import matplotlib.pyplot as plt

def getYearCounts(year):
    filename = "years/yob" + str(year) + ".txt"
    namesFile = open(filename, "r")
    nameEntries = namesFile.readlines()

    fCount = 0
    mCount = 0
    aCount = 0

    fNames = set()
    mNames = set()
    aNames = set()
    
    #Get each line
    for entry in nameEntries:
        #Separate each line's parts (name, sex, count)
        entry = entry.split(",")
        #Find out sex
        if entry[1] is "F":
            #Is the name androgynous?
            #Yes. Remove from male list, add to andro.
            if entry[0] in mNames:
                mNames.remove(entry[0])
                aNames.add(entry[0])
                mCount -= 1
                aCount += 1
            #No.
            else:
                fNames.add(entry[0])
                fCount += 1
        else: # is "M"
            if entry[0] in fNames:
                fNames.remove(entry[0])
                aNames.add(entry[0])
                fCount -= 1
                aCount += 1
            #No.
            else:
                mNames.add(entry[0])
                mCount += 1
    return fCount, mCount, aCount

def getTotals(start, end):
    fCounts = []
    mCounts = []
    aCounts = []

    years = list(range(start, end+1))

    for year in years:
        thisYearF, thisYearM, thisYearA = getYearCounts(year)
        fCounts.append(thisYearF)
        mCounts.append(thisYearM)
        aCounts.append(thisYearA)
        print(year)

    return fCounts, mCounts, aCounts, years

def plotCounts(fCounts, mCounts, aCounts, years):
    plt.title("Name Diversity in American Names ("
              + str(years[0]) + "-" + str(years[-1]) + ")")

    labels = ["Female" "Male", "Andro"]
    yearsMinus = [i-0.2 for i in years]
    yearsPlus = [i+0.2 for i in years]
    plt.bar(yearsMinus, fCounts, width=0.2, color="b", align="center", label="Female")
    plt.bar(years, mCounts, width=0.2, color="g", align="center", label="Male")
    plt.bar(yearsPlus, aCounts, width=0.2, color="r", align="center", label="Andro")

    plt.legend(loc=0)
    plt.show()

'''Runner for the program'''
def main():
    start = 1880 #Possibly user input
    end = 2013
    fCounts, mCounts, aCounts, years = getTotals(start, end)

    plotCounts(fCounts, mCounts, aCounts, years)
    
main()
