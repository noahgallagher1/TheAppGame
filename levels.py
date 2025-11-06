"""
Level Definitions for The Application Game
10 unique levels with progressively absurd questions
"""

import random

class Level:
    def __init__(self, number, job_title, company, questions):
        self.number = number
        self.job_title = job_title
        self.company = company
        self.questions = questions

    def get_info(self):
        return f"Level {self.number}: {self.job_title} at {self.company}"

def get_levels():
    """Return all 10 levels with their questions"""

    levels = [
        # Level 1: Normal job application
        Level(1, "Junior Data Entry Clerk", "Boring Corp",
              [
                  {"q": "What is your full name?", "type": "text", "time": 15},
                  {"q": "What is your email address?", "type": "text", "time": 15},
                  {"q": "What is your phone number?", "type": "text", "time": 15},
                  {"q": "Do you have a high school diploma? (yes/no)", "type": "yesno", "time": 10},
                  {"q": "Why do you want to work here?", "type": "text", "time": 20},
              ]),

        # Level 2: Still normal, more questions
        Level(2, "Assistant Manager", "Generic Industries",
              [
                  {"q": "What is your full name?", "type": "text", "time": 12},
                  {"q": "Years of experience in management?", "type": "number", "time": 10},
                  {"q": "Highest education level achieved?", "type": "text", "time": 15},
                  {"q": "Are you authorized to work in the US? (yes/no)", "type": "yesno", "time": 8},
                  {"q": "List three professional strengths:", "type": "text", "time": 20},
                  {"q": "Expected salary range?", "type": "text", "time": 12},
                  {"q": "Can you work weekends? (yes/no)", "type": "yesno", "time": 8},
              ]),

        # Level 3: Getting weird
        Level(3, "Synergy Optimization Specialist", "Buzzword Solutions LLC",
              [
                  {"q": "How many buzzwords can you fit in one sentence?", "type": "text", "time": 25},
                  {"q": "Rate your synergy skills (1-10):", "type": "number", "time": 8},
                  {"q": "What is the capital of France?", "type": "text", "time": 10, "answer": "paris"},
                  {"q": "Can you leverage paradigm shifts? (yes/no)", "type": "yesno", "time": 8},
                  {"q": "Favorite color?", "type": "text", "time": 8},
                  {"q": "If you were a kitchen appliance, which one?", "type": "text", "time": 15},
                  {"q": "Are circles pointless? (yes/no)", "type": "yesno", "time": 10},
                  {"q": "How many coffee cups can you stack?", "type": "number", "time": 8},
              ]),

        # Level 4: Getting absurd - quick questions
        Level(4, "Chief Meme Officer", "Internet Dynamics",
              [
                  {"q": "What year is it?", "type": "text", "time": 5},
                  {"q": "Favorite meme format?", "type": "text", "time": 8},
                  {"q": "How many planets in the solar system?", "type": "number", "time": 5, "answer": "8"},
                  {"q": "Is a hot dog a sandwich? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is 7 × 8?", "type": "number", "time": 6, "answer": "56"},
                  {"q": "Best pizza topping?", "type": "text", "time": 6},
                  {"q": "Can you moonwalk? (yes/no)", "type": "yesno", "time": 5},
                  {"q": "Spell 'cat' backwards:", "type": "text", "time": 5, "answer": "tac"},
                  {"q": "What is 100 - 7?", "type": "number", "time": 5, "answer": "93"},
                  {"q": "Do fish have eyelids? (yes/no)", "type": "yesno", "time": 6},
              ]),

        # Level 5: Speed round!
        Level(5, "Professional Question Answerer", "Meta Applications Inc",
              [
                  {"q": "Type 'YES':", "type": "text", "time": 4, "answer": "yes"},
                  {"q": "What is 2 + 2?", "type": "number", "time": 4, "answer": "4"},
                  {"q": "What is 5 × 5?", "type": "number", "time": 4, "answer": "25"},
                  {"q": "Are you alive? (yes/no)", "type": "yesno", "time": 3},
                  {"q": "What is 10 ÷ 2?", "type": "number", "time": 4, "answer": "5"},
                  {"q": "Is water wet? (yes/no)", "type": "yesno", "time": 3},
                  {"q": "What is 3 + 7?", "type": "number", "time": 4, "answer": "10"},
                  {"q": "Type 'HIRED':", "type": "text", "time": 4, "answer": "hired"},
                  {"q": "What is 12 - 3?", "type": "number", "time": 4, "answer": "9"},
                  {"q": "Can you read? (yes/no)", "type": "yesno", "time": 3},
                  {"q": "What is 6 × 2?", "type": "number", "time": 4, "answer": "12"},
                  {"q": "Is the sky blue? (yes/no)", "type": "yesno", "time": 3},
              ]),

        # Level 6: Pop culture & trivia
        Level(6, "Cultural Knowledge Validator", "TriviaWorks Global",
              [
                  {"q": "Who painted the Mona Lisa?", "type": "text", "time": 12, "answer": "leonardo da vinci"},
                  {"q": "What is the capital of Japan?", "type": "text", "time": 10, "answer": "tokyo"},
                  {"q": "How many Harry Potter books are there?", "type": "number", "time": 8, "answer": "7"},
                  {"q": "Who is Mario's brother?", "type": "text", "time": 8, "answer": "luigi"},
                  {"q": "What is the fastest land animal?", "type": "text", "time": 10, "answer": "cheetah"},
                  {"q": "How many continents are there?", "type": "number", "time": 8, "answer": "7"},
                  {"q": "What color are Smurfs?", "type": "text", "time": 6, "answer": "blue"},
                  {"q": "What is 10 + 15?", "type": "number", "time": 6, "answer": "25"},
                  {"q": "Who wrote Romeo and Juliet?", "type": "text", "time": 10, "answer": "shakespeare"},
              ]),

        # Level 7: Random chaos
        Level(7, "Reality Distortion Field Engineer", "Quantum Nonsense Ltd",
              [
                  {"q": "If a train leaves at 3pm going 60mph, are you hiring?", "type": "text", "time": 15},
                  {"q": "How many dimensions can you perceive?", "type": "number", "time": 10},
                  {"q": "What color is Tuesday?", "type": "text", "time": 10},
                  {"q": "Rate your ability to exist (1-10):", "type": "number", "time": 8},
                  {"q": "Can you taste sounds? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is the square root of a banana?", "type": "text", "time": 12},
                  {"q": "How many roads must a man walk down?", "type": "number", "time": 10},
                  {"q": "Is mayonnaise an instrument? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is the airspeed velocity of an unladen swallow?", "type": "text", "time": 12},
                  {"q": "Do you believe in life after love? (yes/no)", "type": "yesno", "time": 8},
              ]),

        # Level 8: Existential crisis
        Level(8, "Existential Question Processor", "Philosophy & Sons",
              [
                  {"q": "Why?", "type": "text", "time": 12},
                  {"q": "But why though?", "type": "text", "time": 12},
                  {"q": "Are you sure? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is your purpose?", "type": "text", "time": 15},
                  {"q": "On a scale of 1-10, how real do you feel?", "type": "number", "time": 10},
                  {"q": "If a tree falls and no one is around, did this question happen?", "type": "text", "time": 15},
                  {"q": "What is the meaning of life?", "type": "number", "time": 10, "answer": "42"},
                  {"q": "Are we living in a simulation? (yes/no)", "type": "yesno", "time": 8},
                  {"q": "Do you think, therefore you are? (yes/no)", "type": "yesno", "time": 8},
                  {"q": "Can you prove you exist?", "type": "text", "time": 12},
                  {"q": "What is consciousness?", "type": "text", "time": 15},
              ]),

        # Level 9: Ultimate chaos - everything mixed
        Level(9, "Supreme Overlord of Application Forms", "The Final Boss Inc",
              [
                  {"q": "What is 144 ÷ 12?", "type": "number", "time": 6, "answer": "12"},
                  {"q": "Type the word 'CHAOS':", "type": "text", "time": 5, "answer": "chaos"},
                  {"q": "How many fingers am I holding up?", "type": "number", "time": 6},
                  {"q": "What is the capital of Antarctica?", "type": "text", "time": 10},
                  {"q": "Can you juggle time? (yes/no)", "type": "yesno", "time": 5},
                  {"q": "What is 9 × 7?", "type": "number", "time": 6, "answer": "63"},
                  {"q": "Favorite element from the periodic table?", "type": "text", "time": 10},
                  {"q": "Are you still there? (yes/no)", "type": "yesno", "time": 4},
                  {"q": "What is 88 - 22?", "type": "number", "time": 6, "answer": "66"},
                  {"q": "If you could be any font, which font?", "type": "text", "time": 10},
                  {"q": "Do you enjoy filling out applications? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is 15 + 28?", "type": "number", "time": 6, "answer": "43"},
                  {"q": "Last question: Will you accept the job? (yes/no)", "type": "yesno", "time": 8},
              ]),

        # Level 10: The final form - ULTIMATE APPLICATION
        Level(10, "God-Emperor of Form Filling", "∞ Infinite Applications ∞",
              [
                  {"q": "Welcome to the ULTIMATE application. Ready? (yes/no)", "type": "yesno", "time": 6},
                  {"q": "What is 256 + 128?", "type": "number", "time": 8, "answer": "384"},
                  {"q": "Name a country starting with 'Z':", "type": "text", "time": 10},
                  {"q": "Can you handle the pressure? (yes/no)", "type": "yesno", "time": 5},
                  {"q": "What is 17 × 3?", "type": "number", "time": 7, "answer": "51"},
                  {"q": "How many legs does a spider have?", "type": "number", "time": 6, "answer": "8"},
                  {"q": "Type 'UNSTOPPABLE':", "type": "text", "time": 6, "answer": "unstoppable"},
                  {"q": "What comes after Wednesday?", "type": "text", "time": 6, "answer": "thursday"},
                  {"q": "Is this your final form? (yes/no)", "type": "yesno", "time": 5},
                  {"q": "What is 100 - 37?", "type": "number", "time": 7, "answer": "63"},
                  {"q": "How many sides does a hexagon have?", "type": "number", "time": 6, "answer": "6"},
                  {"q": "Are you a master of applications? (yes/no)", "type": "yesno", "time": 5},
                  {"q": "What is the square root of 144?", "type": "number", "time": 8, "answer": "12"},
                  {"q": "Type 'I AM THE CHAMPION':", "type": "text", "time": 7, "answer": "i am the champion"},
                  {"q": "Final question: Did you have fun? (yes/no)", "type": "yesno", "time": 8},
              ]),
    ]

    return levels

def validate_answer(question, user_answer):
    """Check if answer is correct (for questions with specific answers)"""
    if "answer" not in question:
        # No specific answer required, any response is valid
        return True

    expected = str(question["answer"]).lower().strip()
    user = user_answer.lower().strip()

    # Handle partial matches for names (e.g., "da vinci" matches "leonardo da vinci")
    if question["type"] == "text":
        return expected in user or user in expected or user == expected

    return user == expected
