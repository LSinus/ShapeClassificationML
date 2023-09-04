import csv
import os
import shutil

# image_dir = "imageData"

# train_data = []
# test_data = []

# i = 0
# for image in os.listdir(image_dir):
#     label = image.split("_")
#     image_path = os.path.join(image_dir, image)

#     if i <= 70000:
#         if label[0] == "Cirlce":
#             train_data.append([image_path, 0])
        
#         if label[0] == "Heptagon":
#             train_data.append([image_path, 1])
        
#         if label[0] == "Hexagon":
#             train_data.append([image_path, 2])
        
#         if label[0] == "Nonagon":
#             train_data.append([image_path, 3])

#         if label[0] == "Octagon":
#             train_data.append([image_path, 4])
        
#         if label[0] == "Pentagon":
#             train_data.append([image_path, 5])
        
#         if label[0] == "Square":
#             train_data.append([image_path, 6])

#         if label[0] == "Star":
#             train_data.append([image_path, 7])

#         if label[0] == "Triangle":
#             train_data.append([image_path, 8])

#     else:
#         if label[0] == "Cirlce":
#             test_data.append([image_path, 0])
        
#         if label[0] == "Heptagon":
#             test_data.append([image_path, 1])
        
#         if label[0] == "Hexagon":
#             test_data.append([image_path, 2])
        
#         if label[0] == "Nonagon":
#             test_data.append([image_path, 3])

#         if label[0] == "Octagon":
#             test_data.append([image_path, 4])
        
#         if label[0] == "Pentagon":
#             test_data.append([image_path, 5])
        
#         if label[0] == "Square":
#             test_data.append([image_path, 6])

#         if label[0] == "Star":
#             test_data.append([image_path, 7])

#         if label[0] == "Triangle":
#             test_data.append([image_path, 8])

#     i+=1

# train_file_path = "trainDataset.csv"
# test_file_path = "testDataset.csv"

# with open(train_file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["directory", "label"])
#     writer.writerows(train_data)

# with open(test_file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["directory", "label"])
#     writer.writerows(test_data)

# print("File CSV creato con successo.")

main_dir = "hand-drawn-shapes-dataset/data/"
new_dir = "dataset_images"

users = os.listdir(main_dir)

#data = []

def findDirectoryShape(shape):
    try:
        user_dir = os.path.join(main_dir, user + "/images/" + shape)
        image_dir = os.listdir(user_dir)
        for image in image_dir:
            
            dir = os.path.join(user_dir + "/" + image)
            shutil.copy(dir, new_dir + "/" + shape)
            #data.append(data_element)
    except:
        print(shape +" directory not found at " + user)


for user in users:
    findDirectoryShape("ellipse")
    findDirectoryShape("rectangle")
    findDirectoryShape("triangle")
    
# train_file_path = "dataset.csv"

# with open(train_file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["directory", "label"])
#     writer.writerows(data)
#     print("dataset successfully created!")