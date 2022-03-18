# ChatBot

## Description
This is a general purpouse ChatBot about retial clothing and accesories. The ChatBot is able to discuess reviews, compliants, and product satisfaction.

## Assignment 3 Description
This is a general-purpose ChatBot about retail clothing and accessories. ChatBot is able to discuss reviews, complaints, product satisfaction, and suggestions. The system has been equipt with a GUI for a cleaner interface. Other features include Porter Stemming,

## How to compile and run
Firstly download the repository. Then run the "Main.py" file.

## Assignment 3 Code Features
- the brand new GUI to intract with. (1 point)
    - The new GUI allows the user to interact with the bot with a more user-friendly medium.

    example: Can be found when running the project.

- Extra Topics the bot can suggest other atricals of clothing. (0.5 points) 
    - This helps the user better extrapolate their feelings towards the product and give the system usefull feedback.
    
    example:

- 5 responable responses outside the two main topics. (0.5 points)
    - The bot is able to understand its limitations and steer the conversation back to its understood topics.
    
    example:

- Bot can handle spelliing mistakes with Porter Stemmer. (1 point)
    - This is done with Porter Stemmer and is better at normilizing responses i.e. given a wide response variation for a single response its able to normilze the resaponse to a single normilized one that can be interperated the same no matter the variation of the response. This enables the bot to give a similar response every time.
    - The bot also uses cosine similarity to determine user setiment so if a word is misspelled it will not be critical the the overall detection of the users sentiment.
    
    example: Porter Stemmer

    liked
    likely
    liking

    will all be reduced to like.

- The bot is able to have a conversation with another bot. (3 points)
    - Using sockets or locally the bot is able to talk with another bot. This can give great insight into gaps in the bots knolage without human interaction.
    
    example:

    Bot_1: Hello!
    Bot_2: Howdy! I am here for any input on are products you have!
    Bot_1: I am sorry to hear about that. What in particular was wrong with the product?
    Bot_2: Thank you for sharing your complaint about are product. Is there anything we could do in the future to prevent this?

    As you can see testing are bot against its self yeild mixed results since its only orinted to coustomer responses and not giving complaints, reviews or satisfaction. But agianst a bot that was it would return the proper results.
