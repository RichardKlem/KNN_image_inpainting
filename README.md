# KNN_image_inpainting
Image inpainting with edge focused WGAN-GP adversarial loss

This work is based on this paper: https://arxiv.org/abs/1801.07892

We improved the original model.
The work is still in the progress.

Authors: Tomáš Beránek (xberan46), Richard Klem (xklemr00)

# How to ... common stuff
1. Install requirements: `pip install -r requirements.txt`
2. Install sufficient tools like cuDNN etc. to run code on GPU. (optional)

# How to TEST
1. Download pre-trained model from GDrive and place it in `model_logs` folder.
2. Continue as described in README.md in `generative_inpainting` subfolder.

# How to TRAIN 
1. Install requirements. (optional)
2. Download dataset and insert it in `data` folder.
3. Create a `.flist` file where are paths to the dataset files (each file on one line). It could be relative paths or absolute paths.
4. Continue as described in README.md in `generative_inpainting` subfolder.

# Licensing + Credits
Part of the [generative_inpainting](https://github.com/JiahuiYu/generative_inpainting) is also [neuralgym](https://github.com/JiahuiYu/neuralgym) folder.
Both folders have origin in repositories of [Jiahui Yu](https://github.com/JiahuiYu).