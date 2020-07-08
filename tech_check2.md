### Checks for the mispelling in technical terms and tries to correct it.

**Method :** infer_spaces(s):<br/>
 **Parameters:** The question entered by the user.<br/>
 **Returns:** Valid space seperated string.<br/>
  
**Method :** fn(st):<br/>
  **Parameters:** A single word.<br/>
  **Returns:** A variable flag to indicate if the word is present or not.<br/>

**Method :** tech_main(l1):
  **Parameters:** The question entered by the user. 
  **Returns:** Spell corrected technical words.

**Method :**spell_correct(tech_question):
  **Parameters:** The question entered by the user.
  **Return:**Spell corrected query. 

 **Method :** best_match(i):
  **Parameters:** i refers to the first i characters.
  **Return:** Returns a pair (match_cost, match_length).
     
