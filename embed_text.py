from PIL import Image, ImageDraw, ImageFont
import os
import shutil
import numpy as np


def text_wrap(text, font, max_width):

    lines = []
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines


file = open('/media/deepesh/8014-DD4E/Flickr7k/Flickr_7kdata.csv')
for line in file:
    line.replace("'", '')  # removing punctuation
    line1 = line.rstrip('\r\n').split('|')

    im1 = Image.open(
        '/media/deepesh/8014-DD4E/Flickr7k/flickr7k_images/'+line1[0])

    im2 = im1.copy()
    im2_w = im2.size[0]  # finding the width of the image

    # list of fonts
    list2 = ['ubuntu.mono-italic.ttf', 'ubuntu.mono-bold-italic.ttf', 'ubuntu.mono.ttf', 'ubuntu.condensed.ttf',
             'ubuntu.light.ttf', 'ubuntu.bold-italic.ttf', 'ubuntu.bold.ttf', 'ubuntu.italic.ttf', 'ubuntu.regular.ttf']

    # generating a random value
    val1 = np.random.randint(0, len(list2)-1)

    # picking a random font with fixed font size
    font = ImageFont.truetype(
        '/home/deepesh/Downloads/'+list2[val1], 25)

    # finding the height of the font
    line_height = font.getsize('hg')[1]

    text = line1[2]

    d = ImageDraw.Draw(im2)

    # function to generating multiple lines if single line width is greater than the image width.
    lines = text_wrap(text, font, im2_w)

    y = np.random.randint(0, 200)

    # list of colours
    list1 = [(255, 255, 0), (255, 0, 0), (204, 0, 102),
             (0, 204, 0), (255, 128, 0), (110, 48, 48)]

    val = np.random.randint(0, len(list1)-1)

    for text1 in lines:
        d.text((1, y), text1, font=font, fill=list1[val])
        y = y + line_height  # adding font height in case of multiple lines

    line2 = line1[0].split('.')  # getting the image name

    im2.save('/media/deepesh/8014-DD4E/Flickr7k/embedded_text/' +
             line2[0]+'_'+line1[1]+'.jpg')
