import os
import cv2

from acutance import cal_acutance

from option import args

src = []
names = []
if os.path.isfile(args.src):
    image = cv2.imread(args.src)
    if image is not None:
        src.append(image)
        print(args.src)
        names.append(os.path.basename(args.src))
elif os.path.isdir(args.src):
    files = os.listdir(args.src)
    for file in files:
        path = os.path.join(args.src, file)
        image = cv2.imread(path)
        if image is not None:
            src.append(image)
            print(path)
            names.append(file)
else:
    print('src error. :', args.src)

f = open(args.result, 'w')
for name, image in zip(names, src):
    acu = cal_acutance(image)
    print(acu)
    f.write(name + '\t' + str(acu))
