# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:51:34 2019

@author: Akshita

Q: What are requirements to run this program?
A: This progam has been implemented using python 3.7
Hence, recommended to run it with same version installation on your computer
 
Q: How to run the program?
A: Open a command prompt. Go to the directory where this file is placed. 
   Run this program directly from command prompt using following command -
       python Memory_Maneuver_Solution.py
    
   You will see following text on the prompt -
       Waiting for input:

   Copy paste the sample input on the command prompt and press enter. You will see the 
   result on the command prompt. You can also give your own input but it should be in the
   same format as the sample input. For description of the input format read Input
   Description.

Sample Input:
    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    
Input Description:
    This is pre-order format of representing a tree's node's information. 
    It can be read as...
    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    A----------------------------------
        B----------- C-----------
                         D-----
    In this tree, A, B, C and D are nodes, where A is root node. A's metadata entires 
    are - 1, 1, 2. B's metadata entries are - 10, 11, 12. C's metadata entry is 2 
    and D's metadata entry is 99. We need to find the sum of all these entries. 
    Each node also has header information about number of it's children and 
    number of metadata entries. For example, A's number of children is 2 and number of 
    metadata entries is 3.
                         
Sample Output:
    The sum of all metadata entries is: 138.0
"""

def sum_metadata_entries(tree):
    """ Fuction to calculate sum of all metadata entries. Assumes no metadata 
    entry is missing."""
    
    # Header Stack to store number of children of node and number of metadata entries.
    header_stack = []
    
    # Add root note information to header_stack
    header_stack.append((tree[0], tree[1]))
    
    # Initiate list pointer and metadata sum
    pointer = 2
    metadata_sum = 0
    
    # Traverse through the input list while storing number of children and number of 
    # metadata entries of nodes into header stack when the number of unprocessed 
    # children is more than 0 for parent node. If all the children of the node have been 
    # processed i.e. if unprocessed children is 0 we add the metadata entries of the 
    # current node into the metadata_sum variable.
    while(header_stack):
        
        (unprocessed_children, metadata_entries_count) = header_stack.pop()
        
        if(unprocessed_children < 0):
            return
        
        elif(unprocessed_children == 0):
            
            if(metadata_entries_count < 0):
                return
            
            pointer += int(metadata_entries_count)
            
            while(metadata_entries_count):
                metadata_sum += tree[pointer - int(metadata_entries_count)]
                metadata_entries_count -= 1
            
            if(header_stack):
                (unprocessed_children, metadata_entries_count) = header_stack.pop()
                header_stack.append((unprocessed_children - 1, metadata_entries_count))
            
        else:
            header_stack.append((unprocessed_children, metadata_entries_count))
            
            header_stack.append((tree[pointer], tree[pointer+1]))
            pointer += 2
                
    # Return the sum of all metadata entries        
    return metadata_sum
            
            
if __name__ == "__main__":
    
    # Read data from the console into a list.    
    tree = list(map(float,input('Waiting for input: ').split()))
    
    # Check if there are atleast 2 numbers in the input
    if(len(tree) < 2):
        print('There should be atleast two numbers in the input, defining - '
              'number of children and number of metadata entries of the root node.')
    else:
        result = sum_metadata_entries(tree)
        
        # Check for result. If result comes out to be None, input was invalid with negative 
        # values for number of children of the nodes or number of metadata entries. Metadata
        # itself can be negative or a floating point number.
        if(result == None):
            print('Invalid input - either number of children or number of metadata entries '
                  'is negative somewhere in the input.')
        else:
            print('The sum of all metadata entries is: ', result)