from glob import glob
import pandas as pd
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud

files = glob('pacificArctic\\*.md')

date = []
keywords = []
for file in files:
    with  open(file,'r') as f:
        date.append(f.read().split('\n')[0])
        f.seek(0)
        keywords.append(f.read().split('\n')[6].split(', '))
readDates = pd.DataFrame({'Date': pd.to_datetime(date), 'Keys':keywords})
unique = set(x for l in readDates.Keys for x in l)
allKeys = ','.join(str(r) for v in keywords for r in v)
topKeys = ''
numPapers = len(files)
numDays = (max(readDates.Date)-min(readDates.Date)).days+1
print('Total papers read: '+ str(len(files)) + '\n '+
     'Average per day: ' + str(numPapers/numDays) + '\n '+
     'Most common keywords: ' + str(Counter(list(itertools.chain.from_iterable(readDates.Keys.values))).most_common(5)))

# figure 1 - wordmap
wordcloud = WordCloud(background_color="white").generate(allKeys)
wordcloud.to_file("readingCloud.png")

# figure 2 - paper counts
readDates.groupby('Date').size().plot(x = 'Date', y='Number Papers', figsize = (4.5,2.5))
plt.gcf().subplots_adjust(bottom=0.2)
plt.savefig('readingTimeline.png')

# Now lets populate the readme file with the paper list
readme = 'README.md'
# searchfile = open(readme, "r")
# allText = ''
# for line in searchfile:
#     allText = allText+line
# searchfile.close()
n = 18 # These are the lines before the actual listed links
nfirstlines = []
with open(readme) as f, open("readmetmp.txt", "w") as out:
    for x in range(n):
        nfirstlines.append(next(f))
    for line in nfirstlines:
        out.write(line)
# NB : it seems that `os.rename()` complains on some systems
# if the destination file already exists.
os.remove(readme)
os.rename("readmetmp.txt", readme)

with open(readme,'a') as myFile:
    for file in files:
        f = open(file,'r')
        title = f.read().split('\n')[4]
        f.seek(0)
        sig = f.read().split('\n')[12]
        #if os.path.basename(file)[:-3] not in allText:
        myFile.write('* ['+os.path.basename(file)[:-3]+' - '+
        title+'](https://github.com/leviner/ReadingList/tree/master/pacificArctic/'+os.path.basename(file)+') \n' +
        '     * '+ sig + ' \n')
