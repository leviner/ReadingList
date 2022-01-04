from glob import glob
import pandas as pd
import itertools
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib as mpl
import numpy as np
import os
from wordcloud import WordCloud

def paperStats(files): # builds the table from the md files
    testDict = {'Date':[],'fName':[],'Title':[],'Keywords':[], 'Geography':[]}
    for file in files:
        with  open(file,'r') as f:
            curFile = f.read().split('\n')
            testDict['Date'].append(pd.to_datetime(curFile[0]))
            testDict['fName'].append(os.path.basename(file)[:-3])
            testDict['Title'].append(curFile[4])
            testDict['Keywords'].append(curFile[6].split(', '))
            testDict['Geography'].append(curFile[8])
    testTable = pd.DataFrame(testDict)
    print('Total papers read: '+ str(len(testTable)) + '\n '+
         'Number of days since first record: '+ str((testTable.Date.max()- testTable.Date.min()).days+1) + '\n '+
         'Average per day: ' + str(len(testTable)/((testTable.Date.max()- testTable.Date.min()).days+1)) + '\n '+
         'Most common keywords: ' + str(Counter(list(itertools.chain.from_iterable(testTable.Keywords))).most_common(5)))
    return testTable

def wordCloud(testTable): # builds and saves the wordcloud from the md table
    listToStr = ','.join([str(elem) for elem in list(itertools.chain.from_iterable(testTable.Keywords))])
    wordcloud = WordCloud(background_color="white").generate(listToStr)
    wordcloud.to_file("readingCloud.png");


def date_heatmap(series, start=None, end=None, mean=False, ax=None, **kwargs):
    # calendar heatmap function sourced from various stacks
    DAYS = ['Sun.', 'Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.']
    MONTHS = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']

    # Combine values occurring on the same day.
    dates = series.index.floor('D')
    group = series.groupby(dates)
    series = group.mean() if mean else group.sum()

    # Parse start/end, defaulting to the min/max of the index.
    start = pd.to_datetime(start or series.index.min())
    end = pd.to_datetime(end or series.index.max())

    # We use [start, end) as a half-open interval below.
    end += np.timedelta64(1, 'D')

    # Get the previous/following Sunday to start/end.
    # Pandas and numpy day-of-week conventions are Monday=0 and Sunday=6.
    start_sun = start - np.timedelta64((start.dayofweek + 1) % 7, 'D')
    end_sun = end + np.timedelta64(7 - end.dayofweek - 1, 'D')

    # Create the heatmap and track ticks.
    num_weeks = (end_sun - start_sun).days // 7
    heatmap = np.zeros((7, num_weeks))
    ticks = {}  # week number -> month name
    for week in range(num_weeks):
        for day in range(7):
            date = start_sun + np.timedelta64(7 * week + day, 'D')
            if date.day == 1:
                ticks[week] = MONTHS[date.month - 1]
            if date.dayofyear == 1:
                ticks[week] += f'\n{date.year}'
            if start <= date < end:
                heatmap[day, week] = series.get(date, 0)

    # Get the coordinates, offset by 0.5 to align the ticks.
    y = np.arange(8) - 0.5
    x = np.arange(num_weeks + 1) - 0.5

    # Plot the heatmap. Prefer pcolormesh over imshow so that the figure can be
    # vectorized when saved to a compatible format. We must invert the axis for
    # pcolormesh, but not for imshow, so that it reads top-bottom, left-right.
    ax = ax or plt.gca()
    mesh = ax.pcolormesh(x, y, heatmap, edgecolor='k',linewidth=.005,**kwargs)
    ax.invert_yaxis()
    # Set the ticks.
    ax.set_xticks(list(ticks.keys()))
    ax.set_xticklabels(list(ticks.values()),fontsize=12)
    ax.set_yticks(np.arange(7))
    ax.set_yticklabels(DAYS,fontsize=12)

    # Set the current image and axes in the pyplot API.
    plt.sca(ax)
    plt.sci(mesh)

    return ax

def calendarMap(testTable): # Build the assembled calendar heat map. This is what will ned to be adjusted with each new year
    plt.rcParams.update({'font.size':8})
    fig = plt.figure(figsize=(14,10))
    for year in sorted(testTable.Date.dt.year.unique()):
        ax = plt.subplot(5,1,np.where(testTable.Date.dt.year.unique() == year)[0][0]+1)
        date_heatmap(testTable[testTable.Date.dt.year == year].groupby('Date').count()['fName'], start = pd.to_datetime('1-1-'+str(year)), end = pd.to_datetime('12-31-'+str(year)))
        cmap = mpl.cm.get_cmap('Blues', 5)
        plt.set_cmap(cmap)
        plt.clim(-0.5, 4.5)
        ax.set_aspect('equal')
    plt.subplots_adjust(hspace=.4)
    plt.tight_layout()
    plt.savefig('readingTimeline.png')

def buildReadMe(folders): # rebuilds the readme file
    readme = 'README.md'
    n = 15 # These are the lines before the actual listed links
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
        for folder in folders:
            myFile.write('\n## '+ folder.split('\\')[1]+' \n \n')
            for subfolder in glob(folder+'*/'):
                myFile.write('\n### '+ subfolder.split('\\')[-2]+' \n \n')
                for file in glob(subfolder+'*.md'):
                    f = open(file,'r')
                    title = f.read().split('\n')[4]
                    f.seek(0)
                    sig = f.read().split('\n')[12]
                    #if os.path.basename(file)[:-3] not in allText:
                    myFile.write('* ['+os.path.basename(file)[:-3]+' - '+
                    title+'](https://github.com/leviner/ReadingList/tree/master/'+os.path.relpath(file).replace('\\','/')+') \n' +
                    '     * '+ sig + ' \n')


testTable = paperStats(glob('papers/**/**.md', recursive=True)) # Build out the table
wordCloud(testTable) # make the wordcloud
calendarMap(testTable) # make the calendar heatmap
buildReadMe(glob('papers/*/')) # rebuild the readme
