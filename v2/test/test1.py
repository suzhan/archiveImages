import exiftool
import os
import time

#sPath =  'C:/Users/sulei/Desktop/exif-samples-master/exif-samples-master/jpg'

sPath = 'C:/Users/sulei/Desktop/aabb/'

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))



filename_list = []
# 将需整理的文件放入数组
for root, dirs, files in os.walk(sPath, True):
    # 如果没选择子文件夹,限在根目录
    for filename in files:
        filename = os.path.join(root, filename)
        f, e = os.path.splitext(filename)
        if e.lower() not in ('.jpg', '.jpeg', '.png', '.nef', '.mp4', '.3gp', '.flv', '.mkv', '.mov'):
            continue
        filename_list.append(filename)

print(filename_list)

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

files = ['C:/Users/sulei/Desktop/bb/DSC_0552.jpg', 'C:/Users/sulei/Desktop/bb/IMG_1040_2013.07.20.MOV','C:/Users/sulei/Desktop/bb/Pentax_K10D.jpg','C:/Users/sulei/Desktop/bb/DSC_1664.png']
#files = ['C:/Users/sulei/Desktop/bb/IMG_1040_2013.07.20.MOV']

filenames = ['C:/Users/sulei/Desktop/aa\DSC_0553.jpg']


#metadata = exiftool.ExifTool()

#metadata.get_metadata_batch('C:/Users/sulei/Desktop/aa/DSC_0553.jpg')

a = 0

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(filename_list)
for d in metadata:
    a = a + 1
    print("$$$")
    print('#' + str(a))
    print(d)
    #print("{:20.20} {:20.20}".format(d["SourceFile"],d["EXIF:DateTimeOriginal"]))
    #print(d["EXIF:DateTimeOriginal"])

    #print(d[])
    if d["File:FileType"] == "MOV":
        print(d["QuickTime:MediaCreateDate"])
        print(d["QuickTime:Model"])

    elif d["File:FileType"] == "JPEG":
        #print(d["EXIF:DateTimeOriginal"])
        print(d["EXIF:Model"])
        print(d["File:FileCreateDate"][:19])
        #print(d["MakerNotes:Lens"])
    elif d["File:FileType"] == "MP4":
        #print(d["EXIF:Model"])
        print(d["QuickTime:CreateDate"][:19])
        #print(d["MakerNotes:Lens"])
        print(d["Composite:GPSLatitude"])
        print(d["Composite:GPSLongitude"])
    elif d["File:FileType"] == "NEF":
        print(d["EXIF:Model"])
        print(d["EXIF:CreateDate"])
        print(d["MakerNotes:Lens"])
    else:
        pass

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))