import os
import csv
import io
from google.cloud import vision


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

#os.system('instagram-scraper %s' % (str(profileNameList)[1:-1]))


rootDir = '.'
for dirName, subdirList, fileList in os.walk(rootDir):
    print(dirName)
    filePath = os.path.join(rootDir, dirName)
    os.chdir('%s' % subdirList[1])
    print(os.getcwd())
    for i in subdirList:
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
                with io.open(fname,'rb') as image_file:
                    content = image_file.read()
                    image = vision_client.image(content=content)
                    labels = image.detect_labels()
                    logos = image.detect_logos()

                    for label in labels:
                       print(label.description)



    #
    # profileNameFolder = subdirList
    # print('Found directory: %s' % dirName)
    # print(os.getcwd())
    # os.chdir('%r' % (str(profileNameFolder)[2:-2]))
    # for fname in fileList:
    #     print(os.getcwd())
        #with io.open(fname,'rb') as image_file:
            #  #os.chdir(fname)
            #  content = image_file.read()
            #  image = vision_client.image(content=content)
        #print('\t%s' % fname)

# file_name = '500px-Guido_van_Rossum_OSCON_2006.jpg'
#
# with io.open(file_name,'rb') as image_file:
#   content = image_file.read()
#   image = vision_client.image(content=content)
#
# labels = image.detect_labels()
# logos = image.detect_logos()
#
# for label in labels:
#   print(label.description)
