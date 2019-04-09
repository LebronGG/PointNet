import numpy as np
import tensorflow as tf
from model import get_model,get_loss
import time

batch_size=1
num_point=4096
xyzrgb=9

pointclouds_pl=tf.constant(np.random.rand(batch_size,num_point,xyzrgb),dtype=tf.float32)
labels_pl=tf.constant(np.random.rand(batch_size,num_point),dtype=tf.int32)
is_training_pl = tf.constant(True, shape=())
bn_decay=None
pred = get_model(pointclouds_pl, is_training_pl, bn_decay=bn_decay)
loss = get_loss(pred, labels_pl)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(10):
        t1 = time.time()
        sess.run(pred)
        # sess.run(loss)
        t2=time.time()
        print t2-t1






