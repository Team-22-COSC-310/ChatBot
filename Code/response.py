import random
from subject import subjects

"""
This class contains responses for the users messages and finding a response for the user.
"""


def generate_response(category: str, subject: str) -> str:
    """
    Generates random response from users response type and subject
    :param str category: a category of the bots known categories
    :param str subject: a subject from the bots know categories
    :return str: a response from the category and subject
    """
    return random.choice(response_types[category]).format(subject=subject, product=random.choice(subjects))


product_satisfaction_responses: list[str] = [
    "Awesome! I am so glad you enjoyed your {subject}. What was the best part about the {subject}?",
    "That is great! We take so much pride in our {subject}'s. What about it did you enjoy the most?",
    "I am so glad you're happy with your {subject}! Is there anything about your {subject} you enjoyed in "
    "particular?",
]

complaint_responses: list[str] = [
    "I am sorry to hear about that. What in particular was wrong with the {subject}?",
    "I am sorry to hear that about your {subject}. Is there anything you can let us to improve it?",
    "Thank you for sharing your complaint about are {subject}. Is there anything we could do in the future to "
    "prevent this?",
]

review_responses: list[str] = [
    "I will note your review on are {subject}'s. Is there more you would like to talk about?",
    "Thank you for sharing, I will note your review on are {subject}'s. Is there anything else I can help you "
    "with?",
    "Thank you for your input about are {subject}'s. Your review will be noted. Is there anything else you "
    "wanted to share?",
]

suggestion_responses: list[str] = [
    "I would recommend a {product}. What do you think of that?",
    "You should check out are {product}. Does this product interest you?",
    "From your interests I would suggest {product}."
]

greeting_responses: list[str] = [
    "Hi! How can I assist you today?",
    "Hello! What can I help you with?",
    "Howdy! I am here for any input on are products you have!",
]

general_responses: list[str] = [
    "Ok",
    "Great!",
    "Is there anything else you would like to share?",
    "How else can I assist you today?",
    "I'm sorry I don't understand what you are asking me? Could you rephrase your question.",
    "I can't understand what you said. could you try again.",
    "Sorry I didn't quite get that. could you try again.",
    "I couldn't quite understand what you were talking about.",
    "I'm sorry that is beyond my understanding.",
]

closing_responses: list[str] = [
    "Have a great day!",
    "Thank you for your time.",
    "Thanks for sharing your thought with me.",
]

response_types: dict[int:list] = {
    "product satisfaction": product_satisfaction_responses,
    "complaint": complaint_responses,
    "review": review_responses,
    "suggestion": suggestion_responses,
    "greeting": greeting_responses,
    "general": general_responses,
    "closing": closing_responses,
}
