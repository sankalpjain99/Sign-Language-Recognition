# Sign-Language-Recognition
A project to recognize sign language using OpenCV and Convolutional neural network

## Requirements
* OpenCV
* Numpy
* Keras
* sklearn
* Google Colab

## Dataset
You can create your own dataset and train your model or use our pretrained model to recognizer letters. The dataset consists of 19200 images i.e. 800 images per letter except 'J' and 'Z'. 

## How to RUN
### Training your own model (Optional)
#### Creating Dataset
1. Specify the path for storing images in [capture.py](https://github.com/sankalpjain99/Sign-Language-Recognition/blob/master/capture.py)
2. execute the following command
```bash
python capture.py
```
3. Enter the letter for which you want to capture the images.
4. Place your hand inside the green rectangle
5. Press 'C' to start the capturing process
6. Repeat step 2-5 for all the letters except 'J' and 'Z'

#### Training Model
1. Specify the path for parent folder of images in [upload_array.py](https://github.com/sankalpjain99/Sign-Language-Recognition/blob/master/upload_array.py)
2. Execute the following command
```bash
python upload_array.py
```
3. Upload the generated .npy files on Google Drive
4. Run [recogModel.ipynb](https://github.com/sankalpjain99/Sign-Language-Recognition/blob/master/recogModel.ipynb)
5. Download the h5 file from your Google Rrive

### Recognizing Sign Language
1. Specify the path of h5 file in [recog.py](https://github.com/sankalpjain99/Sign-Language-Recognition/blob/master/recog.py)
2. Execute the following command
```bash
python recog.py
```
3. Press 'C' to start recognition
4. Press 'Q' to QUIT
