![owl_example](https://github.com/myamma/superb-owl/blob/master/owl_example.JPG)
![ball_example](https://github.com/myamma/superb-owl/blob/master/ball_example.JPG)

# training 
if you wish to train your own CNN instead of using mine, you can look into the tensorflow code in superb_owl/training folder.
there are two .ipynb files. 'model' is used to train and test the network. 'predict_helper' is for manully testing images not in training and test sets.
the CNN has the following layers:
CONV2D -> RELU -> MAXPOOL -> CONV2D -> RELU -> MAXPOOL -> FLATTEN -> FULLYCONNECTED

# deployment
you can view deployed app in https://superb-owl-kecheng.herokuapp.com/
it may take 30 seconds to load since I am using free tier

# superb-owl
CNN classifier (superb-owl vs super-bowl)

# description
This machine learning web app (django backend; html, css, jquery, javascript frontend) is able to distinguish between images 
of owl (superb-owl) and american football (superbowl). 

# installation and running
1. create virtual environment with python 3.6.1 (version is important)
   python36 -m virtualenv venv
2. enter into virtual environment
   source venv/Scripts/activate (for windows and git bash)
3. install dependencies
   pip install -r requirements.txt
4. run server
   python manage.py runserver 3000
5. profit!!!!

# troubleshooting
If you run into some issues, you may have to create a django project from scratch by running 'django-admin startproject superb-owl',
then copy the files (python and saved tensorflwo models) over.

