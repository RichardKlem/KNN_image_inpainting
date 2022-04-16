# KNN_image_inpainting
Image inpainting

[//]: # (TODO - doplnit nejake zakladni info, loginy, puvondi clanek apod.)

# How to ... common stuff
1. Install requirements: `pip install -r requirements.txt`
2. Install sufficient tools like cuDNN etc. to run code on GPU. (optional)

# How to TEST
1. Download pre-trained model from GDrive and place it in `model_logs` folder.
2. Continue as described in README.md in `generative_inpainting` subfolder.

# How to TRAIN 
1. Install requirements. (optional)
2. Download dataset and insert it in `data` folder.
3. Create a `.flist` file where are paths to the dataset files. (each file one line)
4. Continue as described in README.md in `generative_inpainting` subfolder.

# Licensing + Credits
Part of the generative_inpainting is also neuralgym folder.
Both folders have origin in <TODO> .