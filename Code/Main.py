from preprocess import parse_string as ps
from category import find_category as fc
from subject import find_subject as fs
from response import generate_response as gs

"""
This is the core class for the ChatBot. This is a general purpose ChatBot about retail clothing and accessories. The 
ChatBot is able to discuss reviews, compliant, and product satisfaction.
"""


def main() -> None:
    """
    This is the core method for the ChatBot. Generates response based 
    on the users message.
    :return: None
    """

    while True:
        user_message: str = ps(input("You: "))
        if user_message == "Quit":
            break
        
        category: str = fc(user_message)
        subject: str = fs(user_message)
        response: str = gs(category, subject)
        print("Agent: {response}".format(response=response))


if __name__ == "__main__":
    main()
