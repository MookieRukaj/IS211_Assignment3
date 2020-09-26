import urllib.request
import csv
import re
import argparse

argsparser = argparse.ArgumentParser()
argsparser.add_argument('-u', '--url', help='Enter a URL linking to a .csv file.')
arguments = argsparser.parse_args()

def downloadData(url):
    csvfile = urllib.urlopen(url)
    return csvfile

def processData(csvfile):
    reader = csv.reader(csvfile)
    lnum = 0
    inum = 0

    chrome = ['Google Chrome', 0]
    internetexplorer = ['Internet Explorer', 0]
    apple = ['Safari', 0]
    mozilla = ['Firefox', 0]

    for line in reader:
        lnum += 1
        if re.search('firefox', line[2], re.I):
            mozilla[1] += 1
        elif re.search(r'MSIE', line [2]):
            internetexplorer[1] += 1
        elif re.search(r'Chrome', line[2]):
            chrome[1] += 1
        elif re.search(r'Safari', line[2]) and not re.search('Chrome', line[2]):
            apple[1] += 1


        if re.search(r"jpe?g|JPE?G|png|PNG|gif|GIF", line[0]):
            inum += 1

    img_pct = (float(inum) / lnum) * 100
    bnum = [chrome, internetexplorer, apple, mozilla]

    top = 0
    tname = ' '
    for b in bnum:
        if b[1] > top:
            top = b[1]
            tname = b[0]
        else:
            continue

    message = ('There were {} page hits today, {} percent of them were image requests. \n{} has the most hits at{}').format(lnum, img_pct, tname, top)
    print(message)

def main():
    if not arguments.url:
        raise SystemExit
    try:
        data = dataDownload(arguments.url)
    except urllib.URLError:
        print('Please enter a valid URL.')
        raise
    else:
        processData(data)
if __name__ == '__main__':
    main()



        
        
        
