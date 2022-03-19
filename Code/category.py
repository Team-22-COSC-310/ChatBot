import math
from typing import Sequence
from preprocess import parse_string as ps

"""
This class is responsible for analysis a strings similarity with a category.
"""


def get_bofw(document: str) -> dict[str:int]:
    """
    Creates dict with word count for each distinct word
    :param str document: a string of normalized words
    :return: dict[str: int]
    """
    bag_of_words: list[str] = document.split()
    return {word: bag_of_words.count(word) for word in set(bag_of_words)}


def term_frequency(term: str, bofw: dict[str:int]) -> float:
    """
    Finds term frequency from token
    :param str term: a normalized word
    :param bofw: a tokenized document
    :type bofw: dict[str: int]
    :return float: the tf value
    """
    return bofw[term] / len(bofw.keys())


def inverse_document_frequency(term: str, bsofw: Sequence[dict[str:int]]) -> float:
    """
    Finds term inverse frequency from tokens
    :param str term: a normalized word
    :param bsofw: tokenized documents
    :type bsofw: Sequence[dict[str: int]]
    :return float: the idf value
    """
    return math.log(len(bsofw) / sum(token[term] for token in bsofw if term in token))


def tfidf(term: str, bofw: dict[str:int], bsofw: Sequence[dict[str:int]]) -> float:
    """
    Finds term frequency and inverse frequency
    :param str term: a normalized word
    :param bofw: a tokenized document
    :type bofw: dict[str: int]
    :param bsofw: tokenized documents
    :type bsofw: Sequence[dict[str: int]]
    :return float: the tfidf value
    """
    return term_frequency(term, bofw) * inverse_document_frequency(term, bsofw)


def cosine_similarity(bofw_1: dict[str:int], bofw_2: dict[str:int]) -> float:
    """
    Computes cosine similarity between two strings
    :param bofw_1: a tokenized document
    :type bofw_1: dict[str: int]
    :param bofw_2: a tokenized document
    :type bofw_2: dict[str: int]
    :return float: the cosine similarity of both tokens
    """
    keys: set[str] = set(bofw_1.keys()) & set(bofw_2.keys())
    product: int = 0
    magnitude_1: float = 0.0
    magnitude_2: float = 0.0
    for key in keys:
        product += bofw_1[key] * bofw_2[key]
        magnitude_1 += math.pow(bofw_1[key], 2)
        magnitude_2 += math.pow(bofw_2[key], 2)

    cross_product: float = math.sqrt(magnitude_1) * math.sqrt(magnitude_2)
    return 0.0 if not cross_product else product / cross_product


def find_category(document: str, default_category: str = "general") -> str:
    """
    Finds the most similar recognized category based on given string
    :param str document: a string of normalized words
    :param str default_category: a default category if no others are found
    :return str: generated category
    """
    category: str = default_category
    similarity: float = 0.0
    for _category, keyterms in categorical_types.items():
        # Gets TF-IDF between all keyterms in category with _str
        tokens: list[dict[str:int]] = [get_bofw(s) for s in [document, *keyterms]]
        for token in tokens:
            for term in token.keys():
                token[term] = tfidf(term, token, tokens)

        # Gets similarity between _str and all keyterms in category
        user_token: dict[str:int] = tokens.pop(0)
        _similarity: float = sum(
            cosine_similarity(user_token, t) for t in tokens
        ) / len(keyterms)
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
    "i bought some awesome ..." "the ... was super fun",
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
    "i bought a ... from your store and it is awesome",
]

complaint_keyterms: list[str] = [
    "not",
    "bad",
    "problem",
    "awe full",
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
    "the ... i bought was an awe full decision",
    "this is very annoying",
    "the ... was not straight forward when i bought it, and i found it very confusing",
    "the ... did not fit properly",
    "the ... had many problems",
    "i have a complaint",
    "the ... had a terrable design",
    "the ... was horrible",
    "i could not figure out the ... its was confusing",
    "the ... dysfunction was irritating",
    "my disappointed was immeasurable",
    "my disappointing in the product was immeasurable",
    "i was very disappointment in the ...",
    "i would not buy ... again",
    "i am regretful of the ... i purchased",
    "buying the ... was the worst decision i made",
    "i would like to complain about the ... i bought",
    "i am having problems with my ...",
    "i bought a product from one of your stores and it was broken",
]

review_keyterms: list[str] = [
    "rate",
    "stars",
    "review",
    "opinion",
    "feedback",
    "you should use better",
    "in my opinion the ...",
    "i would give the ... a",
    "my rating of the ... would be",
    "i would give the ... a ... out of ...",
]

suggestion_keyterms: list[str] = [
    "suggest",
    "recommend",
    "suggestion",
    "suggestions",
    "could you suggest anything for me",
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

categorical_types: dict[str: list[str]] = {
    "product satisfaction": [ps(term) for term in product_satisfaction_keyterms],
    "complaint": [ps(term) for term in complaint_keyterms],
    "review": [ps(term) for term in review_keyterms],
    "suggestion": [ps(term) for term in suggestion_keyterms],
    "greeting": [ps(term) for term in greeting_keyterms],
    "general": [ps(term) for term in general_keyterms],
    "closing": [ps(term) for term in closing_keyterms],
}
