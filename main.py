import os
from tkinter.filedialog import askdirectory

road = askdirectory(title="Please, Select a Folder!")

list_files = os.listdir(road)
print(list_files)

places = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Audios/Music": [".mp3"],
    "Videos": [".mp4"],
    "HEIC": [".heic"],
    "Sheets": [".xlsx",],
    "PDFs": [".pdf"],
    "Zip": [".zip"],
    "Rar": [".rar"],
    "Notes": [".txt"],
    "Cvs": [".cvs"],
    "Executable": [".exe"]
}

for file in list_files:
    name, extension = os.path.splitext(f"{road}/{file}")
    for folder in places:
        if extension in places [folder]:
            if not os.path.exists(f"{road}/{folder}"):
                os.mkdir(f"{road}/{folder}")
            os.rename(f"{road}/{file}", f"{road}/{folder}/{file}")