Koala detection  from image using Yolov8n [Namespace IT Task]
========
 
Created by
* [Md Nadim Mahamood](cse1605030@gmail.com) 
  * Begum Rokeya University, Rangpur
  
This repository contains implementation for object detection "Yolo" model along with image preprocessing. Dataset available in: https://drive.google.com/drive/folders/1UPfjYLQlhaajc16yuS7CdhDNkTlPaIHC?usp=sharing

## Brief Description
The image processing to image testing is divided into three phases i.e., the Pre-processing Phase, the Training phase
 and Testing phase and overall architecture shown below:
### Architecture diagrams

The overall architecture
![architecture]

[architecture]: ./Slide1.PNG

I) Preprocessing phase: The provided raw images are filtered by deleting several unknown files.
Following that, resize the image to a defined size i.e., 224 x 224 x 3 which matches with input size
of Yolo. Then, the image dataset is split into three sets i.e., training set, validation set and test
set. Finally, label each image by hand using labelImg tools.

II) Training Phase: In the training phase, I used pre-trained Yolov8n which
trained on the large-scale COCO dataset. This helps to identify edges or boxes more 
easily than trained on scratch because it learns from a large-scale dataset. Trained on 
train images with labels and validated with Val sets. In each train, back-propagation and 
optimization occur automatically. In addition, I trained on 50 epochs
and saved the best weight path. The Adam optimization and augmentation are defined automatically. [We can do it manually too]

III) Testing Phase: In this phase, the model performance is evaluated with 
the test set via a fine-tuned model [Best model] on the training 
set. The result is shown in the provided Google Drive link.

The  traind and predicted result shown in: https://drive.google.com/drive/folders/19yPsUu7WspPCG8jHffRm8knLqGMlZ8Yt?usp=sharing




 


### Data preparation
Download and extract images. The directory structure should be as follows. The preprocess data available in :
https://drive.google.com/drive/folders/1UPfjYLQlhaajc16yuS7CdhDNkTlPaIHC?usp=sharing
```
│images/
├──Train/
│  │   ├──26.JPEG
│  │   ├──27.JPEG
│  │   ├── ......
│  ├── ......
├──Val/
│  │   ├──293.JPEG
│  │   ├──38.JPEG
│  │   ├── ......
│  ├── ......
├──Test/
│  │   ├──193.JPEG
│  │   ├──138.JPEG
│  │   ├── ......
│  ├── ......
│labels/
├──Train/
│  │   ├──26.txt
│  │   ├──27.txt
│  │   ├── ......
│  ├── ......
├──Val/
│  │   ├──293.txt
│  │   ├──38.txt
│  │   ├── ......
│  ├── ......
```


### Requirements
- torch>=1.10.0
- torchvision
- shutil
- random
- os
- ultralytics
