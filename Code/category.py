import math
from preprocess import parse_string as ps

"""
This class is responsible for analysis a strings similarity with a category.
"""


def tokenize(_str: str) -> dict[str: int]:
    """
    Creates dict with word count for each distinct word.
    :param _str: str
    :return: dict[str: int]
    """
    bag_of_words: list[str] = _str.split()
    return {word: bag_of_words.count(word) for word in set(bag_of_words)}


def cosine_similarity(tokens_1: dict[str: int], tokens_2: dict[str: int]) -> float:
    """
    Computes cosine similarity between two strings.
    :param tokens_1: dict[str: int]
    :param tokens_2: dict[str: int]
    :return: float
    """
    keys: set[str] = set(tokens_1.keys()) & set(tokens_2.keys())
    product: int = 0
    magnitude_1: float = 0.0
    magnitude_2: float = 0.0
    for key in keys:
        product += tokens_1[key] * tokens_2[key]
        magnitude_1 += math.pow(tokens_1[key], 2)
        magnitude_2 += math.pow(tokens_2[key], 2)
    
    cross_product: float = math.sqrt(magnitude_1) * math.sqrt(magnitude_2)
    return 0.0 if not cross_product else product / cross_product


def find_category(_str: str, default_category: str = "general") -> str:
    """
    Finds the most similar recognized category based on given string.
    :param _str: str
    :param default_category: str
    :return: str
    """
    main_tokens: dict[str: int] = tokenize(_str)
    main_category: str = default_category
    max_category_score: float = 0.0
    for key, item in categorical_types.items():
        category_score: float = sum(cosine_similarity(main_tokens, categorical_tokens) for categorical_tokens in item)
        if category_score > max_category_score:
            main_category = key
            max_category_score = category_score
    
    return main_category


product_satisfaction_keyterms: list[str] = [
    "the ... was super fun",
    "i love how the ... looks",
    "the ... was good",
    "i had a great experience",
    "i am happy with it",
    "it is great",
    "it is super",
    "the ... worked well",
    "it is pretty decent",
    "it is amazing how well the ... worked",
    "it is awesome",
    "i am satisfied with it",
    "it was super satisfying",
    "i love the ... that i got",
    "the ... i purchased was great",
    "i really like the ... i bought",
]

complaint_keyterms: list[str] = [
    "the ... was not good",
    "... is a bad ...",
    "it was a huge fail",
    "the ... had a poor quality to it",
    "fails to deliver", 
    "i have a issue with that", 
    "the ... broke as soon as i used it",
    "i want a refund for the ...",
    "it was broken as soon as i used it",
    "failed to provide anything i expected from it",
    "i have multiple issues",
    "i am very annoyed",
    "i have a problem with ...",
    "the ... i bought was an awefull desicion",
    "this is very annoying",
    "the ... was not stright forward when i bought it, and i found it very confusing",
    "the ... did not fit properly",
    "the ... had many problems",
    "i have a complaint",
    "the ... had a terrable design",
    "the ... was horrible",
    "i could not figure out the ... its was confusing",
    "the ... disfunction was irritating",
    "my disappointed was immersurable", 
    "my disappointing in the product was immersurable", 
    "i was very disappointment in the ...",
    "i would not buy ... agian",
    "i am regretful of the ... i purchased",
    "buying the ... was the worst decision i made",
    "i would like to complain about the ... i bought",
]

review_keyterms: list[str] = [
    "stars",
    "review", 
    "rating",
    "opinion",
    "reviewed",
    "feedback", 
    "recommend",
    "suggestion",
    "suggestions",
    "in my opinion the ...",
    "i would give the ... a",
    "my rating of the ... would be",
    "i would give the ... a ... out of ...",
]

greeting_keyterms: list[str] = [
    "hi",
    "hello",
    "what is up",
    "how are you",
    "good morning",
    "good evening",
    "good afternoon",
]

general_keyterms: list[str] = [
    "ok thanks",
    "that is great",
    "thanks for letting me know",
]

closing_keyterms: list[str] = [
    "later",
    "goodbye",
    "good night",
    "see you later",
    "have a good day",
    "thanks for listening",
]

categorical_types: dict[str: list[dict]] = {
    "product satisfaction": [tokenize(ps(term)) for term in product_satisfaction_keyterms],
    "complaint": [tokenize(ps(term)) for term in complaint_keyterms],
    "review": [tokenize(ps(term)) for term in review_keyterms],
    "greeting": [tokenize(ps(term)) for term in greeting_keyterms],
    "general": [tokenize(ps(term)) for term in general_keyterms],
    "closing": [tokenize(ps(term)) for term in closing_keyterms],
}
