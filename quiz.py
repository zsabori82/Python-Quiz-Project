import json

# Step 1: Define the quiz questions in a dictionary
quiz_data = {
    "questions": [
        {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": "C"},
        {"question": "Which programming language is known for web development?", "options": ["A. Python", "B. Java", "C. HTML", "D. C++"], "answer": "C"},
        {"question": "What is 5 + 7?", "options": ["A. 10", "B. 12", "C. 14", "D. 15"], "answer": "B"}
    ]
}

# Step 2: Save questions to a JSON file
def save_questions():
    with open("quiz_data.json", "w") as file:
        json.dump(quiz_data, file, indent=4)

def load_questions():
    with open("quiz_data.json", "r") as file:
        return json.load(file)

# Step 3: Function to run the quiz
def run_quiz():
    score = 0
    data = load_questions()
    
    print("Welcome to the Python Quiz!\n")
    
    for idx, q in enumerate(data["questions"], start=1):
        print(f"{idx}. {q['question']}")
        for opt in q["options"]:
            print(opt)
        
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        
        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}\n")
    
    print(f"Quiz Over! Your final score is: {score}/{len(data['questions'])}")

# Step 4: Main function to start the quiz
if __name__ == "__main__":
    save_questions()
    run_quiz()
