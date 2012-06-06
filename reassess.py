# Reassessment rocktoberfest
# need date, etc.

import sys
import csv
import string
import subprocess

# Import LaTeX header
#headerlen = 32

#headerfile = open('Latex/Reassess template for python.tex', 'r')

#header = []
#for row in range(headerlen):
#    header.append(headerfile.next().strip())

# Test import
#for i in range(headerlen):
#    print header[i]

# Ask for date
date = raw_input('Choose a date: ')

# Import reassessment list
reader = csv.reader(open('../Reassessment Request - Sheet1.csv', 'U'))

reassesslist = []

for row in reader:
    reassesslist.append( row )


# Get todaylist's reassessments into a list
todaylist = []
for row in reassesslist:
    datefield = row [4]
    if datefield[0:len(date)] == date: 
        todaylist.append(row)

# Print the reassessments
#
# time: 0, name: 1, section: 2, Hstd: 3, Date: 4, Actions: 5
# Pstd: 6, #: 7, didit: 8, ready: 9, Pnum: 10
#

# Name section

namesection = []

for row in todaylist:
        namesection = []

        # name
        namesection.append('\n' + r'% Name section'+'\n' + r'\noindent {\sc {\bf {\Large ' + row[1] + r' }} \hfill')
        # standards
        namesection.append(row[6] + '}' + '\n')
        # section and date
        namesection.append(r'\noindent {\sc ' + row[2] + r' }' + r'\hfill {\large ' + date + r'}' + '\n' + r'\bigskip' + '\n')
        
        # test namesection list
        for i in range(len(namesection)):
            print namesection[i]

        # open file
        filename = ''
        filename = '/Users/jgates/desktop/latex/reassessments/' + ''.join(e for e in row[1] if e.isalnum()) + '.tex'
        print filename
        reassessfile = open(filename, 'w')
        
        # write header
        
        reassessfile.write(r'\input{/Users/jgates/desktop/latex/headerforinput.tex}')
        reassessfile.write('\n')

        # write name section
        for row in namesection:
            reassessfile.write(row)
            reassessfile.write('\n')

        # write problems
        reassessfile.write(r'% Questions section' + '\n')


        # Write standards
        reassessfile.write(r'% Questions section' + '\n')

        
        # close file
        reassessfile.write(r'\end{document}')
        reassessfile.close()
        
        # compile PDF
        filename4exp = filename[:-4]
        print filename4exp
        subprocess.check_output((r'/usr/local/texlive/2011/bin/universal-darwin/pdflatex', r'-aux-directory=/Users/jgates/desktop/latex/aux' , r'-output-directory=/Users/jgates/desktop/latex/reassessments' , filename4exp))
        

# print PDFs

