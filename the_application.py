#!/usr/bin/env python3
"""
THE APPLICATION - The Ultimate Job Application Simulator
A retro 90s game about filling out increasingly absurd job applications
"""

import time
import sys
from datetime import datetime
from colorama import Fore, Style

from ui import UI
from game_state import GameState
from levels import get_levels, validate_answer
from captcha import CaptchaSystem
from scoring import ScoringSystem

class TheApplicationGame:
    def __init__(self):
        self.game_state = GameState()
        self.levels = get_levels()
        self.current_level = None
        self.scoring = None

    def show_start_screen(self):
        """Display the main menu/start screen"""
        while True:
            UI.clear()
            UI.show_title_screen()

            # Show game stats
            print(f"\n{Fore.YELLOW}{'─' * 100}{Style.RESET_ALL}")
            today = datetime.now().strftime("%B %d, %Y")
            print(UI.center_text(f"📅 {today}", 100))
            print(UI.center_text(f"🎯 Jobs Applied: {self.game_state.jobs_applied} | 🏆 High Score: {self.game_state.high_score:,}", 100))
            print(f"{Fore.YELLOW}{'─' * 100}{Style.RESET_ALL}\n")

            # Main menu
            UI.show_menu("MAIN MENU", [
                "START GAME (Level 1)",
                "LEVEL SELECT",
                "VIEW HIGH SCORES",
                "EXIT"
            ])

            choice = UI.get_input("Select option", Fore.YELLOW)

            if choice == "1":
                self.start_game(1)
            elif choice == "2":
                self.level_select()
            elif choice == "3":
                self.show_high_scores()
            elif choice == "4":
                self.quit_game()
                break
            else:
                print(f"{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
                time.sleep(1)

    def level_select(self):
        """Show level selection screen"""
        UI.clear()
        print(f"\n{Fore.CYAN}╔{'═' * 78}╗")
        print(f"║{'LEVEL SELECT'.center(78)}║")
        print(f"╠{'═' * 78}╣{Style.RESET_ALL}")

        for i, level in enumerate(self.levels, 1):
            if i <= self.game_state.unlocked_levels:
                high_score = self.game_state.level_high_scores[i - 1]
                status = f"{Fore.GREEN}✓ UNLOCKED{Style.RESET_ALL} | High Score: {high_score:,}"
                print(f"{Fore.CYAN}║ {Fore.YELLOW}{i:2d}.{Style.RESET_ALL} {level.get_info().ljust(45)} {status.ljust(30)}{Fore.CYAN}║{Style.RESET_ALL}")
            else:
                status = f"{Fore.RED}🔒 LOCKED{Style.RESET_ALL}"
                print(f"{Fore.CYAN}║ {Fore.YELLOW}{i:2d}.{Style.RESET_ALL} {'???'.ljust(45)} {status.ljust(30)}{Fore.CYAN}║{Style.RESET_ALL}")

        print(f"{Fore.CYAN}╚{'═' * 78}╝{Style.RESET_ALL}\n")

        choice = UI.get_input("Select level (or 'back')", Fore.YELLOW)

        if choice.lower() == 'back':
            return

        try:
            level_num = int(choice)
            if 1 <= level_num <= self.game_state.unlocked_levels:
                self.start_game(level_num)
            elif 1 <= level_num <= 10:
                print(f"{Fore.RED}This level is locked! Complete previous levels to unlock.{Style.RESET_ALL}")
                time.sleep(2)
            else:
                print(f"{Fore.RED}Invalid level number!{Style.RESET_ALL}")
                time.sleep(1)
        except ValueError:
            print(f"{Fore.RED}Invalid input!{Style.RESET_ALL}")
            time.sleep(1)

    def show_high_scores(self):
        """Display high scores"""
        UI.clear()
        print(f"\n{Fore.YELLOW}╔{'═' * 58}╗")
        print(f"║{'🏆 HIGH SCORES 🏆'.center(58)}║")
        print(f"╠{'═' * 58}╣{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL} {'Overall High Score:'.ljust(35)} {f'{self.game_state.high_score:,} points'.rjust(21)} {Fore.YELLOW}║{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL} {'Total Jobs Applied:'.ljust(35)} {f'{self.game_state.jobs_applied} times'.rjust(21)} {Fore.YELLOW}║{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}╠{'═' * 58}╣{Style.RESET_ALL}")

        for i in range(10):
            level_score = self.game_state.level_high_scores[i]
            if i < self.game_state.unlocked_levels:
                status = f"{Fore.GREEN}✓{Style.RESET_ALL}"
            else:
                status = f"{Fore.RED}🔒{Style.RESET_ALL}"

            print(f"{Fore.YELLOW}║{Style.RESET_ALL} {status} Level {i+1:2d}:".ljust(45) + f"{level_score:,} points".rjust(22) + f"{Fore.YELLOW}║{Style.RESET_ALL}")

        print(f"{Fore.YELLOW}╚{'═' * 58}╝{Style.RESET_ALL}\n")

        UI.pause()

    def start_game(self, level_num):
        """Start playing from specified level"""
        self.game_state.increment_jobs_applied()
        self.scoring = ScoringSystem()

        # Play levels sequentially from selected level
        for i in range(level_num - 1, len(self.levels)):
            level = self.levels[i]
            if not self.play_level(level):
                # Player quit or failed
                return

        # Game completed!
        self.game_complete()

    def play_level(self, level):
        """Play a single level"""
        UI.clear()
        UI.show_loading_bar(f"Loading {level.job_title}", 1.0)

        UI.clear()
        print(f"\n{Fore.CYAN}╔{'═' * 78}╗")
        print(f"║{f'LEVEL {level.number}'.center(78)}║")
        print(f"╠{'═' * 78}╣")
        print(f"║{f'Position: {level.job_title}'.center(78)}║")
        print(f"║{f'Company: {level.company}'.center(78)}║")
        print(f"╚{'═' * 78}╝{Style.RESET_ALL}\n")

        print(f"{Fore.YELLOW}Congratulations! You've been selected to fill out our application!{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Answer quickly for bonus points. Wrong answers break your combo!{Style.RESET_ALL}\n")

        UI.pause("Press ENTER to start the application")

        level_start_time = time.time()

        # Ask questions
        for i, question in enumerate(level.questions, 1):
            UI.clear()
            UI.show_score(self.scoring.get_score(), self.game_state.high_score, self.scoring.get_combo())

            print(f"\n{Fore.CYAN}Level {level.number} - Question {i}/{len(level.questions)}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}{'─' * 80}{Style.RESET_ALL}\n")

            # Show question with timer
            result = self.ask_question(question)

            if result is None:
                # Player quit
                return False

            is_correct, time_remaining = result

            # Calculate score
            points = self.scoring.calculate_question_score(
                time_remaining,
                question["time"],
                is_correct
            )

            # Show feedback
            if is_correct:
                combo = self.scoring.get_combo()
                combo_text = f" | COMBO x{combo}!" if combo > 1 else ""
                print(f"\n{Fore.GREEN}✓ CORRECT! +{points:,} points{combo_text}{Style.RESET_ALL}")
            else:
                print(f"\n{Fore.RED}✗ WRONG! Combo broken!{Style.RESET_ALL}")

            time.sleep(0.8)

        # CAPTCHA time!
        print(f"\n{Fore.YELLOW}One more thing before we process your application...{Style.RESET_ALL}")
        time.sleep(1.5)

        captcha_success = CaptchaSystem.run_captcha(level.number)
        captcha_bonus = self.scoring.add_captcha_bonus(captcha_success)

        if captcha_bonus > 0:
            print(f"{Fore.GREEN}CAPTCHA BONUS: +{captcha_bonus} points!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}CAPTCHA PENALTY: {captcha_bonus} points{Style.RESET_ALL}")

        time.sleep(1)

        # Level complete!
        level_time = int(time.time() - level_start_time)
        bonuses = self.scoring.add_level_completion_bonus(level.number, level_time)

        # Update game state
        final_score = self.scoring.get_score()
        new_level_high = self.game_state.update_level_score(level.number, final_score)
        new_overall_high = self.game_state.update_high_score(final_score)

        # Unlock next level
        if level.number < 10:
            self.game_state.unlock_level(level.number + 1)

        # Show completion screen
        UI.show_level_complete(level.number, final_score, new_level_high or new_overall_high)

        self.scoring.show_bonus_breakdown(bonuses)

        if new_overall_high:
            print(f"{Fore.MAGENTA}{'*' * 80}")
            print(UI.center_text("🎊 NEW OVERALL HIGH SCORE! 🎊", 80))
            print(f"{'*' * 80}{Style.RESET_ALL}\n")

        # Continue to next level?
        if level.number < 10:
            choice = UI.get_input("Continue to next level? (yes/no)", Fore.YELLOW)
            if choice.lower() not in ['yes', 'y']:
                return False

        return True

    def ask_question(self, question):
        """Ask a single question with timer"""
        print(f"{Fore.CYAN}{question['q']}{Style.RESET_ALL}\n")

        time_limit = question["time"]
        print(f"{Fore.YELLOW}[You have {time_limit} seconds to answer]{Style.RESET_ALL}\n")

        start_time = time.time()
        user_answer = UI.get_input("Answer", Fore.GREEN)
        end_time = time.time()

        time_taken = end_time - start_time
        time_remaining = max(0, time_limit - time_taken)

        # Check if user wants to quit
        if user_answer.lower() in ['quit', 'exit', 'q']:
            return None

        # Validate answer
        is_correct = validate_answer(question, user_answer)

        # Time penalty - if over time, it's wrong
        if time_taken > time_limit:
            print(f"\n{Fore.RED}⏰ TOO SLOW!{Style.RESET_ALL}")
            time.sleep(0.5)
            is_correct = False
            time_remaining = 0

        return is_correct, time_remaining

    def game_complete(self):
        """Show game completion screen"""
        UI.clear()
        print("\n" * 2)

        victory = [
            "🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉",
            "                                        ",
            "   YOU ARE HIRED!!! (everywhere)        ",
            "                                        ",
            "   You've completed ALL 10 levels!      ",
            "                                        ",
            "🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉",
        ]

        for line in victory:
            print(UI.center_text(f"{Fore.YELLOW}{line}{Style.RESET_ALL}", 100))

        print("\n")
        self.scoring.show_final_statistics()

        print(UI.center_text(f"{Fore.CYAN}You are now a MASTER of job applications!{Style.RESET_ALL}", 100))
        print(UI.center_text(f"{Fore.CYAN}Thanks for playing THE APPLICATION!{Style.RESET_ALL}", 100))
        print("\n")

        UI.pause()

    def quit_game(self):
        """Quit the game"""
        UI.clear()
        print("\n" * 5)

        goodbye = [
            "Thanks for playing THE APPLICATION!",
            "",
            "Remember: The real job was the applications we filled along the way.",
            "",
            "👋 See you next time!",
        ]

        for line in goodbye:
            print(UI.center_text(UI.rainbow_text(line), 100))

        print("\n" * 5)
        time.sleep(2)

def main():
    """Main entry point"""
    try:
        game = TheApplicationGame()
        game.show_start_screen()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Game interrupted. Goodbye!{Style.RESET_ALL}\n")
        sys.exit(0)

if __name__ == "__main__":
    main()
