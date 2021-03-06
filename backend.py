
# coding: utf-8

# # To install Emnist dataset and import it
# 
# ---
# 
#  Download the EMNIST data-set for recognizing Hand-Written Alpha-Numeric Characters.

# In[ ]:


get_ipython().system('pip install python-mnist')
from mnist import MNIST


# 
# 
# 
# # To handle time-related tasks
# 
# 
# ---
# 
# 
# 
# 
# 
# 

# In[ ]:


import time


# # Deliver non-fatal alerts to the user about issues encountered when running a program
# 
# ---
# 
# 

# In[ ]:


import warnings
warnings.filterwarnings('ignore')


# # Importing Libraries
# 
# ---
# 
# 
# 
# *   Tensorflow-TensorFlow is an open-source machine learning library for research and                                production. TensorFlow offers APIs to develop for desktop, mobile, web, and cloud. 
# *   Matplotlib-Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. 
# *   NumPy-NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays.
# 
# 

# In[ ]:


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


# # Load Data
# 
# ---
# 
# *  Create a new object instance: data = MNIST(data_dir="data/MNIST/").
#     This automatically downloads the files to the given dir.
#      
#   
# *   Load the testing Images and Labels  into images , labels 
# 
# 
# *   Load the training Images and Labels  into testIM , testLAB  
# 
# 

# In[ ]:


emnist = MNIST('sample_data')
images,labels = emnist.load_training()
testIM,testLAB = emnist.load_testing()


# # Conversion of training data and testing data into Numpy arrays
# 
# ---
# 
# 

# In[ ]:


n_images = np.array(images)
n_labels = np.array(labels)
testIM = np.array(testIM)
testLAB = np.array(testLAB)


# # Displaying the Numpy arrays
# 
# ---
# 
# 

# In[ ]:


print(n_images)
print(n_labels)
print(testIM)
print(testLAB)


# #Reshaping Image
# 
# ---
# 
# 
#  Taking a random image NumPy array and reshaping it to 28x28 

# In[ ]:


n_images1 = n_images[19000].reshape(28,28)


# # Plotting the image(n_image1) and showing it on Graph
# 
# ---
# 
# 

# In[ ]:


plt.imshow(n_images1,cmap='gist_gray')
plt.show()


# # Printing pixel value of any random image
#  
# 
# ---
#  
# Here we consider  0th , 455th index  pixel value of an image

# In[ ]:


n_images[0][455]


# # Min Max Scaler
# 
# ---
# 
# 
# 
# * Importing Min Max Scaler from sklearn
#   
# *  Transforms features by scaling each feature to a given range.
# *   Applying Min Max Scaling on training images to fit the pixel value between 0 and 1
# 
# 

# In[ ]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(n_images)
train_images = scaler.transform(n_images)


# #Printing the  pixel of training image
# 
# 
# ---
# 
# The pixel value of the 0th,455th index image is printed between 0 and 1 after applying Min Max Scaler
# 

# In[ ]:


train_images[0][455]


# # Min Max Scaling on test images
# 
# ---
# 
# Applying Min Max Scaling on testing images to fit the pixel value between 0 and 1

# In[ ]:


scaler.fit(testIM)
test_images = scaler.transform(testIM)


# # Printing the pixel of testing image
# 
# ---
# 
# Here we consider the pixel value of 0,567th index image

# In[ ]:


testIM[0][567]


# # Printing the random pixel of testing image
# 
# ---
# 
# 
# 
# The pixel value of 0,567th index image is printed between 0 and 1 after applying Min Max Scaler

# In[ ]:


test_images[0][567]


# # Printing total training and testing images
# 
# ---
# 
# 

# In[ ]:


print(len(train_images))
print(len(test_images))
print(len(n_labels))
print(len(testLAB))


# # Storing the training  images and labels,testing images and labels
# 
# ---
# 
# 
# 
# 
# 

# In[ ]:


get_ipython().run_line_magic('store', 'n_images')
get_ipython().run_line_magic('store', 'n_labels')
get_ipython().run_line_magic('store', 'testIM')
get_ipython().run_line_magic('store', 'testLAB')


# # Printing the  value of label of any random training image
# 
# ---
# 
# 

# In[ ]:


n_labels[11200]


# # One Hot Enoding of Labels
# 
# ---
# 
# *  The output-data is loaded as both integer class-numbers and so-called One-Hot encoded arrays. This means the class-numbers have been converted from a single integer to a vector whose length equals the number of possible classes. All elements of the vector are zero except for the $i$'th element which is 1 and means the class is $i$. For example, the One-Hot encoded labels for the first 5 images in the test-set are:
# 
# 
# * One hot encoding is a process by which categorical variables are converted into a form that could be provided to ML algorithms to do a better job in prediction.
# 
# 
# * Converting into a sparse matrix(A sparse matrix is a matrix in which many or most of the elements have a value of zero. This is in contrast to a dense matrix, where many or most of the elements have a non-zero value.)

# In[ ]:


from sklearn.preprocessing import OneHotEncoder


# In[ ]:


n_labels[0]


# In[ ]:


shaped_n_labels  = n_labels.reshape(-1,1)
enc = OneHotEncoder()
enc.fit(shaped_n_labels)
train_labels = enc.transform(shaped_n_labels).toarray()


# In[ ]:


train_labels[0]


# In[ ]:


shaped_testLAB = testLAB.reshape(-1,1)
enc.fit(shaped_testLAB)
test_labels = enc.transform(shaped_testLAB).toarray()


# In[ ]:


test_labels[0]


# # Convolutional Neural Network(CNN) Model Building
# 
# ---
# ## CNN Overview
# 
# ![CNN](http://personal.ie.cuhk.edu.hk/~ccloy/project_target_code/images/fig3.png)
# 
# Convolutional neural networks (CNNs) are the current state-of-the-art model architecture for image classification tasks. CNNs apply a series of filters to the raw pixel data of an image to extract and learn higher-level features, which the model can then use for classification.CNNs contains three components:
# 
# * Convolutional layers, which apply a specified number of convolution filters to the image. For each subregion, the layer performs a set of mathematical operations to produce a single value in the output feature map. Convolutional layers then typically apply a ReLU activation function to the output to introduce nonlinearities into the model.
# 
# 
# *  Pooling layers, which downsample the image data extracted by the convolutional layers to reduce the dimensionality of the feature map in order to decrease processing time. A commonly used pooling algorithm is max pooling, which extracts subregions of the feature map (e.g., 2x2-pixel tiles), keeps their maximum value, and discards all other values.
# 
# 
# *  Dense (fully connected) layers, which perform classification on the features extracted by the convolutional layers and downsampled by the pooling layers. In a dense layer, every node in the layer is connected to every node in the preceding layer.
# 
# 
# 
# 
# 
# 
# 

# # Methods to create each of the layer
# 
# ---
# *  init_weights().To initialize the weights of the Layer.
# 
# *  init_bias().To initialize bias for each Layer.
# 
# * conv2d(). Constructs a two-dimensional convolutional layer. Takes number of filters, filter kernel size, padding, and activation function as arguments.
# 
# *  max_pooling_2by2(). Constructs a two-dimensional pooling layer using the max-pooling algorithm. Takes pooling filter size and stride as arguments.
# 
# *  convolutional_layer():Constructs a convolution layer,calling function conv2d().Takes input shape ,kernal size,strides as input.
# 
# * normal_full_layer(). Constructs a dense layer. Takes number of neurons and activation function as arguments.

# In[ ]:


# initialising weights
def init_weights(shape):
    init_random_dist = tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(init_random_dist)
# initialising bias
def init_bias(shape):
    init_bias_vals = tf.constant(0.1,shape=shape)
    return tf.Variable(init_bias_vals)
#conv2d
def conv2d(x,W):
    #x -> [bias,height,width,channels]
    #W -> [Filter H,filter W,Channel In,Channel Out]
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')
#pooling layer
def max_pool_2by2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
#Convolutional layer
def convolutional_layer(input_x,shape):
    W=init_weights(shape)
    bias = init_bias([shape[3]])
    return tf.nn.relu(conv2d(input_x,W)+bias)
#Fully connected layer
def normal_full_layer(input_layer,size):
    input_size = int(input_layer.get_shape()[1])
    W = init_weights([input_size,size])
    bias = init_bias([size])
    return tf.matmul(input_layer,W) + bias


# # Building the CNN EMNIST Classifier
# 
# ---
# *  Convolutional Layer #1: Applies 32 5x5 filters (extracting 5x5-pixel subregions), with ReLU activation function.Image size remains 28 X 28
# 
# *  Pooling Layer #1: Performs max pooling with a 2x2 filter and stride of 2 (which specifies that pooled regions do not overlap).Image size reduces  to 14 X 14
# 
# *  Convolutional Layer #2: Applies 64 5x5 filters, with ReLU activation function.Image size remains 14 X 14
# 
# * Pooling Layer #2: Again, performs max pooling with a 2x2 filter and stride of 2.mage size reduces  to 7 X 7
# 
# *  Fully Connected Layer: Neurons in a fully connected layer have full connections to all activations in the previous layer
# 
# *    Dense Layer #1: 1,024 neurons, with dropout regularization rate of 0.5 (probability of 0.5 that any given element will be dropped during training)
# 
# 
# *  Dense Layer #2 (Logits Layer): 47 neurons, one for each alphanumeric target class (0–9 , A-Z , a-z)
# 
# 
# 
# 

# In[ ]:


#placeholders
x = tf.placeholder(tf.float32,shape=[None,784])
y_true=tf.placeholder(tf.float32,shape=[None,47])

#layers(input)
x_image = tf.reshape(x,[-1,28,28,1])

#first convolutional layer
convo_1 = convolutional_layer(x_image,shape=[5,5,1,32])
convo_1_pooling = max_pool_2by2(convo_1)

#second convolutional layer
convo_2 = convolutional_layer(convo_1_pooling,shape=[5,5,32,64])
convo_2_pooling = max_pool_2by2(convo_2)

#fully connected layer
convo_flat = tf.reshape(convo_2_pooling,[-1,7*7*64])
full_layer_one = tf.nn.relu(normal_full_layer(convo_flat,1024))
 
#drop out (used to overcome overfitting)

hold_prob = tf.placeholder(tf.float32)
full_one_dropout = tf.nn.dropout(full_layer_one,keep_prob=hold_prob)

#Logits Layer
y_pred = normal_full_layer(full_one_dropout,47)


# # Loss & Optimization
# 
# ---
# *   Loss function that measures how closely the model's predictions match the target classes. For multiclass classification problems like  EMNIST, cross entropy is typically used as the loss metric
# 
# *  Optimizers shape and mold your model into its most accurate possible form by futzing with the weights.To optimize our cost, we will use the AdamOptimizer, which is a popular optimizer along with others like Stochastic Gradient Descent and AdaGrad.
# 
# 
# 
# 
# 

# In[ ]:


import tensorflow.contrib.slim as slim

#Loss Function 
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true,logits = y_pred))

#optimizer
optimizer = tf.train.AdamOptimizer(learning_rate = 0.001)
train =optimizer.minimize(cross_entropy)

#initialise variables to execute it
init = tf.global_variables_initializer()

steps = 5000


# # Saving the model
# 
# ---
# 
# 
# 
# Saving and restoring the model

# In[ ]:


saver = tf.train.Saver()


# # Training the model
# 
# ---
# 
# *   A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated
# *   Defining session in which all variables that were declared are initialized
# *   Traing the model for 5000 epochs to calculate accuracy for a batch size of 120      images
# *   Printing the accuracy for every 100th epoch
# *   Saving the checkpoints of the model after training is done.
# 
# 
# 
# 

# In[ ]:


validation_train_accuracy_results = []
training_test_loss_results = []
training_train_accuracy_results = []
validation_test_loss_results = []
start = time.time()
with tf.Session() as sess:
    sess.run(init)
    batch_size = 120
    for i in range(steps):
        rand_ind = np.random.randint(len(train_images),size=batch_size)
        feed = {x:train_images[rand_ind],y_true:train_labels[rand_ind],hold_prob:0.5}
        sess.run(train,feed_dict=feed)
       
        
        if i%100 == 0:
            
            print("On step: {}".format(i))
            match = tf.equal(tf.argmax(y_pred,1),tf.argmax(y_true,1))
            acc = tf.reduce_mean(tf.cast(match,tf.float32))
            
            
            print("Accuracy obtained at {x} is {y} & loss is {z}".format(x=i,y=sess.run(acc,feed_dict={x:test_images,y_true:test_labels,hold_prob:1.0}),z=sess.run(cross_entropy,feed_dict= {x:test_images,y_true:test_labels,hold_prob:1.0})))
            validation_train_accuracy_results.append(sess.run(acc,feed_dict={x:test_images,y_true:test_labels,hold_prob:1.0}))
            training_train_accuracy_results.append(sess.run(acc,feed_dict={x:train_images[rand_ind],y_true:train_labels[rand_ind],hold_prob:0.5}))
            training_test_loss_results.append(sess.run(cross_entropy, feed_dict={x:train_images[rand_ind],y_true:train_labels[rand_ind],hold_prob:0.5}))
            validation_test_loss_results.append(sess.run(cross_entropy, feed_dict={x:test_images,y_true:test_labels,hold_prob:1.0}))
            print('\n')
    saver.save(sess,'model/cnn_model_1_with_tamil.ckpt')
end = time.time()
        


# # Declaring an array 

# In[ ]:


s=[] 
i=0 
while i<5000: 
      s.append(i)
      i+=100


# # Displaying & plotting Training Accuracy

# In[ ]:


training_train_accuracy_results


# In[ ]:


plt.plot(np.array(training_train_accuracy_results),s )
plt.xlabel('training Accuracy')
plt.ylabel('Epoch')
plt.title('Training Accuracy')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 1, 0, 5000])
plt.show()


# # Displaying & plotting Training loss

# In[ ]:


training_test_loss_results


# In[ ]:


plt.plot(np.array(training_test_loss_results),s )
plt.xlabel('training loss')
plt.ylabel('Epoch')
plt.title('Taining loss')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 15, 0, 5000])
plt.show()


# # Displaying Validation Accuracy

# In[ ]:


validation_train_accuracy_results


# In[ ]:


plt.plot(np.array(validation_train_accuracy_results),s )
plt.xlabel('validation Accuracy')
plt.ylabel('Epoch')
plt.title('Validation Accuracy')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([0, 1, 0, 5000])
plt.show()


# # Displaying Validation loss

# In[ ]:


validation_test_loss_results


# In[ ]:



plt.plot(np.array( validation_test_loss_results),s )
plt.xlabel('validation loss')
plt.ylabel('Epoch')
plt.title('Validation Loss')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

plt.axis([0, 6, 0, 5000])
plt.show()


# # Input Image

# In[ ]:


plt.imshow(np.array(images[1940]).reshape(28,28))
plt.show()


# In[ ]:


from sklearn.metrics import log_loss

with tf.Session() as sess:
        sess.run(init)
        saver.restore(sess, "model/cnn_model_1_with_tamil.ckpt")
        
        prediction=tf.argmax(y_pred,1)
        var = prediction.eval(feed_dict={x: [images[1940]],y_true:train_labels,hold_prob: 0.5}, session=sess)
        
labels_dict ={0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'l',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'u',31:'V',32:'W',33:'X',34:'Y',35:'Z',36:'a',37:'b',38:'d',39:'e',40:'f',41:'g',42:'h',43:'n',44:'q',45:'r',46:'t'}
print('The predicted character is : "{}"'.format(labels_dict[var[0]]))


# In[ ]:




print(tf.Session().run(y_pred))

