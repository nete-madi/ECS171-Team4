
# ECS 171 (Group 4) - Web Site Start Guide

0. Have Python3 installed and be using a Linux PC(x86).
1. Download Group Code from GitHub: https://github.com/nete-madi/ECS171-Team4
2.  'Enter the following in a Linux terminal to install the web framework we used: `pip3 install django`
3. Go into the ECS171-Team4(unzipped file)'s ECS171 folder: `cd ECS171-Team4-main/ECS171Backend`
4. Make sure you have the following libraries installed:
- Matplotlib (`pip3 install matplotlib`)
- Pandas (`pip3 install pandas`)
- Tensorflow (`pip3 install tensorflow`)
- Keras (`pip3 install keras`)
- Scikit-learn (`pip3 install sklearn`)
- Extra Keras Datasets(`pip3 install extra_keras_datasets
`)
- OpenCV (`pip3 install opencv-python`)

5. Use the following command to start server: `python3 manage.py runserver` [Make sure you are in the same directory level as the manage.py in ECS171]
6. Go to `http://127.0.0.1:8000/` to view and play around with the website! Please make sure to use the empty provided form `Patient_Form.png` (It should be included the project files you downloaded of GitHub from step 1 in this guide).

The CSV is formated in the following way:
```
,0,1,2,3, [position of letters]
0,0 [the numbers of letters it has read in]
1 [debug/test line]
```

