from random import choice as rc

"""
This class contains responses for the users messages and finding a response for the user.
"""


def generate_response(response_type: str, subject: str) -> str:
    """
    Generates random response from users response type and subject.
    :param response_type: str
    :param subject: str
    :return: str
    """
    return rc(response_types.get(response_type)).format(subject=subject)


greeting_responses: list[str] = [
        "Hello!, how can I assist you today?",
        "Nice to meet you! What can I help you with?",
        "Hi! I am here to assist you!",
]

general_responses: list[str] = [
        "Ok.",
        "Ok Thanks!",
        "Great.",
]

closing_responses: list[str] = [
        "Have a great day!",
        "Thanks for sharing your thought with me.",
        "Thank you for your time.",
]

product_satisfaction_responses: list[str] = [
        "I so glad you're happy with your {subject}! Is there anything about your {subject} you enjoyed in particular?",
        "That is great! We take so much pride in our {subject}\'s. What about it did you enjoy the most?",
        "Awesome! I am so glad you enjoyed your {subject}. What was the best part about the {subject}?",
]

complaint_responses: list[str] = [
        "I am sorry to hear that about your {subject}. Is there anything you can let us know to improve it?",
        "I am sorry to hear about that. What in particular was wrong with the {subject}?",
        "Thank you for sharing your complaint about are {subject}. Is there anything we could do in the future to "
        "prevent this?",
]

review_responses: list[str] = [
        "Thank you for your input. Your review will be noted. Is there anything else you wanted to talk about?",
        "Thank you for sharing, I will note your review. Anything else?",
        "I will note your review. Is there more you would like to talk about?",
]

response_types: dict[int: list] = {
        "greeting":             greeting_responses,
        "general":              general_responses,
        "closing":              closing_responses,
        "product satisfaction": product_satisfaction_responses,
        "complaint":            complaint_responses,
        "review":               review_responses,
}
