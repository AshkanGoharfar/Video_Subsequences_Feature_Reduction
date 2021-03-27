# Video_Subsequences_Feature_Reduction



# Table of contents
Sections headers will be used to reference the location of destination
- [How to use](#How-to-use)
- [Algorithms Description](#Algorithms-Description)
- [Goals](#Goals)
- [Reference](#Reference)


# How to use
Call the Main.py

Sample command is like this :

```bash
$ python Main.py skeleton camera non-automatic
```
You should pass 3 parameters which are skeleton, camera,and non-automic in this sample command, respectively. 

First paramter is choosing between using Skeletal Modelling and just Background Subtraction by deciding between 'skeleton' and 'hls', respectively.

Second paramter is choosing between using webcam and a video in UCF101 dataset by deciding between 'cam' and 'video', respectively.

Third paramter is choosing between initialing hls values thereshold automatically and non-automatically by deciding between 'auto' and 'non-automatic', respectively. Also, if you choose 'non-automatic', after running the code you will see a panel which has 6 trackbar for changing hls values. So, you can change the values to achieve better results for your video subsequences. 

# Algorithms Description
By reviewing [1], I have implemented a program using OpenCV in order to record camera or video sequences of UCF101 dataset and finally use Background Subtraction
and Skeletal Modelling algorithms as the parts of feature reduction module. In this regard, input data for a HAR model has been generated and in this step a model
should be constructed to recognize human features.


# Goals
Use Video_Sequences.txt data in Output folder for deep learning algorithms in order to select features.


# Reference
[1] Serpush, F., Rezaei, M. Complex Human Action Recognition Using a Hierarchical Feature Reduction and Deep Learning-BasedMethod. SN COMPUT. SCI. 2, 94 (2021).
https://doi.org/10.1007/s42979-021-00484-0
