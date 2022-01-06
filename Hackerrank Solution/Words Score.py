
def score_words(words):
    score=0
    for word in words:
        count1=0
        count2=0
        for letter in word:
            if letter in "aeiouy":
                count1+=1
        if count1%2==0:
            score+=2
        else:
            score+=1
    return score
            


n = int(input())
words = input().split()
print(score_words(words))
