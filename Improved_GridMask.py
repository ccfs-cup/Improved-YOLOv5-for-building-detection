
import random
import cv2
import os



def getFileList(dir, Filelist, ext=None):
    """
Get a list of files in a folder and its subfolders
Enter dir: folder root directory
Enter ext: extension
Return: List of file paths
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


org_img_folder = #Source path
imglist = getFileList(org_img_folder, [], 'jpg')

def xiugai(d, b, alpha, beta,imgpath):
    im = cv2.imread(imgpath)

    width = im.shape[1]
    height = im.shape[0]
    o = random.randint(200,1800)
    p = random.randint(200,1800)
    q = random.randint(200,400)
    r = random.randint(200,400)    
    for i in range (o,q+o,d):
        for j in range (p,r+p,b):
            for l in range (i,i+alpha):
                if l>=width:
                    continue
                for n in range (j,j+beta):
                    if n>=height:
                        continue
                    im[n,l]=0
    return im

a = []
for i in range(25, 100):
    for j in range(25, 100):
        a.append([i, j])

x = []

for imgpath in imglist:
    imgname = os.path.splitext(os.path.basename(imgpath))[0]
    imgpath = #Source path
    imgpath2 = #Save path
    y = random.randint(100,2500)
    gailv = random.randint(0, 20)
    c = a[y]
    if c not in x:
        x = c + x
        d = x[0]
        b = x[1]
        alpha = int(0.5 * d)
        beta = int(0.5 * b)
        #print(d, b,alpha, beta)
        if(gailv<=30):
            img2 = xiugai(d, b, alpha, beta,imgpath)
            cv2.imwrite(imgpath2, img2) 