"""
CAPTCHA System for The Application Game
Various types of increasingly absurd CAPTCHAs
"""

import random
import time
from colorama import Fore, Style
from ui import UI

class CaptchaSystem:
    @staticmethod
    def math_captcha():
        """Simple math CAPTCHA"""
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operations = [
            ('+', num1 + num2),
            ('-', num1 - num2),
            ('×', num1 * num2)
        ]
        op, answer = random.choice(operations)

        print(f"\n{Fore.CYAN}╔════════════════════════════════╗")
        print(f"║  🤖 PROVE YOU'RE HUMAN 🤖      ║")
        print(f"╠════════════════════════════════╣")
        print(f"║  What is {num1} {op} {num2}?".ljust(33) + "║")
        print(f"╚════════════════════════════════╝{Style.RESET_ALL}")

        user_answer = UI.get_input("Answer", Fore.YELLOW)
        try:
            return int(user_answer) == answer
        except:
            return False

    @staticmethod
    def word_captcha():
        """Type the distorted word"""
        words = ["SYNERGY", "PARADIGM", "LEVERAGE", "OPTIMIZE", "DISRUPT",
                 "INNOVATE", "AGILE", "PIVOT", "BANDWIDTH", "SCALABLE"]
        word = random.choice(words)

        # Create "distorted" version with random spacing and characters
        distorted = ""
        for i, char in enumerate(word):
            if random.random() < 0.3:
                distorted += char + random.choice("~!@#$%")
            else:
                distorted += char
            if random.random() < 0.2:
                distorted += " "

        print(f"\n{Fore.CYAN}╔════════════════════════════════════════╗")
        print(f"║  🔒 SECURITY CHECK 🔒                  ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  Type this word (ignore symbols):      ║")
        print(f"║                                        ║")
        print(f"║  {Fore.RED}{distorted.center(36)}{Fore.CYAN}  ║")
        print(f"║                                        ║")
        print(f"╚════════════════════════════════════════╝{Style.RESET_ALL}")

        user_answer = UI.get_input("Type the word", Fore.YELLOW)
        return user_answer.upper().replace(" ", "") == word

    @staticmethod
    def select_image_captcha():
        """Select all images with... (simulated with ASCII)"""
        categories = [
            ("🚗 cars", ["🚗", "🚙", "🚕"], ["🚲", "🏍️", "✈️", "🚁", "⛵"]),
            ("🌳 trees", ["🌲", "🌳", "🎄"], ["🌵", "🌻", "🌺", "🌹", "🏵️"]),
            ("😊 faces", ["😊", "😃", "😄"], ["🐶", "🐱", "🦁", "🐯", "🐻"]),
            ("🍕 food", ["🍕", "🍔", "🌭"], ["⚽", "🏀", "🎾", "⚾", "🏈"])
        ]

        category_name, correct_items, wrong_items = random.choice(categories)

        # Create a grid of 9 items
        items = []
        correct_positions = random.sample(range(9), random.randint(2, 4))

        for i in range(9):
            if i in correct_positions:
                items.append(random.choice(correct_items))
            else:
                items.append(random.choice(wrong_items))

        print(f"\n{Fore.CYAN}╔════════════════════════════════════════╗")
        print(f"║  🖼️  IMAGE VERIFICATION 🖼️             ║")
        print(f"╠════════════════════════════════════════╣")
        print(f"║  Select all squares with {category_name}".ljust(41) + "║")
        print(f"║                                        ║")

        # Display 3x3 grid
        for row in range(3):
            row_str = "║  "
            for col in range(3):
                idx = row * 3 + col
                row_str += f"[{idx + 1}]{items[idx]}  "
            print(row_str.ljust(41) + "║")

        print(f"║                                        ║")
        print(f"╚════════════════════════════════════════╝{Style.RESET_ALL}")

        user_input = UI.get_input("Enter numbers (e.g., 1 3 5)", Fore.YELLOW)

        try:
            user_selections = [int(x) - 1 for x in user_input.split() if x.isdigit()]
            return set(user_selections) == set(correct_positions)
        except:
            return False

    @staticmethod
    def slider_captcha():
        """Slide to the position"""
        target_pos = random.randint(15, 35)

        print(f"\n{Fore.CYAN}╔════════════════════════════════════════════════╗")
        print(f"║  🎯 SLIDE TO VERIFY 🎯                         ║")
        print(f"╠════════════════════════════════════════════════╣")
        print(f"║  Slide the slider to position {target_pos}!".ljust(49) + "║")
        print(f"║                                                ║")
        print(f"║  |{'-' * 40}|                    ║")
        print(f"║  0{' ' * 38}40                    ║")
        print(f"║                                                ║")
        print(f"╚════════════════════════════════════════════════╝{Style.RESET_ALL}")

        user_input = UI.get_input("Enter position (0-40)", Fore.YELLOW)

        try:
            user_pos = int(user_input)
            return abs(user_pos - target_pos) <= 2  # Allow some tolerance
        except:
            return False

    @staticmethod
    def absurd_captcha():
        """Increasingly absurd CAPTCHAs for higher levels"""
        captchas = [
            {
                "question": "How many fingers does a duck have?",
                "answer": "0"
            },
            {
                "question": "Is water wet? (yes/no)",
                "answer": "yes"
            },
            {
                "question": "Type 'I love filling out applications'",
                "answer": "i love filling out applications"
            },
            {
                "question": "What sound does a circle make?",
                "answer": "none"
            },
            {
                "question": "Solve: ∞ + 1 = ?",
                "answer": "infinity"
            },
            {
                "question": "Are you a robot? (lie to me)",
                "answer": "yes"
            },
            {
                "question": "What is the meaning of life, the universe, and everything?",
                "answer": "42"
            }
        ]

        captcha = random.choice(captchas)

        print(f"\n{Fore.MAGENTA}╔════════════════════════════════════════════════╗")
        print(f"║  🤔 PHILOSOPHICAL VERIFICATION 🤔              ║")
        print(f"╠════════════════════════════════════════════════╣")

        # Wrap question if too long
        question = captcha["question"]
        if len(question) > 44:
            words = question.split()
            lines = []
            current_line = ""
            for word in words:
                if len(current_line) + len(word) + 1 <= 44:
                    current_line += (word + " ")
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "
            if current_line:
                lines.append(current_line.strip())

            for line in lines:
                print(f"║  {line.ljust(44)}  ║")
        else:
            print(f"║  {question.ljust(44)}  ║")

        print(f"║                                                ║")
        print(f"╚════════════════════════════════════════════════╝{Style.RESET_ALL}")

        user_answer = UI.get_input("Answer", Fore.YELLOW)
        return user_answer.lower().strip() == captcha["answer"].lower().strip()

    @staticmethod
    def run_captcha(level):
        """Run appropriate CAPTCHA based on level"""
        captcha_types = [
            CaptchaSystem.math_captcha,
            CaptchaSystem.word_captcha,
            CaptchaSystem.select_image_captcha,
            CaptchaSystem.slider_captcha,
            CaptchaSystem.absurd_captcha
        ]

        # Higher levels get more absurd CAPTCHAs
        if level <= 3:
            captcha = random.choice(captcha_types[:2])
        elif level <= 6:
            captcha = random.choice(captcha_types[:4])
        else:
            captcha = random.choice(captcha_types)

        UI.show_loading_bar("Generating CAPTCHA", 0.8)

        attempts = 2
        for attempt in range(attempts):
            if captcha():
                print(f"\n{Fore.GREEN}✓ CAPTCHA VERIFIED! You're probably human.{Style.RESET_ALL}")
                time.sleep(1)
                return True
            else:
                if attempt < attempts - 1:
                    print(f"\n{Fore.RED}✗ INCORRECT! Try again...{Style.RESET_ALL}")
                    time.sleep(1)

        print(f"\n{Fore.RED}✗ CAPTCHA FAILED! But we'll let you continue anyway...{Style.RESET_ALL}")
        time.sleep(1.5)
        return False
