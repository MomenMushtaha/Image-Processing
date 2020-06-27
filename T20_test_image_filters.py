# Justin Park 101013156
# Maitreyi Patel 101120534
# Momin Mushtaha - 101114546

# T20_MILESTONE2_JUNE 9th 2020

from T20_image_filters import *
from unit_testing import check_equal
from Cimpl import *


def test_two_tone(original: Image, test: Image, tone1: str, tone2: str ) -> None:
    """Returns testing of function two_tone with "Passed" or "Failed"
    
    >>>original = Image(choose_file())
    >>>test = two_tone(original, "black", "white")
    >>>test_two_tone(original, test, "black", "white")
    {0} PASSED
    ------
    By Maitreyi Patel 101120534
    """
    
    colour_names = ['BLACK','WHITE','RED','LIME','BLUE','YELLOW','CYAN','MAGENTA', 'GRAY']
    colours = [BLACK, WHITE, RED, LIME, BLUE, YELLOW, CYAN, MAGENTA,GRAY]
    
    colour1 = (0,0,0)
    colour2 = (0,0,0)
    count = 0
    for i in range(len(colour_names)):
        if colour_names[i] == tone1:
            colour1 = colour_nums[i]
        elif colour_names[i] == tone2:
            colour2 = colour_nums[i]
    
    for x, y, (r,g,b) in original:
        avg = (r+g+b) // 3
        if avg <= 127: 
            colourtest = colour1
            colour_pic = get_color(test, x, y)
        else:
            colourtest = colour2
            colour_pic = get_color(test, x, y)
            
        
        if colourtest == colour_pic:
            count = count
        else:
            count +=1


def test_three_tone(original: Image, test: Image, tone1: str, tone2: str, tone3: str) -> None:
    """Returns testing of function two_tone with "Passed" or "Failed"
    
    >>>original = Image(choose_file())
    >>>test = three_tone(original, "black", "white", "gray")
    >>>test_three_tone(original, test, "black", "white", "gray")
    three_tone PASSED
    By Maitreyi Patel 101120534
    ------
    """
    
    colour_names = ["black", "white", "red", "lime", "blue", "yellow", "cyan", "magenta", "gray"]
    colour_nums = [(0,0,0), (255,255,255), (255,0,0), (0,255,0),(0,0,255),(255,255,0), (0, 255, 255), (0,255,0),(128,128,128)]
    
    colour1 = (0,0,0)
    colour2 = (0,0,0)
    colour3 = (0,0,0)
    count = 0
    for i in range(len(colour_names)):
        if colour_names[i] == tone1:
            colour1 = colour_nums[i]
        elif colour_names[i] == tone2:
            colour2 = colour_nums[i]
        elif colour_names[i] == tone3:
            colour3 = colour_nums[i]
    
    for x, y, (r,g,b) in original:
        avg = (r+g+b) // 3
        if avg <= 84:
            colourtest = colour1
            colour_pic = get_color(test, x, y)
        elif avg <= 170:
            colourtest = colour2
            colour_pic = get_color(test, x, y)
        else:
            colourtest = colour3
            colour_pic = get_color(test, x, y)
            
        
        if colourtest == colour_pic:
            count = count
        else:
            count +=1
    
    outcome = count
    expected = 0
    check_equal("three_tone", expected, outcome)
    
def test_extreme_contrast() -> None :
    """
    Tests if the filter code implemented correctly and Prints True for the 
    function, extreme_contrast(), for all the expecte colour of pixels on the image passed.
    
    >>> test_extreme_contrast()
    extreme_contrast(image) PASSED
    
    By Justin Park 101013156
    """
    original_Image = Image(choose_file())
    show(original_Image)
    extreme_contrasted_image = extreme_contrast(original_Image)
    show(extreme_contrasted_image)
    count = 0
    
    # Extreme contrasted image is inputed and will be counting number of pixels
    # that are not matching with expected brightness

    for pixel in extreme_contrasted_image :
        x, y, (r, g, b) = pixel
        contrasted_pixel = (r,g,b)
        if r >= 0 and r <= 127 :
            if g >= 0 and g <= 127 :
                if b >= 0 and b <= 127 :
                    expected_pixel = create_color(0,0,0)
                else :
                    expected_pixel = create_color(0, 0, 255)
            else :
                if b >= 0 and b <= 127 :
                    expected_pixel = create_color(0, 255, 0)
                else :
                    expected_pixel = create_color(0, 255, 255)
        else :
            if g >= 0 and g <= 127 :
                if b >= 0 and b <= 127 :
                    expected_pixel = create_color(255, 0, 0)
                else :
                    expected_pixel = create_color(255, 0, 255)
            else :
                if b >= 0 and b <= 127 :
                    expected_pixel = create_color(255, 255, 0)
                else :
                    expected_pixel = create_color(255, 255, 255)     
            
        if contrasted_pixel != expected_pixel :
            count += 1
            
    outcome = count
    expected = 0
    check_equal("extreme_contrast(image)", outcome, expected)

def test_Posterize_Filter(image: Image)-> Image:
    """
    By Momin Mushtaha 101114546
    prints 'Posterizing works correctly' if 
    all midpoints of the rgb are (31 or 95 or 159 or 223)
    """
    new_image= posterize(image)
    show(new_image)
    for x, y, (r, g, b) in new_image:
        if not((r) == 31 or 95 or 159 or 223) and ((g) == 31 or 95 or 159 or 223) and ((b) == 31 or 95 or 159 or 223):
            return False
        
    print('Posterizing works correctly') 

def test_sepia() -> None :
    """
    Tests if the filter code implemented correctly and Prints True for the 
    function, sepia(), for all the expecte colour of pixels on the image passed.
    
    >>> test_sepia()
    sepia(image) PASSED
    
    By Justin Park 101013156
    """
    original_image = Image(choose_file())
    gray_pic = grayscale(original_image)
    show(gray_pic)
    sepia_image = sepia(original_image)
    show(sepia_image)
    count = 0
       
    
    for x, y, (r, g, b) in gray_pic:
        sepia_filtered_pixel = get_color(sepia_image,x,y)
        if r > 191:
            set_color(gray_pic, x, y, create_color(r*1.08, g, b*0.93))
            testing_pixel = get_color(gray_pic,x,y)
        if r >= 63 and r <= 191:
            set_color(gray_pic, x, y, create_color(r*1.15, g, b*0.85))       
            testing_pixel = get_color(gray_pic,x,y)
        if r < 63:
            set_color(gray_pic, x, y, create_color(r*1.1, g, b*0.9))
            testing_pixel = get_color(gray_pic,x,y)
        
        if testing_pixel != sepia_filtered_pixel :
            count += 1
            
    actual = count
    expected = 0
    check_equal("sepia(image)", actual, expected)    

def test_detect_edge() -> None:
    """
    >>> test_detect_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------
    >>> test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) FAILED: expected Color(red=255, green=255,\
    blue=255), got Color(red=0, green=0, blue=0)
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------
    """
    original = create_image(5, 2)
    
    set_color(original, 0, 1, create_color(10, 30, 3))
    set_color(original, 1, 1, create_color(67, 90, 1))
    set_color(original, 2, 1, create_color(0, 2, 20))
    set_color(original, 3, 1, create_color(189, 53, 222))
    set_color(original, 4, 1, create_color(145, 136, 198))
    
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 10, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))    

    expected = create_image(5, 2)

    set_color(expected, 0, 1, create_color(10, 30, 3))
    set_color(expected, 1, 1, create_color(67, 90, 1))
    set_color(expected, 2, 1, create_color(0, 2, 20))
    set_color(expected, 3, 1, create_color(189, 53, 222))
    set_color(expected, 4, 1, create_color(145, 136, 198))
    
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))
    

    # threshold is 15

    edge = detect_edges(original, 15)

    for x, y, col in edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))



def test_filter_edge_better() -> None :
    """
    Tests if the filter code implemented correctly and Prints True for the 
    function, test_filter_edge_better(), for all the expected colour of pixels on the image passed.
    
    >>> test_filter_edge_better()
    test_edge_better(image) PASSED
    
    By Justin Park 101013156
    """
    
    original_image = Image(choose_file())
    new_image = copy(original_image)
    show(new_image)
    threshold = int(input("Please enter the threshold value(In positive integer): "))    
    edged_image = detect_edges_better(original_image,threshold)
    show(edged_image)    
    count = 0
    
    # Only two colours to be used
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # determine the width and height of the image
    pixel_width = get_width(original_image)
    pixel_height = get_height(original_image)
    
    # Pixel color change for all rows except the last row
    for x in range(pixel_width - 1) :                       # last column must be all white
        for y in range(pixel_height - 1) :                  # Last row must be all white
            (r1,g1,b1) = get_color(new_image, x, y)         #  RGB components of the top pixel
            (r2,g2,b2) = get_color(new_image, x, y + 1)     #  RGB components of the bottom pixel
            (r3,g3,b3) = get_color(new_image, x + 1, y)     #  RGB components of the bottom pixel
            
            (r4,g4,b4) = get_color(edged_image, x, y)         #  RGB components of the top pixel
            (r5,g5,b5) = get_color(edged_image, x, y + 1)     #  RGB components of the bottom pixel
            (r6,g6,b6) = get_color(edged_image, x + 1, y)     #  RGB components of the bottom pixel
            
            top_orig_brightness = (r1 + g1 + b1)//3 
            bottom_orig_brightness = (r2 + g2 + b2)//3
            right_orig_brightness = (r3 + g3 + b3)//3
            
            top_edged_brightness = (r1 + g1 + b1)//3 
            bottom_edged_brightness = (r2 + g2 + b2)//3
            right_edged_brightness = (r3 + g3 + b3)//3
            
            orig_contrasted_diff_1 = abs(top_orig_brightness - bottom_orig_brightness)
            orig_contrasted_diff_2 = abs(top_orig_brightness - right_orig_brightness)
            
            edged__contrasted_diff_1 = abs(top_edged_brightness - bottom_edged_brightness)
            edged__contrasted_diff_2 = abs(top_edged_brightness - right_edged_brightness)
            
            # Count num of pixels that two comparing pixels of images are not identical
            if orig_contrasted_diff_1 != edged__contrasted_diff_1 or orig_contrasted_diff_2 != edged__contrasted_diff_2:
                count+= 1           
    
    
    actual = count
    expected = 0
    check_equal("test_edge_better(image)", actual, expected)

def test_flip_vertical() -> None:
    """ Returns a "Passed" or "Failed", testing if the function flip_vertical correctly flips the image vertically along the horizontal line.
    
    >>>picture = Image(choose_file())
    >>>test_flip_vertical()           
    Passed
    By Maitreyi Patel 101120534
    """
    original = create_image(1, 3)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 0, 1,  create_color(1, 1, 1))
    set_color(original, 0, 2,  create_color(2, 2, 2))
      
      
    expected = create_image(1, 3)
    set_color(expected, 0, 0,  create_color(2, 2, 2))
    set_color(expected, 0, 1,  create_color(1, 1, 1))
    set_color(expected, 0, 2,  create_color(0, 0, 0))    
      
    picture_flip = flip_vertical(original)
      
    for x, y, color in picture_flip:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     color, get_color(expected, x, y))

def test_flip_horizontal():
    """Returns a "Passed" or "Failed", testing if the function flip_horizontal correctly flips the image horizontally along the vertical line.
    
    >>>picture = Image(choose_file())
    >>>test_flip_horizontal()
    Passed
    By Moe Muhstaha
    """

    creation = create_image(4, 1)
    set_color(creation, 0, 0,  create_color(27, 111, 247))
    set_color(creation, 1, 0,  create_color(167, 177, 76))
    set_color(creation, 2, 0,  create_color(45, 132, 31)) 
    set_color(creation, 3, 0,  create_color(176, 216, 41)) 
    
    expected = create_image(4, 1)
    set_color(expected, 0, 0,  create_color(176, 216, 41))
    set_color(expected, 1, 0,  create_color(45, 132, 31)) 
    set_color(expected, 2, 0,  create_color(167, 177, 76)) 
    set_color(expected, 3, 0,  create_color(27, 111, 247))
    
    horizontally_flipped = flip_horizontal(creation)
    for x, y, (r,g,b) in horizontally_flipped:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     color, get_color(expected, x, y))
          
#------------------------------------------------------     

BLACK = create_color(0, 0, 0)
WHITE = create_color(255, 255, 255)
RED = create_color(255, 0, 0)
LIME = create_color(0, 255, 0)
BLUE = create_color(0, 0, 255)
YELLOW = create_color(255, 255, 0)
CYAN = create_color(128, 128, 128)
MAGENTA = create_color(255, 0, 255)
GRAY = create_color(128, 128, 128)

# Test_Two_tone function
original = Image(choose_file())
test = two_tone(original, "black", "white")
test_two_tone(original, test, "black", "white")

# Test_Three_tone function
original = Image(choose_file())
test = three_tone(original, "black", "white", "gray")
test_three_tone(original, test, "black", "white", "gray")

# Test_Extreme_contrast function
test_extreme_contrast()

# Test_posterize
picture = Image(choose_file())
test_Posterize_Filter(picture)

# Test_Sepia
test_sepia()

# Test_edges filter
test_detect_edge() 

# Test_edges_better filter 
test_filter_edge_better() 

# Test_horizontal filter
picture = Image(choose_file())
test_flip_vertical(picture)

# Test_vertical filter
test_flip_vertical()           


