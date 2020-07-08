It is used to check a generic question for spelling errors. 

Method 1: infer_spaces(s):
  Arguments:The question entered by the user.
  Description:Uses dynamic programming to infer the location of spaces in a string
              without spaces.
  Method 1.1: best_match(i):
    Argument: i refers to the first i characters.
    Description:Find the best match for the i first characters, assuming cost has been built for the i-1 first characters.
    Return:Returns a pair (match_cost, match_length).
  Return: Returns the valid space seperated string.

Method 2: fn(st):
  Arguments:   A single word.
  Description: Check if the word in st is present in the  dictionary .
  Return: Returns a variable flag to indicate if the word is present or not.

Method 3: main(l1):
  Arguments:The question entered by the user.
  Description: Used to correct the mispelt  words. 
  Return: Returns the spell corrected technical words.
