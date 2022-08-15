import os

def get_wsp_path () -> str :
    wsp_path = os.getcwd()
    while os.path.basename(wsp_path) != "AI_remake":
        wsp_path = os.path.dirname(wsp_path)
    return wsp_path

def remove_file ( path ) -> None:
    path : str 
    if os.path.exists(path) :
        os.remove(path)

wsp_path = get_wsp_path()
src_path = os.path.join(wsp_path,"src")

test_data_path = os.path.join(src_path,"raw_dataset","Test_data","")
train_data_path = os.path.join(src_path,"raw_datset","train_data","")

preprocessed_data_path = os.path.join(src_path,"preprocessed_data","")
print(preprocessed_data_path)


resize_test_data_out = os.path.join(preprocessed_data_path,"resize_test_data_out.npy")
test_data_framename = os.path.join(preprocessed_data_path,"test_data_framename.npy")

resize_train_data_out = os.path.join(preprocessed_data_path,"resize_train_data_out.npy")
train_data_label = os.path.join(preprocessed_data_path,"train_data_label")


