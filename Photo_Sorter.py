import os
import datetime


def see_folder(folder: str):
    all_files = []
    for folder in os.walk(folder):
        fold = folder[0].replace(" \ ".strip(), "/")
        for file in folder[-1]:
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".mp4") or file.endswith(".mov") or file.endswith(".MOV") or file.endswith(".MP4"):
                all_files.append(f"{fold}/{file}")
    return all_files


def sort_photos(files: list):
    if not os.path.exists(f"{os.getcwd()}/All_Images"):
        os.mkdir(f"{os.getcwd()}/All_Images")
    for file in files:
        try:
            date = datetime.datetime.fromtimestamp(os.stat(file).st_mtime).strftime("%d %m %Y")
            name = file.split("/")[-1]
            print(date)
            print(name)
            if not os.path.exists(f"{os.getcwd()}/All_Images/{date}"):
                os.mkdir(f"{os.getcwd()}/All_Images/{date}")
            os.replace(file, f"{os.getcwd()}/All_Images/{date}/{name}")
        except Exception as e:
            print(e)
            print(file)


def main():
    folder = input("Введите корневую папку: ")
    sort_photos(see_folder(folder))




if __name__ == '__main__':
    main()
