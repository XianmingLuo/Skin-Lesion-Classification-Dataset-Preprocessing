import cv2
import numpy as np
import csv
import matplotlib.pyplot as plt
import pickle
    
def load_metadata(path):
    print("Reading Metadata...")
    metadata = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            metadata.append(line)
    return metadata

def load_dataset(path, metadata):
    print("Loading Dataset...")
    files = []
    labels = []
    counters = {'bkl': 0, 'akiec': 0, 'bcc': 0, 'df': 0, 'mel': 0, 'nv': 0, 'vasc': 0}
    types = {'bkl': 0, 'akiec': 1, 'bcc': 2, 'df': 3, 'mel': 4, 'nv': 5, 'vasc': 6}
    # We want to skip the header line, so start from 1
    for i in range(1, len(metadata)):
        label = metadata[i][2]
        # Take 100 Samples for each class
        if counters[label] >= 100:
            pass
        else:            
            files.append(path + metadata[i][1] + '.jpg')
            labels.append(label)
            counters[label] += 1

    # RESIZE PARAMETER TO BE TUNED
    images = np.zeros((len(files), 150, 200, 3), dtype = float)
    encoded_labels = np.zeros((len(files)), dtype = int)
    # TODO: Use map
    #images = list(map(lambda file: cv2.resize(cv2.imread(file), (120, 90)), files))

    for i, file in enumerate(files):
        # For Progress Visualization
        if (i % 100 == 0):
            print(i, len(files))
        images[i] = normalize(resize(cv2.imread(file), (150, 200)))
        encoded_labels[i] = types[labels[i]]
        
    return images, encoded_labels        
    
def save_tensor(tensor, path):
    with open(path, "wb") as f:
        pickle.dump(tensor, f)
def load_tensor(path):
    with open(path, "rb") as f:        
        images = pickle.load(f)
    return images
def report_distribution(labels):
    distribution = np.zeros((7), dtype=int)
    for label in labels:
        distribution[label] += 1
    for i, type in enumerate(distribution):
        print('Class {}: {} {} {}%'.format(i, type, sum(distribution), 100 * type/sum(distribution)))

def horizontal_flip(image):
    return cv2.flip(image, 1)
def normalize(image):
    return image / 255
def resize(image, dim):
    # WARNING: cv2 seems to flip width and height
    return cv2.resize(image, (dim[1], dim[0]))
def augment_dataset(images, labels):
    print("Augmenting Dataset...")
    n_samples, dim1, dim2, n_channels = images.shape
    augmented_images = np.zeros((2 * n_samples, dim1, dim2, n_channels), dtype=float)
    augmented_labels = np.zeros((2 * n_samples), dtype=int)
    for i in range(n_samples):
        augmented_images[2*i] = images[i]
        augmented_labels[2*i] = labels[i]
        # Where Augmentation Happens
        # 1. Horizontal Flipping
        augmented_images[2*i+1] = horizontal_flip(images[i])
        augmented_labels[2*i+1] = labels[i]
        # TODO: Random Transformation (rotations, shearing, etc)
    return augmented_images, augmented_labels
    

if __name__ == "__main__":
    metadata = load_metadata('./dataset/HAM10000_metadata')
    try: # Images may not be dumped yet
        print("Reading Images from dumped dataset ")
        images_path = './dataset/images_resized.pickle'
        labels_path = './dataset/labels.pickle'

        images = load_tensor(images_path)
        labels = load_tensor(labels_path)
    except:
        print("Reading Images from raw dataset")
        images, labels = load_dataset('./dataset/images/', metadata)
        save_tensor(images, './dataset/images_resized.pickle')
        save_tensor(labels, './dataset/labels.pickle')
    print(images.shape, labels.shape)
    report_distribution(labels)
    augmented_images, augmented_labels = augment_dataset(images, labels)
    report_distribution(augmented_labels)
    save_tensor(augmented_images, './dataset/images_augmented.pickle')
    save_tensor(augmented_labels, './dataset/labels_augmented.pickle')
