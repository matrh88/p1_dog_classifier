#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
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

    #Define results_dic as an empty dictionary
    results_dic = dict()

    #Creates a list with all the filenames in the specified directory
    filenames = listdir(image_dir)

    #Creates a in index that can be used to specify which location you want to manipulate
    for idx in range(0, len(filenames),1):

      #Ignores the file if the filename starts with .
      if filenames[idx][0] != '.':
        
        #Assigns temp_pet with the first filename, makes characters lowercase and splits it on the _
        #Splitting the filename turns it into a list
        temp_pet = []
        temp_pet = filenames[idx].lower().split('_')
        new_pet = ''

        #Takes the newly created list and iterates through each word and adds it to the new pet variable.
        for word in temp_pet:
          if word.isalpha():
            new_pet += word + ' '
            #print(new_pet)

        #Removes whitespaces
        new_pet = new_pet.strip()

        #iterates through all the filenames and checks if they excist in the results dictionary, if they
        #do not, they get added with the syntax {filename : pet label}
        try:
          if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [new_pet]
          else:
            print("Key already in dictionary: '{}' with the value: '{}'".format(filenames[idx],results_dic[idx]))
        except:
          print('\nERROR\n')

      #print(pet_labels)
      #print('\n\n' + pet_labels[0])

    
    

    # Replace None with the results_dic dictionary that you created with this
    # function
    #print(results_dic)
    return results_dic
