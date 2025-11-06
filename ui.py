"""
UI Rendering System for The Application Game
90s Internet Aesthetic with Colorful Terminal Graphics
"""

from colorama import init, Fore, Back, Style
import os
import time
from datetime import datetime

init(autoreset=True)

class UI:
    @staticmethod
    def clear():
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')

    @staticmethod
    def center_text(text, width=80):
        """Center text in given width"""
        return text.center(width)

    @staticmethod
    def rainbow_text(text):
        """Create rainbow colored text"""
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        result = ""
        for i, char in enumerate(text):
            result += colors[i % len(colors)] + char
        return result + Style.RESET_ALL

    @staticmethod
    def draw_box(title, content, width=80, color=Fore.CYAN):
        """Draw a retro box around content"""
        border_top = color + "╔" + "═" * (width - 2) + "╗" + Style.RESET_ALL
        border_bottom = color + "╚" + "═" * (width - 2) + "╝" + Style.RESET_ALL
        border_side = color + "║" + Style.RESET_ALL

        lines = [border_top]

        if title:
            title_line = border_side + UI.center_text(title, width - 2) + border_side
            lines.append(title_line)
            lines.append(color + "║" + "─" * (width - 2) + "║" + Style.RESET_ALL)

        for line in content:
            padding = " " * ((width - 2 - len(line)) // 2)
            lines.append(border_side + padding + line + " " * (width - 2 - len(padding) - len(line)) + border_side)

        lines.append(border_bottom)
        return "\n".join(lines)

    @staticmethod
    def show_title_screen():
        """Display the epic 90s title screen"""
        UI.clear()
        print("\n")

        # ASCII art title
        title = [
            "████████╗██╗  ██╗███████╗",
            "╚══██╔══╝██║  ██║██╔════╝",
            "   ██║   ███████║█████╗  ",
            "   ██║   ██╔══██║██╔══╝  ",
            "   ██║   ██║  ██║███████╗",
            "   ╚═╝   ╚═╝  ╚═╝╚══════╝",
        ]

        title2 = [
            " █████╗ ██████╗ ██████╗ ██╗     ██╗ ██████╗ █████╗ ████████╗██╗ ██████╗ ███╗   ███╗",
            "██╔══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗ ████║",
            "███████║██████╔╝██████╔╝██║     ██║██║     ███████║   ██║   ██║██║   ██║██╔████╔██║",
            "██╔══██║██╔═══╝ ██╔═══╝ ██║     ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╔╝██║",
            "██║  ██║██║     ██║     ███████╗██║╚██████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚═╝ ██║",
            "╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝     ╚═╝",
        ]

        for line in title:
            print(UI.center_text(UI.rainbow_text(line), 100))

        for line in title2:
            print(UI.center_text(UI.rainbow_text(line), 100))

        print(UI.center_text(Fore.YELLOW + "~*~*~*~ THE ULTIMATE JOB APPLICATION SIMULATOR ~*~*~*~" + Style.RESET_ALL, 100))
        print()

    @staticmethod
    def show_loading_bar(message="Loading", duration=1.5):
        """Show a retro loading bar"""
        print(f"\n{Fore.CYAN}{message}...", end="", flush=True)
        bar_length = 30
        for i in range(bar_length):
            time.sleep(duration / bar_length)
            print(f"{Fore.GREEN}█", end="", flush=True)
        print(f" {Fore.YELLOW}DONE!{Style.RESET_ALL}\n")
        time.sleep(0.3)

    @staticmethod
    def animate_text(text, delay=0.03):
        """Animate text character by character"""
        for char in text:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def show_glitch_effect(text, times=3):
        """Show glitchy text effect"""
        glitch_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        import random

        for _ in range(times):
            glitched = ""
            for char in text:
                if random.random() < 0.3 and char != " ":
                    glitched += random.choice(glitch_chars)
                else:
                    glitched += char
            print(f"\r{Fore.RED}{glitched}{Style.RESET_ALL}", end="", flush=True)
            time.sleep(0.1)

        print(f"\r{Fore.GREEN}{text}{Style.RESET_ALL}")

    @staticmethod
    def show_score(score, high_score, combo=0):
        """Display current score with retro styling"""
        score_text = f"SCORE: {score:,} | HIGH SCORE: {high_score:,}"
        if combo > 1:
            score_text += f" | {Fore.YELLOW}COMBO x{combo}!{Style.RESET_ALL}"

        print(Fore.MAGENTA + "═" * 80 + Style.RESET_ALL)
        print(Fore.CYAN + UI.center_text(score_text, 80) + Style.RESET_ALL)
        print(Fore.MAGENTA + "═" * 80 + Style.RESET_ALL)

    @staticmethod
    def show_level_complete(level, score, new_high_score=False):
        """Show level completion screen"""
        UI.clear()
        print("\n" * 3)

        messages = [
            f"{Fore.GREEN}╔═══════════════════════════════════════╗",
            f"{Fore.GREEN}║  🎉 LEVEL {level} COMPLETE! 🎉           ║",
            f"{Fore.GREEN}╠═══════════════════════════════════════╣",
            f"{Fore.YELLOW}║  Score: {score:,}".ljust(40) + f"{Fore.GREEN}║",
        ]

        if new_high_score:
            messages.append(f"{Fore.MAGENTA}║  ★ NEW HIGH SCORE! ★                 ║")

        messages.append(f"{Fore.GREEN}╚═══════════════════════════════════════╝")

        for msg in messages:
            print(UI.center_text(msg, 100))

        print("\n")
        time.sleep(2)

    @staticmethod
    def get_input(prompt, color=Fore.CYAN):
        """Get user input with styled prompt"""
        return input(f"{color}➤ {prompt}{Style.RESET_ALL}: ").strip()

    @staticmethod
    def show_menu(title, options, color=Fore.CYAN):
        """Show a menu and get selection"""
        print(f"\n{color}╔{'═' * 50}╗{Style.RESET_ALL}")
        print(f"{color}║ {title.center(48)} ║{Style.RESET_ALL}")
        print(f"{color}╠{'═' * 50}╣{Style.RESET_ALL}")

        for i, option in enumerate(options, 1):
            print(f"{color}║ {Fore.YELLOW}{i}.{Style.RESET_ALL} {option.ljust(45)} {color}║{Style.RESET_ALL}")

        print(f"{color}╚{'═' * 50}╝{Style.RESET_ALL}\n")

    @staticmethod
    def pause(message="Press ENTER to continue"):
        """Pause and wait for user input"""
        input(f"\n{Fore.YELLOW}{message}...{Style.RESET_ALL}")
