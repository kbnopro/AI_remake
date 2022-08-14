import os

def get_wsp_path () -> str :
    wsp_path = os.getcwd()
    while os.path.basename(wsp_path) != "AI_remake":
        wsp_path = os.path.dirname(wsp_path)
    return wsp_path

wsp_path = get_wsp_path()
src_path = os.path.join(wsp_path,"src")

print(wsp_path)
