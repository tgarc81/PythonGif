import imageio.v3 as iio

filenames = []
i = 0
while i < 56:
  filenames.append("sukun-" + str(i) + ".png")
  i += 1

images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('sukuna.gif', images, duration = 50, loop = 0)