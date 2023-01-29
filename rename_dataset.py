import os

root_dir="C:\\Users\\jiang\OneDrive\\컴퓨터\\hymenoptera_data\\train"
files=os.listdir(root_dir)
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        print("new folder")

#make ants file
out_dir="C:\\Users\\jiang\\OneDrive\\컴퓨터\hymenoptera_data\\train\\ants_label"
mkdir(out_dir)

#make bees file
out_dir="C:\\Users\\jiang\\OneDrive\\컴퓨터\hymenoptera_data\\train\\bees_label"
mkdir(out_dir)

# make ants label txt file
target_dir ="ants_image"
img_path = os.listdir(os.path.join(root_dir,target_dir))
label = target_dir.split('_')[0]
out_dir="ants_label"
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir,out_dir,"{}.txt".format(file_name)),'w') as f:
        f.write(label)

# make bees label txt file
target_dir ="bees_image"
img_path = os.listdir(os.path.join(root_dir,target_dir))
label = target_dir.split('_')[0]
out_dir="bees_label"
for i in img_path:
    file_name = i.split('.jpg')[0]
    with open(os.path.join(root_dir,out_dir,"{}.txt".format(file_name)),'w') as f:
        f.write(label)

