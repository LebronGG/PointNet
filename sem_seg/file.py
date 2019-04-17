import os

# file_path = "../data/indoor3d_sem_seg_hdf5_data"
# with open("../data/indoor3d_sem_seg_hdf5_data/all_files.txt","w+") as f:
#     for path_list in sorted(os.listdir(file_path)):
        # f.writelines(path_list + "\n")
        # print(path_list)
        
file_path = "../data/stanford_indoor3d"
with open("./meta/all_data_label1.txt","w+") as f:
    for path_list in sorted(os.listdir(file_path)):
        f.writelines(path_list + "\n")
        print(path_list)
