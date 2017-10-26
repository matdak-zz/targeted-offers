import os
import csv
import io
from google.cloud import vision
from PIL import Image

file =  open ('DataMiner.csv', newline = '')
reader = csv.reader(file)
header = next(reader)
vision_client = vision.Client()

rootdir = '/users/mattvukojevic/documents/github/targeted-offers'
profileNameList = []

for row in reader:
    profileName = (row[0])
    profileNameList.append(profileName)

os.chdir('profiles')
os.system('instagram-scraper %s' % (str(profileNameList)[1:-1]))

rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    filePath = os.path.join(rootDir, dirName)
    print(len(subdirList))
    n = 0
    for subdirectory in subdirList:
        savePath = os.path.join(rootDir, str(subdirList[n]))
        completeTextFileName = os.path.join(savePath, str(subdirList[n])+".txt")
        newTextFile = open(completeTextFileName, "w")
    print(os.getcwd())
    fileList[:] = [f for f in fileList if not f.startswith('.') and not f.endswith('.log') and not f.endswith('.txt')]

    for fname in fileList:
        filePath = os.path.join(dirName, fname)
        print('\t%s' % filePath)
        with io.open(filePath,'rb') as image_file:
            content = image_file.read()
            image = vision_client.image(content=content)
            labels = image.detect_labels()
            logos = image.detect_logos()

            for label in labels:
                print(label.description)
                print(dirName)
                print(os.getcwd())
                labelDesc = label.description
                path = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s.txt' % (dirName[2:], dirName[2:])
                with open (path, 'a') as f:
                    f.write('%s, ' % labelDesc)

        newPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s.txt' % (dirName[2:], dirName[2:])
        t = open(newPath,'r')
        #while True:
        text = t.readline()
        counter = 0
        if 'travel' in text:
            imagePath = '/users/mattvukojevic/documents/github/targeted-offers/aventura.jpg'
            if counter == 0:
                counter += 1
                with Image.open(imagePath) as img:
                    img.show()
