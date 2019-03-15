from PIL import Image
import numpy as np
import tensorflow as tf
import os
import os.path
import glob
import math
import h5py

def recImg():
	#silence the warning about more CPU is available on your machine
	os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

	#resizing saved user image
	image_resize()
	
	#convert to tensor
	xmanual= convert_to_tensor()

	sess = tf.InteractiveSession()
	new_saver = tf.train.import_meta_graph('superb_owl/model.ckpt.meta')
	new_saver.restore(sess, 'superb_owl/model.ckpt')

	x = sess.graph.get_tensor_by_name("input:0")
	y_conv = sess.graph.get_tensor_by_name("output:0")

	result_pre = sess.run(y_conv, feed_dict={x:xmanual})
	result = "what a superb owl! :)"

	if result_pre[0] == 1:
		result = "it's related to superbowl; it has nothing to do with owl..."

	#clean up user folder so input images don't pile up
	filelist = glob.glob(os.path.join("superb_owl/user", "*.jpg"))
	for f in filelist:
	    os.remove(f)

	return result

def image_resize():
    images = glob.glob("superb_owl/user/*.jpg")
    for image in images:
        im_path = os.path.abspath(image)
        im = Image.open(im_path)
        im = im.resize((64, 64), Image.ANTIALIAS)
        im.save(os.path.splitext(im_path)[0] + '-small.jpg')

def convert_to_tensor():
    x = np.empty((0, 64, 64, 3))
    y = np.empty((0, 2))
    directory_name = "superb_owl/user" 
    for filename in os.listdir(directory_name):
        if filename.endswith("-small.jpg"):
            img = Image.open(os.path.join(directory_name, filename)).convert('RGB')
            x = np.append(x, np.array(img).reshape((1, 64, 64, 3)), axis = 0)  
    return x