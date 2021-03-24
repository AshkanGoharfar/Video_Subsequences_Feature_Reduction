# Video_Subsequences_Feature_Reduction

# Table of contents
Sections headers will be used to reference the location of destination
- [How to use](#How-to-use)
- [Algorithms Description](#Algorithms-Description)
- [Goals](#Goals)
- [Reference](#Reference)


# How to use
Call the Main.py.
sample command is like this :

```bash
$ python skeleton camera non-automatic
```
You should pass 3 parameters which are skeleton, camera,and non-automic in this sample command, respectively. 
First paramter is choosing between using Skeletal Modelling and just Background Subtraction by deciding between 'skeleton' and 'hls', respectively.
Second paramter is choosing between using webcam and a video in UCF101 dataset by deciding between 'cam' and 'video', respectively.
Third paramter is choosing between initialing hls values thereshold automatically and non-automatically by deciding between 'auto' and 'non-automatic', respectively.

# Algorithms Description
By reviewing [1], I have implemented a program using OpenCV in order to record camera or video sequences of UCF101 dataset and finally use Background Subtraction
and Skeletal Modelling algorithms as the parts of feature reduction module. In this regard, input data for a HAR model has been generated and in this step a model
should be constructed to recognize human features.


# Goals
Use Video_Sequences.txt data in Output folder for deep learning algorithms in order to select features.


# Reference
Serpush, F., Rezaei, M. Complex Human Action Recognition Using a Hierarchical Feature Reduction and Deep Learning-BasedMethod. SN COMPUT. SCI. 2, 94 (2021).
https://doi.org/10.1007/s42979-021-00484-0
