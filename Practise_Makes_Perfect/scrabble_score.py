score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower() #method to make the string lower case
    total = 0 #innitial score
    for i in word:
        total = total + (score[i])
        """loop through the word that                                       you are given as input and                                       look up the score for each                                       letter in the score dictionary"""
    print total
    return total