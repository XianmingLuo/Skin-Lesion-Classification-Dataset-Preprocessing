# Skin Lesion Classification Dataset Preprocessing
# What is it?
This is a repository that pre-processes the raw dataset used for skin lesion classification. The processing steps are as follows.
1. Resize the images into from (450, 600, 3) to (150, 200, 3)
2. Sample the dataset to make it evenly distributed. The size of the dataset becomes 100 samples x 7 classes
3. Augment the dataset by horizontally flipping each sample, making the size of the dataset 200 samples x 7 classes
# How to use?
1. Clone the repository
```
git clone https://github.com/XianmingLuo/Skin-Lesion-Classification-Dataset-Preprocessing.git
```
2. Create directories
```
cd Skin-Lesion-Classification-Dataset-Preprocessing/
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
Sample Output:
```
Reading Metadata...
Reading Images from dumped dataset
(700, 90, 120, 3) (700,)
Class 0: 100 700 14.285714285714286%
Class 1: 100 700 14.285714285714286%
Class 2: 100 700 14.285714285714286%
Class 3: 100 700 14.285714285714286%
Class 4: 100 700 14.285714285714286%
Class 5: 100 700 14.285714285714286%
Class 6: 100 700 14.285714285714286%
Augmenting Dataset...
Class 0: 200 1400 14.285714285714286%
Class 1: 200 1400 14.285714285714286%
Class 2: 200 1400 14.285714285714286%
Class 3: 200 1400 14.285714285714286%
Class 4: 200 1400 14.285714285714286%
Class 5: 200 1400 14.285714285714286%
Class 6: 200 1400 14.285714285714286%
```
