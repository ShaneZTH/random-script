#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def detect_labels_local_file(photo):
    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        # print(image.read())
        response = client.detect_text(Image={'Bytes': image.read()})
        
    print('Detected texts in ' + photo)  
    res = []  
    for label in response['TextDetections']:
        if (label['Confidence'] > 80):
            print (label['Type'] + ' : ' + str(label['Confidence']))
            print ('  '+ label['DetectedText'])
            res.append(label['DetectedText'])
    return res

def main():
    photo='./images/img01.png'

    print(detect_labels_local_file(photo))
    # print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()



