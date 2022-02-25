from preprocess import parse_string as ps
from category import find_category as fc
from subject import find_subject as fs
from response import generate_response as gs

"""
This is the core class for the ChatBot. This is a general purpose ChatBot about retail clothing and accessories. The 
ChatBot is able to discuss reviews, compliant, and product satisfaction.
"""


def help() -> None:
    """
    prints commands to screen.
    :return: None
    """
    print("""
    Commands:
        help - display commands
        exit - exits program
    """)


def exit() -> None:
    """
    exits program by breaking main loop.
    :return: None
    """
    global running
    running = False


def main() -> None:
    """
    This is the core method for the ChatBot. Generates response based 
    on the users message.
    :return: None
    """

    print("Customer Service: Hello!")

    while running is True:
        user_message: str = ps(input("You: "))
        if user_message in commands:
            commands[user_message]()
        
        else:
            category: str = fc(user_message)
            subject: str = fs(user_message, "product")
            response: str = gs(category, subject)
            print("Customer Service: {response}".format(response=response))


running: bool = True
commands: dict[str: callable] = {
    "help": help,
    "exit": exit,
}

if __name__ == "__main__":
    main()

quit()
