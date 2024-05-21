# # CODE FOR RUNNING ON GOOGLE COLAB
PATH = '/content/drive/MyDrive/Colab_Notebooks/data'

import os

# Assign variables for train, validation, test directory
train_dir = os.path.join(PATH, 'train')
val_dir = os.path.join(PATH, 'val')
test_dir = os.path.join(PATH, 'test')

# Show file path
for i in train_dir, val_dir, test_dir:
    print(f'File paths: {i}')
print('---------------------------------')

# Assign variables for subfolders
train_msimut_dir = os.path.join(train_dir, 'MSIMUT')
train_mss_dir = os.path.join(train_dir, '1.MSS')
# Show file path
for i in train_msimut_dir, train_mss_dir:
    print(f'Subfolder paths: {i}')
print('---------------------------------')

val_msimut_dir = os.path.join(val_dir, 'MSIMUT')
val_mss_dir = os.path.join(val_dir, '1.MSS')
for i in val_msimut_dir, val_mss_dir:
    print(f'Subfolder paths: {i}')
print('---------------------------------')

test_msimut_dir = os.path.join(test_dir, 'MSIMUT')
test_mss_dir = os.path.join(test_dir, '1.MSS')
for i in test_msimut_dir, test_mss_dir:
    print(f'Subfolder paths: {i}')
print('---------------------------------')

# Check how many images are in each directory

# Assign variables for train, validation, test directory
num_msimut_train, num_mss_train = len(os.listdir(train_msimut_dir)), len(os.listdir(train_mss_dir))
num_msimut_val, num_mss_val = len(os.listdir(val_msimut_dir)), len(os.listdir(val_mss_dir))
num_msimut_test, num_mss_test = len(os.listdir(test_msimut_dir)), len(os.listdir(test_mss_dir))

# Get total number of images for each subfolder
total_train = num_msimut_train + num_mss_train
total_val = num_msimut_val + num_mss_val
total_test = num_msimut_test + num_mss_test

# Print Image Quantities
print('Total No. of Images in Each Subfolder:')
print('- Training MSIMUT: ', num_msimut_train)
print('- Training MSS: ', num_mss_train)
print('- Validation MSIMUT: ', num_msimut_val)
print('- Validation MSS: ', num_mss_val)
print('- Testing MSIMUT: ', num_msimut_test)
print('- Testing MSS: ', num_mss_test)
print('---------------------------------')
print('Total No. of Images in Each Directory:')
print('- Total Training images: ', total_train)
print('- Total Validation images: ', total_val)
print('- Total Testing images: ', total_test)