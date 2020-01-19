"""
This script will demonstrate how to use a pretrained model, in PyTorch, 
to make predictions. Specifically, we will be using VGG16 with a cat 
image.

References used to make this script:
PyTorch pretrained models doc:
    http://pytorch.org/docs/master/torchvision/models.html
PyTorch image transforms example:
    http://pytorch.org/tutorials/beginner/data_loading_tutorial.html#transforms
Example code:
    http://blog.outcome.io/pytorch-quick-start-classifying-an-image/    
"""

import io
from projict import *
from PIL import Image
import requests
from torch.autograd import Variable
import torchvision.models as models
import torchvision.transforms as transforms

# Random cat img taken from Google

 
            
# Class labels used when training VGG as json, courtesy of the 'Example code' link above.

def rec(im): #to get the image from the maze and acorrdeing to the letter it rutern the image then send it to another fun : sc
    i=""
    if im == 'A': 
        i= "images\image_01.jpg"
    if im == 'B':
        i= "images\image_02.jpg"   
    if im == 'C':
        i= "images\image_03.jpg"         
    if im == 'D':
        i= "images\image_04.jpg"    
    if im == 'E':
        i= "images\image_05.jpg"    
    if im == 'F':
        i= "images\image_06.jpg"   
    if im == 'H':
        i= "images\image_07.jpg" 
    if im == 'I':
        i= "images\image_08.jpg" 
    if im == 'J':
        i= "images\image_09.jpg" 
    if im == 'K':
        i= "images\image_10.jpg"  
    if im == 'L':
        i= "images\image_11.jpg"    
    if im == 'M':
        i= "images\image_12.jpg"         
    if im == 'N':
        i="images\image_13.jpg"    
    if im == 'O':
        i= "images\image_14.jpg"    
    if im == 'Q':
        i="images\image_15.jpg"   
    if im == 'R':
        i= "images\image_16.jpg" 
    if im == 'T':
        i= "images\image_17.jpg" 
    if im == 'U':
        i= "images\image_18.jpg" 
    if im == 'V':
        i= "images\image_19.jpg"
    if im == 'X':
        i= "images\image_20.jpg"
    if im == 'Y':
        i= "images\image_21.jpg"
    if im == 'Z':
        i="images\image_22.jpg"
    return i

# Let's get our class labels.
LABELS_URL = 'https://s3.amazonaws.com/outcome-blog/imagenet/labels.json'
response = requests.get(LABELS_URL)  # Make an HTTP GET request and store the response.
labels = {int(key): value for key, value in response.json().items()}
def sc (u):    # this function to receive the image then detected if it is obstacles or not!

    img = Image.open(u)  # Read bytes and store as an img.
    img.load()
 

    min_img_size = 224  
    transform_pipeline = transforms.Compose([transforms.Resize(min_img_size),
                                         transforms.ToTensor(),
                                         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                              std=[0.229, 0.224, 0.225])])
    img = transform_pipeline(img)


    img = img.unsqueeze(0)  

# Now that we have preprocessed our img, we need to convert it into a 
# Variable; PyTorch models expect inputs to be Variables. A PyTorch Variable is a  
# wrapper around a PyTorch Tensor.
    img = Variable(img)

# Now let's load our model and get a prediciton!
    vgg = models.vgg16(pretrained=True)  # This may take a few minutes.
    prediction = vgg(img)  # Returns a Tensor of shape (batch, num class labels)
    prediction = prediction.data.numpy().argmax()  # Our prediction will be the index of the class label with the largest value.
    print ("Type:>> ",labels[prediction])  # Converts the index to a string using our labels dict
    #print(prediction)
    return prediction
    
