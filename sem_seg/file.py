import os

npy_file = "../data/stanford_indoor3d"
h5_file = "../data/indoor3d_sem_seg_hdf5_data"

# with open("meta/all_data_label.txt","w+") as f:
#     for file_name in sorted(os.listdir(npy_file)):
#         f.writelines(file_name +"\n")
#         print(file_name)
# f.close()

with open("../data/indoor3d_sem_seg_hdf5_data/all_files.txt","w+") as f:
    for file_name in sorted(os.listdir(h5_file)):
        f.writelines('indoor3d_sem_seg_hdf5_data/'+file_name +"\n")
        print(file_name)
f.close()