"""
_ascii_converter_

This code is a slight modification of code shared on Hacker Earth by
Praveen Kumar. The original post where this code was shared can be found
here:
https://www.hackerearth.com/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
"""
import sys
import requests
from PIL import Image

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']


def _scale_image(image, new_width=100):
    """
    Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image


def _convert_to_grayscale(image):
    """
    convert image to grascale
    """
    return image.convert('L')


def _map_pixels_to_ascii_chars(image, range_width=25):
    """
    Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [
        ASCII_CHARS[pixel_value/range_width] for pixel_value inpixels_in_image
    ]

    return "".join(pixels_to_chars)


def _convert_image_to_ascii(image, new_width=100):
    """
    First scale image to 100px and convert it to grayscale, then map
    the grayscale image to ascii characters in an array.

    Returns the array as text where each sub-array is an individual row
    """
    scaled_image = _scale_image(image)
    grayscale_image = _convert_to_grayscale(scaled_image)

    pixels_to_chars = _map_pixels_to_ascii_chars(grayscale_image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [
        pixels_to_chars[index: index + new_width] for index in xrange(
            0, len_pixels_to_chars, new_width)
        ]

    return "\n".join(image_ascii)


def handle_image_conversion(image_file):
    """
    Convert an image to ascii characters and print image.
    """
    img = None
    try:
        img = Image.open(img_file)
    except Exception, e:
        print "Unable to open image file with error: {}".format(e)
        return

    image_ascii = _convert_image_to_ascii(img)
    print image_ascii
