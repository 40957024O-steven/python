from cgi import test
from Questionuse import question

test = ["1+3=? \n (a) 2 \n (b) 3 \n (c) 4 \n\n",
        "1公尺等於幾公分? \n (a) 20 \n (b) 100 \n (c) 400 \n\n",
        "what is the coler of banana?\n (a) 紅色 \n (b) 黃色 \n (c) 綠色 \n\n"]
    
Question = [
        question(test[0],"c"),
        question(test[1],"b"),
        question(test[2],"b")
]

def runtest(question):
    score = 0
    for question in Question:
        answer = input(question.question)
        if answer == question.answer:
            score += 1
    print("你得到" + str(score) + "分,共有" + str(len(test)) + "題")

runtest(question)