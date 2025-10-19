import imageio.v3 as iio

filenames = ['images/img_1.png', 'images/img_2.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('images/team.gif', images,  duration=500, loop=0)