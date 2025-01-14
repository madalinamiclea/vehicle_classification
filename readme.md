To train, validate and use the model, please install bellow dependences

Dependencies:

tensorflow=2.13.1
pillow=10.4.0
scipy=1.10.1

Scripts and their functionalities:

- move_images.py -> moved the datasets from ./data to train and validation folders 
- vehicle_classification.py -> used to build and train the model
- test_model.py -> used to validate the model using a predefined dataset (also test with a hardcoded image)
- interface.py -> the interface used to classify the images given as input


Steps to run:

add the data dataset into the folder where are all the binaries
run move_images.py
run vehicle_classification.py to train and create the model
run test_model.py to validate the model, get it's accuracy on the validation dataset and test it with a dummy image
run interface.py to access the model via interface and test it with your own images
