import cv2
#import tensorflow as tf
#import os
from base_camera import BaseCamera

import sys
sys.path.append('./Google_API/object_detection/')

from Google_API.object_detection import object_detection

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        #####################################
        #load model tf graph
        #model info
        print 'loading model'
        MODEL_NAME = 'ssd_mobilenet_v1_coco_2017_11_17'
        PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

        object_detection.load_model(PATH_TO_CKPT)
        '''detection_graph = tf.Graph()
                                with detection_graph.as_default():
                                    od_graph_def = tf.GraphDef()
                                    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
                                        serialized_graph = fid.read()
                                        od_graph_def.ParseFromString(serialized_graph)
                                        tf.import_graph_def(od_graph_def, name='')'''
        #####################################

        while True:
            # read current frame
            _, img = camera.read()#np.array(img).shape   shape is (720, 1280, 3)

            #####################################
            #process, call Google_API
            print 'process...'
            img_=object_detection.image_detection(img)
            #####################################

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img_)[1].tobytes()
