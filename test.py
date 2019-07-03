import os
import matplotlib.pyplot as plt
import cv2

from option import args
from acutance import cal_acutance

src = cv2.imread(args.src)
if args.dst is None:
    args.dst = os.path.join('results', os.path.splitext(os.path.basename(args.src))[0])
if not os.path.isdir(args.dst):
    os.makedirs(args.dst)

y = []
for i in range(10):
    sigma = pow(2, i/2)
    filter_size = int(3 * sigma)
    filter_size += filter_size % 2 - 1
    img = cv2.GaussianBlur(src, (filter_size, filter_size), sigma)
    acu = cal_acutance(img)
    print(acu)
    cv2.putText(img, str(acu), (10, 40), 2, 1.2, 255)
    name = '%02d.png' % (i + 1)
    cv2.imwrite(os.path.join(args.dst, name), img)
    y.append(acu)

fig = plt.plot(range(10), y)
plt.savefig(os.path.join(args.dst, 'result.png'))