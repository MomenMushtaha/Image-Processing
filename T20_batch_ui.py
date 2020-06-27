"""ECOR 1051 - Milestone 3
Team Identifier: T20
Date: June 16, 2020
Authors:
Momin Mushtaha - 101114546
Justin Park 101013156
Maitreyi Patel 101120534

"""

from T20_image_filters import *
from Cimpl import *

THRESHOLD= 15 # provided by the Milestone 3 Description


#Function
def interface_batch(filename:str) -> None:
    """
    loads the text file which contains the name of picture and the jobs to be 
    implemented from different filter functions, saves the picture after every
    implementation and the final copy of image will be saved in the folder 
    as "test#" (in jpg)
    
    By Justin Park 101013156
    >>>interface_batch(filename)
    
    """
    batch_file = open(filename)
    
    for line in batch_file:
        items = line.split(" ")
        command = (str(items[0]), str(items[1]), str(items[2]))
        image = load_image(items[0])
        num_filters = len(items)
        new_image = items[1]
        
        # user prompts starts after index 2
        for n in range(2, num_filters):
            if items[n] == '2':
                image = two_tone(image,'LIME','MAGENTA')
                save_as(image, new_image)
                
            elif items[n] == '3':
                image = three_tone(image,'BLUE','YELLOW','GRAY')
                save_as(image, new_image)
                
            elif items[n] == 'X':
                image = extreme_contrast(image)
                save_as(image, new_image)
                
            elif items[n] == 'P':
                image = posterize(image)
                save_as(image, new_image)
                
            elif items[n] == 'T':
                image = sepia(image)
                save_as(image, new_image)   
             
            elif items[n] == 'E':
                image = detect_edges(image,THRESHOLD)
                save_as(image, new_image)
            
            elif items[n] == 'I':
                image = detect_edges_better(image,THRESHOLD) 
                save_as(image, new_image)
            
            elif items[n] == 'V':
                image = flip_vertical(image)
                save_as(image, new_image)
                
            elif items[n] == 'H':
                image = flip_horizontal(image) 
                save_as(image, new_image)


#Main Script
filename = input("Please type the name of the text file: ")
interface_batch(filename)
