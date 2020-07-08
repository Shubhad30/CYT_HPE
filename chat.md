Answer the generic questions of the user. 

Method 1. response(question):
Arguments: The question entered by the user.
Description: Function tries to retrieve the answer for the user's query by referring to the five generic  datasets given in the below link under the english row:
  	     https://github.com/microsoft/BotBuilder-PersonalityChat/blob/master/CSharp/Datasets/README.md 
	     Every question entered is matched with the dataset and if the matching >70% then the corresponding answer is retrieved.
Return: Returns the corresponding answer from the datasets.

Method 2. greeting(sentence):
Arguments: The question entered by the user.
Description:If user's input is a greeting, return a greeting response.
Return:Returns a random response from the list of GREETING_RESPONSES list .

Method 3.genericResponse(user_response):
Arguments: The question entered by the user.
Description:Retrieves the answer for the user's query by calling the greeting() or response() functions accordingly.
Return: Returns a satisfying answer to the query.
