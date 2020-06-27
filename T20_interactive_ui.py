"""ECOR 1051 - Milestone 3
Team Identifier: T20
Date: June 16, 2020
Authors:
Momin Mushtaha - 101114546
Justin Park 101013156
Maitreyi Patel 101120534

"""

from Cimpl import *
from T20_image_filters import *

def interface_load_image() -> Image :
    """
    By Momin Mushtaha 101114546
    
    Returns an image loaded from filename chosen after the user's command 
    through the user interface for further application of filters on the image loaded
    
    
    >>> interface_load_image()
    >>> show(loaded)
    """
    
    loaded = load_image(choose_file())
    show(loaded)
    
    return loaded

def interface_save_as(loaded: Image) -> Image: 
    """
    By Momin Mushtaha 101114546
    Save Image pict to the specified file. If no filename is supplied,
    first prompt the user to interactively choose a directory and
    filename.
    
    >>> interface_save_as()
    >>> show(loaded)
    """
    if (loaded):
        file_name = input(
            "Input the filename and its file extension "
            "(e.g. this_image.jpg): ")
        print("test")
        show(loaded)
        save_as(loaded, file_name)
        return loaded
    else:
        print("No image loaded")    
   
        
def interface_two_tone(loaded: Image) -> Image :
    """
    By Justin Park 101013156
    By Momin Mushtaha 101114546
    
    Filter returns a copy of an image in which there are only two colours(tones).
    For the milestone 3, the two tones are fixed to LIME and MAGENTA as  the replacement colours for dark
    and bright pixels respectively
    
    >>> interface_two_tone(loaded)
    >>> show(loaded)
    
    
    """
    
    # Given from the Milestone 3 Description 
    colour1 = "LIME"
    colour2 = "MAGENTA"
    
    if (loaded) :
        loaded = two_tone(loaded, colour1, colour2)
        show(loaded)
        return loaded
    else :
        print("No image loaded")

def interface_three_tone(loaded: Image) -> Image :
    """
    By Justin Park 101013156
    By Momin Mushtaha 101114546
    
    Filter returns a copy of an image in which there are only two colours(tones).
    For the milestone 3, the 3 tones are fixed to BLUE and YELLOW and GRAY 
    >>> interface_three_tone(loaded)
    >>> show(loaded)
    
    """
    
    # Given from the Milestone 3 Description 
    colour1 = "BLUE"
    colour2 = "YELLOW"
    colour3 = "GRAY"
    
    if (loaded) :
        loaded = three_tone(loaded, colour1, colour2, colour3)
        show(loaded)
        return loaded
    else :
        print("No image loaded")



def interface_extreme_contrast(loaded: Image) -> Image:
    """
    Returns an image with the extreme contrast filter on the image selected by the user, after prompting the required command. 
    
    >>>interface_extreme_contrast(loaded)
    >>>show(loaded)
    
    By Maitreyi Patel 101120534
    """
    if(loaded):
        loaded = extreme_contrast(loaded)
        show(loaded)
        return loaded
    else:
        print("No image loaded")

def interface_sepia(loaded: Image) -> Image:
    """
    Returns an image with the sepia filter on the image selected by the user, after prompting the required command. 
    
    >>>interface_sepia(loaded)
    >>>show(loaded)
    
    By Momin Mushtaha 101114546
    """
    if (loaded):
        loaded = sepia(loaded)
        show(loaded)
        return loaded
    else:
        print("No image loaded")
        
        
def interface_posterize(loaded: Image) -> Image:
    """
    Returns an image with the posterize filter on the image selected by the user after prompting the required command. 
    
    >>>interface_posterize(loaded)
    >>>show(loaded)
    
    By Maitreyi Patel 101120534
    """
    if (loaded):
        loaded = posterize(loaded)
        show(loaded)
        return loaded
    else:
        print("No image loaded")
        
def interface_detect_edges(loaded: Image) -> Image:
    """
    Returns an image with the edge detection filter on the image selected by the user, after prompting the required command. 
    
    >>>interface_detect_edges(loaded)
    >>>show(loaded)
    
    By Justin Park 101013156
    """    
    if(loaded):
        Input_threshold = float(input("Input a threshold value: "))
        loaded= detect_edges(loaded, Input_threshold)
        show(loaded)
        return loaded
    else:
        print("No image loaded")
        
        
def interface_improved_detect_edges(loaded: Image) -> Image:
    """
    Returns an image with the improved edge detection filter on the image selected by the user, after prompting the required command. 
    
    >>>interface_improved_detect_edges(loaded)
    >>>show(loaded)
    
    By Maitreyi Patel 101120534
    
    """    
    if (loaded):
        Input_threshold = float(input("Input a threshold value: "))
        loaded = detect_edges_better(loaded, Input_threshold)
        show(loaded)
        return loaded
    else:
        print("No image loaded")    

def interface_flip_vertical(loaded: Image) -> Image :
    """
    By Justin Park 101013156
    By Momin Mushtaha 101114546
    
    Returns a copy of the received image as flipped along a horizontal line.
    
    >>> interface_flip_vertical(loaded)
    >>> show(loaded)
    """
    if (loaded):
        loaded = flip_vertical(loaded)
        show(loaded)
        return loaded
    else:
        print("No image loaded")   

def interface_flip_horizontal(loaded: Image) -> Image:
    """
    Returns an image with the horizontal filter on the image selected by the user, after prompting the required command. 
    
    >>>interface_flip_horizontal(loaded)
    >>>show(loaded)
    
    By Maitreyi Patel 101120534

    """    
    if(loaded):
        loaded = flip_horizontal(loaded)
        show(loaded)
        return loaded
    else:
        print("No image loaded")    


Input = ""
this_image=None
while Input != "Q":
    Input = input(
        "L)oad image\tS)ave-as\n2)-tone\t3)-tone\tX)treme contrast\tT)int "
        "sepia\tP)osterize\nE)dge detect\tI)mproved edge detect\tV)ertical "
        "flip\tH)orizontal Flip\nQ)uit\n\n: ")
    Input = Input.upper()
    if Input == "L":
        this_image=interface_load_image()
    elif Input == "2":
        this_image=interface_two_tone(this_image)
    elif Input == "3":
        this_image=interface_three_tone(this_image)
    elif Input == "X":
        this_image=interface_extreme_contrast(this_image)
    elif Input == "T":
        this_image=interface_sepia(this_image)
    elif Input == "P":
        this_image=interface_posterize(this_image)
    elif Input == "E":
        this_image=interface_detect_edges(this_image)
    elif Input == "I":
        this_image=interface_improved_detect_edges(this_image)
    elif Input == "V":
        this_image=interface_flip_vertical(this_image)
    elif Input == "H":
        this_image=interface_flip_horizontal(this_image)
    elif Input == "S":
        interface_save_as(this_image)
    elif Input == "Q":
        pass
    else:
        print("No such command")