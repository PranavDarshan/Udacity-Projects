#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: PRANAV DARSHAN
# DATE CREATED: 3/11/2023                                 
# REVISED DATE: 4/11/2023
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic={}
    #create an empty results_dic
    
    filename_list=listdir(image_dir)
    #get the list of all files in image_dir
    
    for index in range(len(filename_list)):
        pet_label=None
        
        pet_label=filename_list[index].split("_")       
        #splits filename by underscores
        
        pet_label.pop(-1)                 
        #removes the last element that contains num.jpeg in the list
        
        for i in range(1,len(pet_label)):
            pet_label[0]+=" "+pet_label[i]              
            #used to create pet label in first elemnt of the list
        
        results_dic[filename_list[index]]=(pet_label[0].lower().strip().split("-"))  
        #adds the pet label to dict in lower case and removes any trailing whitespaces
        #.split() in the above function is used to convert values of dictionary to list which is useful in the next method
    
    # Replace None with the results_dic dictionary that you created with this
    # function

    return results_dic
