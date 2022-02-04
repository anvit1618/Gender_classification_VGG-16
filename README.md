# Gender Prediction Using Different CNN ARCHITECTURES And Their Comparison

## Motivation & Abstract

Gender prediction has been in increasing demand in the Computer Vision sphere. The need for the ability to predict the gender of a person has many uses. As the world gets more digital by the day, it is absolutely viable to make use of technology like AI to tackle such problems. 
Our motivation was to analyze why some state of the art architectures perform the way they do.

## Proposed Methodology

We aim to implement VGG-16, InceptionV3 CNN models on the “UTKFace” dataset, draw results and analyze them to conclude possible reasons for the results obtained. 

### Dataset Description
UTKFace dataset is a large-scale face dataset with a long age span (range from 0 to 116 years old). The dataset consists of over 20,000 face images with annotations of age, gender, and ethnicity.

## Algorithm/Description of the Work

### VGG-16
We used the standard VGG-16 architecture pre-trained on the ImageNet dataset for our gender classification task. Original images which were 200x200 pixels were pre-processed into size 224x224 to be fed into the model. 

All the fully connected layers and the convolutional layers were freezed, i.e- their ‘weights’ and ‘bias’  were not updated by the optimizer ‘adam’.

## InceptionV3
We used the standard InceptionV3 architecture pre-trained on the ImageNet dataset for our gender classification task. Original images which were 200x200 pixels were pre-processed into size 299x299 to be fed into the model. 

All the fully connected layers and the convolutional layers were freezed, i.e- their ‘weights’ and ‘bias’  were not updated by the optimizer ‘RMS-prop’.

## Results
<table>
  
  <tr align="center">
    <th></th>
    <th colspan="2">Train</th> 
    <th colspan="2">Vaidation</th> 
    <th colspan="2">Test</th> 
  </tr>
  <tr align="center">
    <td></td>
    <td>Accuracy</td> 
    <td>Loss</td>
    <td>Accuracy</td> 
    <td>Loss</td>
    <td>Accuracy</td> 
    <td>Loss</td>
  </tr>
  <tr align="center">
    <td>VGG-16</td>
    <td>88.9</td> 
    <td>27.13</td>
    <td>83.86</td> 
    <td>40.11</td>
    <td>80.38</td> 
    <td>48.19</td>
  </tr>
  <tr align="center">
    <td>InceptionV3</td>
    <td>89.24</td> 
    <td>26.35</td>
    <td>85.40</td> 
    <td>33.27</td>
    <td>82.93</td> 
    <td>40.51</td>
  </tr>
</table>

## Conclusion

We used two CNN architectures pre-trained on the ImageNet Dataset namely, VGG-16 and InceptionV3. Both the models with 10 epochs but both got preempted as their accuracy didn’t improve further. The results were drawn and it was found that InceptionV3 performs better. We analyzed the various factors due to which this could be.



