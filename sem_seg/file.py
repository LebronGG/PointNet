import os

# file_path = "/home/lebron/project/pointnet/data/indoor3d_sem_seg_hdf5_data"
file_path = "../data/stanford_indoor3d"
path_list = os.listdir(file_path)
# print(path_list)

path_name=[]
for i in path_list:
    path_name.append(i.split(".")[0])

path_name.sort()
with open("./meta/all_data_label.txt","w+") as f:
    for file_name in path_name:
        f.writelines(file_name +'.npy'+ "\n")
        print(file_name)
f.close()
