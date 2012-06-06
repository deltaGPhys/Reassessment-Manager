# Problem DB builder and inspector
#

import glob
import os

def searchlist(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return 'yes'
    return 'no'
    

# Build DB
# Find .tex files

os.chdir("/Users/jgates/desktop/latex/pics")

masterqlist = []
masternumlist = []

for files in glob.glob("*.tex"):
    masterqlist.append(files)

# Build dictionary with Q # as key, associated tags as list inside
problemDB = dict()
# Build dictionary with Q # as key, description as list inside
descriptionDB = dict()

# for each file:
for i in range(len(masterqlist)):
    #define filename
    filename = masterqlist[i]
    # open it
    currfile = open(filename, 'r')
    # make key, add to masternumlist
    currkey = masterqlist[i][:-4]
    masternumlist.append(currkey)
    # read tags
    tagline = currfile.readline()
    tagline = currfile.readline()
    tagline = tagline[2:]
    # read description
    desc = currfile.readline()[2:]
    descriptionDB[currkey]=desc
    # read image file
    
    # make tags into a list
    tags = tagline.split()
    # add problem to DB
    problemDB[currkey]=tags
    # close file
    currfile.close()
    
# print problemDB.items()
print 'There are', len(problemDB), 'problems in the database.'

# Get search tags
Tagtemp = raw_input('Search tags? (separate with spaces) ')
Searchtags = Tagtemp.split()

# Find problems
# define list holding problem numbers of the query results
Queryresults = masternumlist
# Perform search for all tags in list (must be present in each)
for j in range(len(Searchtags)):
    for i in masternumlist:
        if searchlist(problemDB[i],Searchtags[j]) == 'no':
            Queryresults.remove(i)

# Display problem list
for i in range(len(Queryresults)):
    print Queryresults[i], r':', descriptionDB[Queryresults[i]], r' (', ','.join(problemDB[Queryresults[i]]), r')'
# Print LaTeX document with query results

# Open document with Preview

        
    



    
# Display standard count

# Open problems



