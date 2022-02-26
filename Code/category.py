import math
from typing import Sequence
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


def term_frequency(term: str, token: dict[str: int]) -> float:
    """
    Finds term frequency from token.
    :param term: str
    :param token: dict[str: int]
    :return: float
    """
    return token[term] / len(token.keys())


def inverse_document_frequency(term: str, tokens: Sequence[dict[str: int]]) -> float:
    """
    Finds term inverse frequency from tokens.
    :param: term: str
    :param tokens: Sequence[dict[str: int]]
    :return: float
    """
    return math.log(len(tokens) / sum(token[term] for token in tokens if term in token))


def tfidf(term: str, token: dict[str: int], tokens: Sequence[dict[str: int]]) -> float:
    """
    Finds term frequency and inverse frequency.
    :param term: str
    :param token: dict[str: int]
    :param tokens: Sequence[dict[str: int]]
    :return: float
    """
    return term_frequency(term, token) * inverse_document_frequency(term, tokens)


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
    category: str = "general"
    similarity: float = 0.0
    for _category, keyterms in categorical_types.items():
        # Gets TF-IDF between all keyterms in category with _str
        tokens: list[dict[str: int]] = [tokenize(s) for s in [_str, *keyterms]]
        for token in tokens:
            for term in token.keys():
                token[term] = tfidf(term, token, tokens)
        
        # Gets similarity between _str and all keyterms in category
        user_token: dict[str: int] = tokens.pop(0)
        _similarity: float = max(cosine_similarity(user_token, t) for t in tokens)
        if _similarity > similarity:
            category = _category
            similarity = _similarity
    
    return category


product_satisfaction_keyterms: list[str] = [
    "love",
    "great",
    "super",
    "awesome",
    "i bought some ... and they rock",
    "i bought some awesome ..."
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
    "I bought some awesome shoes from your store.",
    "the ... i purchased was great",
    "i really like the ... i bought",
    "i bought some ... from a store of yours and they work great",
    "i bought a shirt from your store and it is awesome!",
]

complaint_keyterms: list[str] = [
    "bad",
    "awefull",
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

categorical_types: dict[list[str]] = {
    "product satisfaction": [ps(term) for term in product_satisfaction_keyterms],
    "complaint": [ps(term) for term in complaint_keyterms],
    "review": [ps(term) for term in review_keyterms],
    "greeting": [ps(term) for term in greeting_keyterms],
    "general": [ps(term) for term in general_keyterms],
    "closing": [ps(term) for term in closing_keyterms],
}
