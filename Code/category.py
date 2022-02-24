"""
This class is responsible for categorically identifying a sentence as either satisfaction (0), complaint (1), or review (2)
"""

# feel free to add / remove words
satisfactionWords = ["satisfied", "happy", "good", "love", "great", "amazing", "decent", "mediocre", "fun", "worked"]
complaintWords = ["complaint", "complaints", "issue", "issues", "problem", "problems", "fail", "fails", "failed", "disappointing", "disappointed", "disappointment", "refund", "horrible", "boring", "bad", "irritating", "confusing", "confused", "annoying", "annoyed"]
reviewWords = ["review", "rating", "feedback", "suggestion", "stars", "reviewed", "criticism", "suggestions"]

def find_category(wordList: list) -> int:
    """
    Iterates through every word in wordList and increments category score if the word is found in the category's list of keywords
    :param wordList: list
    :return: int
    """
    satisfactionScore = 0; complaintScore = 0; reviewScore = 0
    for i, word in enumerate(wordList):
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
    
    if satisfactionScore > complaintScore and satisfactionScore > reviewScore:
        return 0    # satisfaction
    elif complaintScore >= satisfactionScore and complaintScore >= reviewScore:
        return 1    # complaint
    elif reviewScore >= satisfactionScore and reviewScore > complaintScore:
        return 2    # review