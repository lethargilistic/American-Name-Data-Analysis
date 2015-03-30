import matplotlib.pyplot as plt

'''Return the average of a list of numbers'''
def average(numList):
    return sum(numList) / len (numList)

'''Read in the year's data and return the following
1) A list of the female name lengths in this year.
2) A list of the male name lengths in this year.
3) The average female name length in the year.
4) The average male name length in the year.
'''
def readInYear(year):
    filename = "years/yob" + str(year) + ".txt"
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
    return fLengths, mLengths, average(fLengths), average(mLengths)

'''Read in all of the years between the dates and return five lists:
1) A list of the lists of all female name lengths in each year.
2) A list of the lists of all male name lengths in each year.
3) A list of the average female name length in each year.
4) A list of the average male name length in each year.
5) The years.
'''
def processData(startYear, endYear):
    fYearlyLengths = []
    mYearlyLengths = []

    femaleLen = []
    maleLen = []

    years = []

    year = startYear
    while year <= endYear:
        years.append(year)
        fem, male, fAvg, mAvg = readInYear(year)

        fYearlyLengths.append(fem)
        mYearlyLengths.append(male)
        
        femaleLen.append(fAvg)
        maleLen.append(mAvg)
        #print(fAvg,mAvg)
        #print()
        
        year += 1
    return fYearlyLengths, mYearlyLengths, femaleLen, maleLen, years

'''Plot the data from the two sets as line graphs on the same plot.'''
def plotData(femaleLen, maleLen, years):
    plt.plot(years, femaleLen)
    plt.plot(years, maleLen)
    plt.legend(["Female", "Male"], loc=0)
    plt.title("Name lengths in the United States (" \
                    + str(years[0]) + "-" + str(years[-1]) + ")")
    plt.ylabel("Name length (letters)")
    plt.xlabel("Year")
    
    plt.show()

'''Runner for the program'''
def main():
    start = 1880 #Possibly user input
    end = 2013
    fYearlyData, mYearlyData, femaleLen, maleLen, years = processData(start, end)

    plotData(femaleLen, maleLen, years)
    
    #Do each cell of the yearly data actually contain all of the lengths in that year?
    #print(fYearlyData[0])
    
    #The average overall lengths of both sexes' names
    #print(average(femaleLen))
    #print(average(maleLen))

main()
