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

x = []
y = []
img = src
cv2.imwrite(os.path.join(args.dst, '00.png'), img)
for i in range(50):
    sigma = pow(2, i/2)
    x.append(i + 1)
    filter_size = 5
    img = cv2.GaussianBlur(img, (filter_size, filter_size), pow(2, 1/2))
    acu = cal_acutance(img)
    print(acu)
    name = '%02d.png' % (i + 1)
    cv2.imwrite(os.path.join(args.dst, name), cv2.putText(img.copy(), str(acu), (10, 40), 2, 1.2, 255))
    y.append(acu)

fig = plt.plot(x, y)
plt.savefig(os.path.join(args.dst, 'result.png'))