import os
import csv
import io
from google.cloud import vision
from PIL import Image
import shutil

file =  open ('DataMiner.csv', newline = '')
reader = csv.reader(file)
header = next(reader)
vision_client = vision.Client()
travelCounter = 0
graduationCounter = 0

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
            text = image.detect_text()
            landmarks = image.detect_landmarks()

            for label in labels:
                print(label.description)
                labelDesc = label.description
                path = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s-labels.txt' % (dirName[2:], dirName[2:])
                with open (path, 'a') as f:
                    f.write('Label Detected: %s, ' % labelDesc)

            for text in text:
                print(text.description)
                textDesc = text.description
                secondPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s-text.txt' % (dirName[2:], dirName[2:])
                with open (path, 'a') as f:
                    f.write('Text Detected: %s, ' % textDesc)

            for logo in logos:
                print(logo.description)
                logoDesc = logo.description
                secondPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s-text.txt' % (dirName[2:], dirName[2:])
                with open (path, 'a') as f:
                    f.write('Logo Detected: %s, ' % logoDesc)

            for landmark in landmarks:
                print(landmark.description)
                landmarkDesc = landmark.description
                secondPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s-text.txt' % (dirName[2:], dirName[2:])
                with open (path, 'a') as f:
                    f.write('Landmark Detected: %s, ' % landmarkDesc)

        newPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s/%s-labels.txt' % (dirName[2:], dirName[2:])
        t = open(newPath,'r')
        text = t.readline()

        if 'travel' in text and travelCounter == 0:
            imagePath = '/users/mattvukojevic/documents/github/targeted-offers/travel.jpg'
            profileAdPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s' % dirName[2:]
            shutil.copy2(imagePath, profileAdPath)
            travelCounter += 1
            with Image.open(imagePath) as img:
                img.show()

        if 'graduation' in text and graduationCounter == 0:
            imagePath = '/users/mattvukojevic/documents/github/targeted-offers/graduation.jpg'
            profileAdPath = '/users/mattvukojevic/documents/github/targeted-offers/profiles/%s' % dirName[2:]
            shutil.copy2(imagePath, profileAdPath)
            graduationCounter += 1
            with Image.open(imagePath) as img:
                img.show()
