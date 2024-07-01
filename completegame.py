questions = [
    {
        "prompt": "1) What is the most popular and easiest computer language?",
        "options": ["A: C", "B: C++", "C: python", "D: java"],
        "answer": "C"
    },
    {
        "prompt": "2) In which language printf is used?",
        "options": ["A: C", "B: python", "C: OOPS", "D: HTML"],
        "answer": "A"
    },
    {
        "prompt": "3) Which language is the standard markup language for making website pages?",
        "options": ["A: C++", "B: javascript", "C: python", "D: HTML"],
        "answer": "D"
    },
    {
        "prompt": "4) What are the essentials for the frontend dev?",
        "options": ["A: html", "B: html, CSS", "C: html, CSS, JAVA", "D: python"],
        "answer": "C"
    }
]
def quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for opt in question["options"]:
            print(opt)
        answer = input("Enter your answers: ")
        if(answer == question["answer"]):
            print("Correct answer!")
            score+=1
        else:
            print("Wrong Answer!")
            
    print(f"YOU GET {score} out of {len(questions)}")
    

quiz(questions)