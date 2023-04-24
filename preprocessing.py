import cv2
import numpy as np
import csv
import matplotlib.pyplot as plt
import pickle
    
def load_metadata(path):
    metadata = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            metadata.append(line)
    print(len(metadata))
    print(metadata[0])
    print(metadata[1])
    return metadata

def load_images(path, metadata):
    files = []
    # We want to skip the header line, so start from 1
    for i in range(1, len(metadata)):
        files.append(path + metadata[i][1] + '.jpg')
        labels.append(metadata[i][2])

    images = np.zeros((len(files), 90, 120, 3), dtype = int)
    # TODO: Use map
    #images = list(map(lambda file: cv2.resize(cv2.imread(file), (120, 90)), files))

    for i, file in enumerate(files):
        print(i, len(files))
        # WARNING: cv2 seems to flip width and height
        images[i] = cv2.resize(cv2.imread(file), (120, 90))

    print(images.shape)    
    return images
def load_labels(metadata):
    labels = []
    for i in range(1, len(metadata)):
        labels.append(metadata[i][2])

    # Convert String Labels into Categorical Labels
    types = {'bkl': 0, 'akiec': 1, 'bcc': 2, 'df': 3, 'mel': 4, 'nv': 5, 'vasc': 6}
    for i in range(len(labels)):
        labels[i] = types[labels[i]]
    return labels
        
    
def save_tensor(tensor):
    path = './dataset/images_resized.pickle'
    with open(path, "wb") as f:
        pickle.dump(path, f)
def load_tensor(path):
    with open(path, "rb") as f:
        images = pickle.load(f)
    return images
def report_distribution(labels):
    distribution = np.zeros((7))
    for label in labels:
        distribution[label] += 1
    for type in distribution:
        print(type, sum(distribution), 100 * type / sum(distribution))
    

if __name__ == "__main__":
    print("BME548 is shit!")    
    metadata = load_metadata('./dataset/HAM10000_metadata')
    labels = load_labels(metadata)    
    try: # Images may not be dumped yet
        images = load_tensor('./dataset/images_resized.pickle')
    except:
        images = load_images('./dataset/images/', metadata)
        save_tensor(images)
    report_distribution(labels)
