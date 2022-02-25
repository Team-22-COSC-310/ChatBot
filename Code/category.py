import math

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
    length_1: float = 0.0
    length_2: float = 0.0
    for key in keys:
        product += tokens_1[key] * tokens_2[key]
        length_1 += math.pow(tokens_1[key], 2)
        length_2 += math.pow(tokens_2[key], 2)
    
    cross_product: float = math.sqrt(length_1) * math.sqrt(length_2)
    return 0.0 if not cross_product else product / cross_product


def find_category(_str: str, default_category: str = "general") -> str:
    """
    Finds the most similar recognized category based on given string.
    :param _str: str
    :param default_category: str
    :return: str
    """
    str_tokens: dict[str: int] = tokenize(_str)
    category: str = default_category
    max_category_score: float = 0.0
    for key, item in categorical_types.items():
        category_score: float = sum(cosine_similarity(str_tokens, categorical_tokens) for categorical_tokens in item) / len(item)
        if category_score > max_category_score:
            category = key
            max_category_score = category_score
    
    return category


product_satisfaction_keyterms: list[str] = [
    "fun",
    "love",
    "good",
    "great",
    "happy",
    "great",
    "super",
    "worked",
    "decent",
    "amazing",
    "awesome",
    "mediocre",
    "satisfied",
    "satisfied", 
    "satisfying",
    "the ... i purchased was great",
    "i love the ... that i got",
    "i really like the ... i bought",
]

complaint_keyterms: list[str] = [
    "not",
    "bad",
    "fail",
    "poor",
    "fails", 
    "issue", 
    "refund",
    "boring",
    "failed",
    "issues",
    "annoyed",
    "problem",
    "awefull",
    "annoying",
    "confused",
    "problems",
    "complain",
    "terrable",
    "horrible",
    "confusing",
    "complaint",
    "complaints",
    "irritating",
    "disappointed", 
    "disappointing", 
    "disappointment",
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
    "product satisfaction": [tokenize(term) for term in product_satisfaction_keyterms],
    "complaint": [tokenize(term) for term in complaint_keyterms],
    "review": [tokenize(term) for term in review_keyterms],
    "greeting": [tokenize(term) for term in greeting_keyterms],
    "general": [tokenize(term) for term in general_keyterms],
    "closing": [tokenize(term) for term in closing_keyterms],
}
