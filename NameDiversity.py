import matplotlib.pyplot as plt

def getYearCounts(year):
    filename = "years/yob" + str(year) + ".txt"
    namesFile = open(filename, "r")
    nameEntries = namesFile.readlines()

    fCount = 0
    mCount = 0
    aCount = 0

    fNames = []
    mNames = []
    aNames = []
    
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
                aNames.append(entry[0])
                mCount -= 1
                aCount += 1
            #No.
            else:
                fNames.append(entry[0])
                fCount += 1
        else: # is "M"
            if entry[0] in fNames:
                fNames.remove(entry[0])
                aNames.append(entry[0])
                fCount -= 1
                aCount += 1
            #No.
            else:
                mNames.append(entry[0])
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
    n = 0
    for year in years:
        years[n] *= 4
        n += 1
    plt.bar(years , fCounts, color="b", label = "Female")

    n = 0
    for year in years:
        years[n] += 1
        n += 1
    plt.bar(years, mCounts, color="g", label = "Male")

    n = 0
    for year in years:
        years[n] += 1
        n += 1
    plt.bar(years, aCounts, color="r", label = "Andro")

    #TODO: make the y-axis values correct. The above is too hacky, requiring no label.
    plt.legend(loc=0)
    plt.show()

'''Runner for the program'''
def main():
    start = 1880 #Possibly user input
    end = 1920#2013
    fCounts, mCounts, aCounts, years = getTotals(start, end)

    plotCounts(fCounts, mCounts, aCounts, years)
    
main()
