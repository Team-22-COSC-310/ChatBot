def replace_by_dict(_str: str, replacement_map: dict[str: str]) -> str:
    """
    Parses through string and replaces parts of the original string based on the .
    :param _str: str
    :return: str
    """
    for key, item in replacement_map.items():
        _str = _str.replace(key, item)

    return _str


def parse_string(_str: str) -> list[str]:
    """
    Parses through string to clean up text and creates a bag of words.
    :param _str: str
    :return: list[str]
    """
    _str = _str.lower()
    _str = _str.strip()
    _str = replace_by_dict(_str, REPLACEMENT_MAP)

    return _str.split()


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
