"""
This class is responsible for preprocessing and normalizing strings for further consistent analysis.
"""


def replace(_str: str, replacement_map: dict[str: str]) -> str:
    """
    Parses through string and replaces parts of the original string based on the replacement_map.
    :param _str: str
    :param replacement_map: dict[str: str]
    :return: str
    """
    for key, item in replacement_map.items():
        _str = _str.replace(key, item)

    return _str


def parse_string(_str: str) -> str:
    """
    Parses through string to clean, lower, and replace text.
    :param _str: str
    :return: list[str]
    """
    _str = _str.lower()
    _str = _str.strip()
    _str = replace(_str, REPLACEMENT_MAP)

    return _str


REPLACEMENT_MAP: dict[str: str] = {
    "!": "",
    "?": "",
    ".": "",
    ":": "",
    'â€¢': "",
    "/": "",
    "(": "",
    ")": "",
    "\'": "",
    "\"": "",
    "â€”": " ",
    "-": " ",
    ",": " ",
    ";": " ",
    "\'s": " is",
    "\'t": " not",
    "\'m": " am",
    "\'ve": " have",
    "\'re": " are",
    "\'ll": " will",
}
