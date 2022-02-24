"""
This class is responsible for analysis strings for certain key subjects
"""


def find_subject(_str: str) -> str:
    """
    This method looks for the most common subject keyword.
    :param _str: str
    :return: str
    """
    subject: str = "product"
    subject_occurrences: int = 0
    bag_of_words: list[str] = _str.split()
    for _subject in subjects:
        occurrences: int = bag_of_words.count(_subject)
        if occurrences > subject_occurrences:
            subject = _subject
            subject_occurrences = occurrences

    return subject


subjects: list[str] = [
        "jacket",
        "coat",
        "sweater",
        "cardigan",
        "coat",
        "parka",
        "trousers",
        "pants",
        "jeans",
        "shorts",
        "bathing suit",
        "suit",
        "skirt",
        "dress",
        "shoe",
        "shoes",
        "boots",
        "sneakers"
        "slippers",
        "flip flops",
]
