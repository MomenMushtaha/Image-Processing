""" ECOR 1051 Fall 2019

Some simple Cimpl image processing filters.
Last edited: Nov. 12, 2019
"""

from Cimpl import choose_file, load_image, copy, create_color, set_color,\
                  show, Image, get_color

def invert(image: Image) -> Image:
    """Return an inverted copy of image; that is, an image that is a colour 
    negative of the original image.
    
    >>> image = load_image(choose_file())
    >>> inverted = invert(image)
    >>> show(inverted)
    """
    new_image = copy(image)
    
    # Invert the intensities of every component in every pixel.
    for x, y, (r, g, b) in image:
        inverted = create_color(255 - r, 255 - g, 255 - b)
        set_color(new_image, x, y, inverted)
    return new_image

# Image processing filters that create grayscale images from a colour image.

def grayscale_from_red(image: Image) -> Image:
    """Return a grayscale copy of image. Each pixel's red component provides
    the RGB components for the corresponding gray shade.
    
    >>> image = load_image(choose_file()) 
    >>> gray_image = grayscale_from_red(image)
    >>> show(gray_image)     
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(r, r, r)
        set_color(new_image, x, y, gray)       
    return new_image
        
def grayscale_from_green(image: Image) -> Image:
    """Return a grayscale copy of image. Each pixel's green component provides
    the RGB components for the corresponding gray shade.
    
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale_from_green(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(g, g, g)    
        set_color(new_image, x, y, gray)       
    return new_image

def grayscale_from_blue(image: Image) -> Image:
    """Return a grayscale copy of image. Each pixel's blue component provides
    the RGB components for the corresponding gray shade.
    
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale_from_blue(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        gray = create_color(b, b, b)      
        set_color(new_image, x, y, gray)        
    return new_image

def grayscale(image: Image) -> Image:
    """Return a grayscale copy of image.
   
    >>> image = load_image(choose_file())
    >>> gray_image = grayscale(image)
    >>> show(gray_image)
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:

        # Use the pixel's brightness as the value of RGB components for the 
        # shade of gray. These means that the pixel's original colour and the
        # corresponding gray shade will have approximately the same brightness.
        
        brightness = (r + g + b) // 3
        
        # or, brightness = (r + g + b) / 3
        # create_color will convert an argument of type float to an int
        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)      
    return new_image