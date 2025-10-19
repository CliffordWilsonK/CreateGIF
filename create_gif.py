import imageio.v3 as iio

filenames = ['images/group1/img1.png', 'images/group1/img2.png', 'images/group1/img3.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('gif_output/nyancat.gif', images,  duration=100, loop=0)