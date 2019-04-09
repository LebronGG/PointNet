import os

file_path = "/home/lebron/project/pointnet/data/indoor3d_sem_seg_hdf5_data"

path_list = os.listdir(file_path)
# print(path_list)

path_name=[]
for i in path_list:
    path_name.append(i.split(".")[0])

path_name.sort()
with open("/home/lebron/project/pointnet/data/indoor3d_sem_seg_hdf5_data/all_files.txt","w+") as f:
    for file_name in path_name:
        f.writelines(file_name +'.h5'+ "\n")
        print(file_name)
f.close()