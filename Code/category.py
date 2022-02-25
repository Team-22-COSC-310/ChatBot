"""
This class is responsible for categorically identifying a sentence as either satisfaction, complaint, review, greeting, general, or closing
"""

# feel free to add / remove words
greetingWords = ["hi", "hello", "hey"]
closingWords = ["bye", "goodbye", "farewell"]
satisfactionWords = ["satisfied", "satisfying", "happy", "good", "love", "great", "amazing", "decent", "mediocre", "fun", "worked"]
complaintWords = ["complaint", "complaints", "issue", "issues", "problem", "problems", "fail", "fails", "failed", "disappointing", "disappointed", "disappointment", "refund", "horrible", "boring", "bad", "irritating", "confusing", "confused", "annoying", "annoyed"]
reviewWords = ["review", "rating", "feedback", "suggestion", "stars", "reviewed", "criticism", "suggestions"]

def find_category(wordList: list) -> str:
    """
    Iterates through every word in wordList and increments category score if the word is found in the category's list of keywords
    :param wordList: list
    :return: str
    """
    greetingScore = 0; closingScore = 0; satisfactionScore = 0; complaintScore = 0; reviewScore = 0
    for i, word in enumerate(wordList):
        if word in greetingWords:
            greetingScore += 1
        if word in closingWords:
            closingScore += 1
        if word in satisfactionWords:
            if wordList[i-1] == "not":
                complaintScore += 1
            else:
                satisfactionScore += 1
        if word in complaintWords:
            if wordList[i-1] == "not" or wordList[i-1] == "no":
                satisfactionScore += 1
            else:
                complaintScore += 1
        if word in reviewWords:
            reviewScore += 1

    d = {}
    d["greeting"] = greetingScore
    d["closing"] = closingScore
    d["product satisfaction"] = satisfactionScore
    d["complaint"] = complaintScore
    d["review"] = reviewScore

    if sum(d.values()) > 0:
        return max(d, key=d.get)
    else:
        return "general"
