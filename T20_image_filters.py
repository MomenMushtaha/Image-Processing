"""ECOR 1051 - Milestone 3
Team Identifier: T20
Date: June 16, 2020
Authors:
Momin Mushtaha - 101114546
Justin Park 101013156
Maitreyi Patel 101120534

"""
# Justin Park 101013156
# Maitreyi Patel 101120534
# Momin Mushtaha - 101114546


from Cimpl import *
# Create a colour and assign to a related
BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)
RED = create_color(255, 0, 0)
LIME = create_color(0, 255, 0)
BLUE = create_color(0, 0, 255)
YELLOW = create_color(255, 255, 0)
CYAN = create_color(128, 128, 128)
MAGENTA = create_color(255, 0, 255)
GRAY = create_color(128, 128, 128)

def two_tone(image: Image, colour1: str, colour2: str) -> Image :
    """
    Filter returns a copy of an image in which there are only two colours(tones).
    If a pixel's brightness is between 0 and 127, the corresponding pixel in the
    two-tone image is set to the first colour or between 128 and 255, the image
    is set to the second colour.
    
    >>> original = Image(choose_file())
    >>> two_tone_image = two_tone(original,'BLACK','WHITE')
    >>> show(two_tone_image)
    
    By Justin Park 101013156
    """
    # List of colours being used
    colour_names = ["BLACK","WHITE","RED","LIME","BLUE","YELLOW","CYAN","MAGENTA", "GRAY"]
    colours = [BLACK,WHITE,RED,LIME,BLUE,YELLOW,CYAN,MAGENTA, GRAY]
    
    # Returns the original image if the parameters of two colours are identical
    if colour1 == colour2 :
        return image
    
    # Assigning local variables with given two colours by the parameters
    for i in range(len(colour_names)) :
        if colour1 == colour_names[i] :
            set_colour1 = colours[i]
        if colour2 == colour_names[i] :
            set_colour2 = colours[i]
    
    two_tone_filtered_image = copy(image)
    
    
    for pixels in image :
        x,y,(r,g,b) = pixels
        brightness = (r + g + b)//3 # Must be an integer for determining a proper brightness range
        if brightness < 128 :
            set_color(two_tone_filtered_image, x, y, set_colour1)
        else :
            set_color(two_tone_filtered_image, x, y, set_colour2)
    
    return two_tone_filtered_image

def three_tone(image: Image, colour1: str, colour2: str, colour3: str) -> Image :
    """
    Filter returns a copy of an image in which there are only three colours(tones).
    If a pixel's brightness is between 0 and 84, the corresponding pixel in the
    three-tone image is set to the first colour or between 85 and 170, the image
    is set to the second colour or lastly is between 171 and 255, the 
    corresponding pixel in the three-tone image is set to the third colour
    >>> image = load_image(choose_file())
    >>> three_tone_image = three_tone(image,'BLACK','WHITE','GRAY')
    >>> show(three_tone_image)
        
    By Justin Park 101013156
    """
    # List of colours being used
    colour_names = ['BLACK','WHITE','RED','LIME','BLUE','YELLOW','CYAN','MAGENTA', 'GRAY']
    colours = [BLACK, WHITE, RED, LIME, BLUE, YELLOW, CYAN, MAGENTA,GRAY]
    #colours = [(0, 0, 0), (255, 255, 255), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128,128, 128)]
      
    # Returns the original image if two of three str parameters are identical
    if colour1 == colour2 :
        return image
    elif colour1 == colour3 :
        return image
    elif colour3 == colour2 :
        return image
        
    # Assigning local variables with given two colours by the parameters
    for i in range(len(colour_names)) :
        if colour1 == colour_names[i] :
            set_colour1 = colours[i]
        if colour2 == colour_names[i] :
            set_colour2 = colours[i]
        if colour3 == colour_names[i] :
            set_colour3 = colours[i]
        
    three_tone_Image = copy(image)
        
        
    for x, y, (r, g, b) in three_tone_Image:    
        if (r + g + b) // 3 < 84:
            set_color(three_tone_Image, x, y, set_colour1)     
        elif (r + g + b) // 3 < 168:
            set_color(three_tone_Image, x, y, set_colour2) 
        else:
            set_color(three_tone_Image, x, y, set_colour3) 
    return three_tone_Image    
    

def extreme_contrast(picture: Image) -> Image:
    """Returns a copy of an image where the contrast between pixels is maximized.
    By Maitreyi Patel 101120534
    
    Possible colours:
    
    white    -> (0,0,0)
    red      -> (255,0,0)
    green    -> (0,255,0)
    blue     -> (0,0,255)
    yellow   -> (255,255,0)
    purple   -> (255,0,255)
    turquise -> (0,255,255)
    black    -> (255,255,255)
    
    >>>picture = Image(choose_file())
    >>>contrast_pic = extreme_contrast(picture)
    >>>show(contrast_pic)
    """
    
    contrast_pic = copy(picture)
    for x, y, (r, g, b) in contrast_pic:
        if r <= 127:
            r = 0
        if r >= 128 and r <= 255:
            r = 255
        if g <= 127:
            g = 0
        if g >= 128 and g <= 255:
            g = 255        
        if b <= 127:
            b = 0
        if b >= 128 and b <= 255:
            b = 255    
        contrast_color = create_color(r, g, b)
        set_color(contrast_pic, x, y, contrast_color)
    return contrast_pic   

def _adjust_component(value: int) -> int:
    """ Returns the midpoint value of the quadrant a component lies. 
    By Maitreyi Patel 101120534
    >>>_adjust_component(43)
    31
    >>>_adjust_component(115)
    95
    >>>_adjust_component(154)
    159
    >>>_adjust_component(210)
    223
    """
    midpt = 0
    if 255 >= value >=192:
        midpt = 223
    if 191 >= value >=128:
        midpt = 159
    if 127 >= value >=64:
        midpt = 95 
    if 63 >= value >=0:
        midpt = 31
    return midpt
    

def posterize(picture: Image) -> Image:
    """Returns a new image composed of fewer colours. Each r,g, or b value takes on the brightness value at its corresponding midpoint.
    
    >>>picture = Image(choose_file())
    >>>new_image = posterize(picture)
    >>>show(new_image)
    By Maitreyi Patel 101120534
    """
    new_pic = copy(picture)
    red = 0
    green = 0
    blue = 0
    for x, y, (r, g, b) in picture:
        red = _adjust_component(r)
        green = _adjust_component(g)
        blue = _adjust_component(b)
        new_colour = Color(red,green,blue)
        set_color(new_pic, x, y, new_colour)
    return new_pic


def grayscale(image: Image) -> Image:
    """ by Momin Mushtaha - 101114546
    filter that applies grayscale to an image
   
    >>> picture = Image(choose_file())
    >>> new_pic = grayscale(picture)
    >>> show(new_pic)
    """
    new_image = copy(image)
    for x,y,(r,g,b) in image:
        pix_bright = (r+g+b)//3
        Gray = create_color(pix_bright,pix_bright,pix_bright)
        set_color(new_image,x,y,Gray)      
    return new_image

def sepia(image: Image) -> Image:                     
    """ by Momin Mushtaha - 101114546
    filter that adds the sepia tone to the image
   
    >>> picture = Image(choose_file())
    >>> new_pic = sepia(picture)
    >>> show(new_pic)
    """
    new_image = copy (image)
    gray_pic = grayscale(new_image)
    for x, y, (r, g, b) in gray_pic:
        if r > 191:
            set_color(gray_pic, x, y, create_color(r*1.08, g, b*0.93)) 
        if r >= 63 and r <= 191:
            set_color(gray_pic, x, y, create_color(r*1.15, g, b*0.85))            
        if r < 63:
            set_color(gray_pic, x, y, create_color(r*1.1, g, b*0.9))
    return gray_pic


def detect_edges(original_image: Image, threshold: int) -> Image :
    
    """
    Returns a copy of an image, in which the copy has been modified using the edge detection technique. For every pixel that has a pixel below it, if the contrast is high, change the top pixel's to black, if low, change it to white. The most bottom row is fixed to white.
    
    >>> original = Image(choose_file())
    >>> final_image = detect_edges(original,15)
    >>> show(final_image)
    
    By Justin Park 101013156
    """
    
    new_image = copy(original_image)
    final_image = copy(new_image)
    
    # Only two colours to be used
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # determine the width and height of the image
    pixel_width = get_width(original_image)
    pixel_height = get_height(original_image)
    
    # Pixel color change for all rows except the last row
    for x in range(pixel_width) :
        for y in range(pixel_height - 1) : # Last row must be all white
            (r1,g1,b1) = get_color(new_image, x, y) #  RGB components of the top pixel
            (r2,g2,b2) = get_color(new_image, x, y + 1) #  RGB components of the bottom pixel
            
            top_brightness = (r1 + g1 + b1)//3 
            bottom_brightness = (r2 + g2 + b2)//3 
            
            if abs(top_brightness - bottom_brightness) > threshold :
                set_color(final_image,x,y,black)
            else :
                set_color(final_image,x,y,white)                
    
    last_row = pixel_height - 1
    
    # Set the last row pixels to white
    for last_row in range(pixel_height) : 
        for i in range(pixel_width) :
            set_color(final_image,x,y,white)
            
    
    return final_image    

def detect_edges_better(original_image: Image, threshold: int) -> Image :
    
    """
    Returns a copy of an image, in which the copy has been modified using the 
    edge detection technique. For every pixel that has a pixel below or next to
    right of it, if the contrast is high, change the top pixel's to black, if 
    low, change it to white. The most bottom row is fixed to white.
    
    >>> original = Image(choose_file())
    >>> final_image = detect_edges(original,15)
    >>> show(final_image)
    
    By Maitreyi Patel 101120534
    """
    
    new_image = copy(original_image)
    final_image = copy(new_image)
    
    # Only two colours to be used
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # determine the width and height of the image
    pixel_width = get_width(original_image)
    pixel_height = get_height(original_image)
    
    # Pixel color change for all rows except the last row
    for x in range(pixel_width - 1) :
        for y in range(pixel_height - 1) : # Last row must be all white
            (r1,g1,b1) = get_color(new_image, x, y) #  RGB components of the top pixel
            (r2,g2,b2) = get_color(new_image, x, y + 1) #  RGB components of the bottom pixel
            (r3,g3,b3) = get_color(new_image, x + 1, y) #  RGB components of the bottom pixel

            top_brightness = (r1 + g1 + b1)//3 
            bottom_brightness = (r2 + g2 + b2)//3
            side_brightness = (r3 + g3 + b3)//3
            
            if abs(top_brightness - bottom_brightness) > threshold or abs(top_brightness - side_brightness) > threshold :
                set_color(final_image,x,y,black)
            else :
                set_color(final_image,x,y,white)                
    
    last_row = pixel_height - 1
    last_column = pixel_width - 1
    
    
    # Set the last row pixels to white
    for last_row in range(pixel_height) : 
        for i in range(pixel_width) :
            set_color(final_image,x,y,white)
            
    # Set the last column pixels to white
    for last_column in range(pixel_width) : 
        for j in range(pixel_height) :
            set_color(final_image,x,y,white)
            
    
    return final_image  

def flip_horizontal(picture: Image) -> Image:
    """Returns a copy of the image flipped horizontally along a vertical line.
    
    >>>picture = Image(choose_file())
    >>>flip_horizontal(picture)
    >>>show(flip_horizontal(picture))
    
    By Maitreyi Patel 101120534
    """
    
    hflip = copy(picture)
    width = get_width(picture)
    height = get_height(picture)
    
    for x in range(width):
        for y in range(height):
            original_hpixel = get_color(picture, x, y)
            hflip_pixel = (width - 1) - x
            set_color(hflip, hflip_pixel, y, original_hpixel)
           
    return hflip  

def flip_vertical(original_image: Image) -> Image :
    
    """
    Returns a copy of the received image as flipped along a horizontal line.
    
    >>> image = Image(choose_file())
    >>> final_image = flip_vertical(image)
    >>> show(final_image)
    
    By Justin Park 101013156
    """
    
    new_image = copy(original_image)
    
    pixel_width = get_width(original_image)
    pixel_height = get_height(original_image)    

    
    for x in range(pixel_width) :
        for y in range(pixel_height) :
            original_vertical_pixel = get_color(original_image, x, y)
            opposite_vertical_pixel = pixel_height - 1 - y
            set_color(new_image, x, opposite_vertical_pixel, original_vertical_pixel)
    
    return new_image


#--------------------------------------------------------------------------------------






