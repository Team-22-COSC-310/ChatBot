from nltk.stem import PorterStemmer

"""
This class is responsible for preprocessing and normalizing strings for further consistent analysis.
"""


def replace(document: str, replacement_map: dict[str:str]) -> str:
    """
    Parses through string and replaces parts of the original string based on the replacement_map
    :param str document: a string of words
    :param replacement_map: dict of terms and its replacement
    :type replacement_map: dict[str: str]
    :return str: new string with terms replaced
    """
    for key, item in replacement_map.items():
        document = document.replace(key, item)

    return document


def parse_string(document: str) -> str:
    """
    Parses through string to clean, lower, and replace text
    :param str document: a string of words
    :return list[str]: parsed document
    """
    document = document.lower()
    document = document.strip()
    document = replace(document, REPLACEMENT_MAP)
    document = " ".join([ps.stem(word) for word in document.split(" ")])

    return document


ps = PorterStemmer()
REPLACEMENT_MAP: dict[str:str] = {
    "!": "",
    "?": "",
    ".": "",
    ":": "",
    "â€¢": "",
    "/": "",
    "(": "",
    ")": "",
    "'": "",
    '"': "",
    "â€”": " ",
    "-": " ",
    ",": " ",
    ";": " ",
    "'s": " is",
    "'t": " not",
    "'m": " am",
    "'ve": " have",
    "'re": " are",
    "'ll": " will",
}
