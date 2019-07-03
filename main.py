import os
import cv2

from acutance import cal_acutance

from option import args

src = []
if os.path.isfile(args.src):
    src.append(args.src)
elif os.path.isdir(args.src):
    files = os.listdir(args.src)
    for file in files:
        src.append(os.path.join(args.src, file))
else:
    print('src error. :', args.src)

f = open(args.result, 'w')
max_val = 0.0
max_name = None
for path in src:
    image = cv2.imread(path)
    if image is None:
        continue
    name = os.path.basename(path)
    acu = cal_acutance(image)
    print(acu)
    f.write(name + '\t' + str(acu))
    if max_val < acu:
        max_val = acu
        max_name = name
