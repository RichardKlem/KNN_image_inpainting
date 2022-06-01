# Image inpainting with edge focused WGAN-GP adversarial loss.
This is a school project from course Convolutional Neural Networks (CNN) at FIT BUT.

Authors: Bc. Tomáš Beránek (xberan46), Bc. Richard Klem (xklemr00)<br>
Date: 10.5.2022

Authors mentioned above are referenced by _we_, _us_, _our_ etc. furthermore and in project report (article).

Full project repository URL: [https://github.com/RichardKlem/KNN_image_inpainting](https://github.com/RichardKlem/KNN_image_inpainting).

Pretrained models on GDrive: [https://drive.google.com/drive/folders/1HzGg9QCF1qiQhGBcK8nmX742tOEnFetf?usp=sharing](https://drive.google.com/drive/folders/1HzGg9QCF1qiQhGBcK8nmX742tOEnFetf?usp=sharing).<br>
`beranek_klem.zip` is ours, `yu_et_al.zip` is Yu's model trained by us.

This project should work on Ubuntu and Windows 10. (has been tested)<br>
Submitted zip file has limited content due to the file size restriction to 2 MB.<br>
We have placed the full version of this project in the public git repository on GitHub.<br>

This reduced project contains:
   - full resource codes, 
   - README files etc.,
   - very limited example data,
   - reduced graphics quality (and potentially content) final report (article)
   - url for full version and
   - urls to pre-traned models etc.

The full version of project contains additionally: 
   - full content and full resolution final report,
   - more example data

We made two branches to compare our changes to original project.<br>
Branch with our code is named `beranek_klem` and the original one is named `yu_et_al`.<br>
Note that we have came out from a branch named `v1.0.0`, which is the correct one connected to the cited paper.<br>
The `neuralgym` repository was taken also from TFv2 PR 15 and has not been changed.<br>


# How to ... common stuff
1. Install requirements: `pip install -r requirements.txt`.
2. Install any other required library, which will be missing in your particular case.
3. (optional) Install sufficient tools like cuDNN etc. to run code on GPU.

# How to TEST
1. Download pre-trained model from GDrive and place it in `model_logs` folder.
2. Continue as described in README.md in `generative_inpainting` subfolder.

# How to TRAIN
1. Download dataset and insert it in `data` folder.
2. Create a `.flist` file where are paths to the dataset files. (each file one line)<br>
   It can be relative or absolute path.
3. Continue as described in README.md in `generative_inpainting` subfolder.

# Licensing + Credits
Part of the [generative_inpainting](https://github.com/JiahuiYu/generative_inpainting) directory is also a [neuralgym](https://github.com/JiahuiYu/neuralgym) folder.
Both folders have origin in repositories of [Jiahui Yu](https://github.com/JiahuiYu).

The difference between ours and theirs work can be seen on branches `beranek_klem` and `yu_et_al`.<br>
We take credits only on these particular changes. The rest goes to Yu and others.

Please follow the LICENCE files in all sub-folders.
