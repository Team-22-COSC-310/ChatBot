from Code.preprocess import parse_string as ps

"""
This class is responsible for analysis strings for certain key subjects.
"""


def find_subject(document: str, default_subject: str = "product") -> str:
    """
    This method looks for the most common subject keyword
    :param str document: a string of normalized words
    :param str default_subject: a default subject if no others are found
    :return str: a subject based of the given document
    """
    subject: str = default_subject
    occurrences: int = 0
    bag_of_words: list[str] = document.split()
    for _subject in subjects:
        _occurrences: int = bag_of_words.count(_subject)
        if _occurrences > occurrences:
            subject = _subject
            occurrences = _occurrences

    return subject


subjects: list[str] = [
    "jacket",
    "coat",
    "sweater",
    "cardigan",
    "coat",
    "parka",
    "suit",
    "skirt",
    "dress",
    "shirt",
    "t-shirt",
    "trousers",
    "pants",
    "jeans",
    "shorts",
    "bathing suit",
    "shoe",
    "boots",
    "sneakers" "slippers",
    "flip flops",
    "glasses",
    "bag",
    "watch",
]
subjects = [ps(subject) for subject in subjects]
