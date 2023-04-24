# Skin Lesion Classification Dataset Preprocessing
# What is it?
This is a repository that preprocess the raw dataset used for skin lesion classification. The processing steps are as follows.
1. Resize the images into from (450, 600, 3) to (90, 120, 3)
2. Sample the dataset to make it evenly distributed. The size of the dataset becomes 100 samples x 7 classes
3. Augment the dataset by horizontally flipping each sample, make the size of the dataset 200 samples x 7 classes
# How to use?
1. Clone the repository
```
git clone https://github.com/XianmingLuo/Skin-Lesion-Classification-Dataset-Preprocessing.git
```
2. Create directories
```
mkdir dataset
mkdir dataset/images
```
3. Download the dataset to ./dataset
4. Unzip the dataset to ./dataset
```
cd dataset
unzip dataverse_files.zip
```
5. Unzip the images to ./dataset/images
```
cd images
unzip HAM10000_images_part_1.zip
unzip HAM10000_images_part_2.zip
```
6. Run the script
```
python3 preprocess.py
```
