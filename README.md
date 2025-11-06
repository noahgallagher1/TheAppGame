# 🎮 THE APPLICATION

**The Ultimate Job Application Simulator**

A hilarious retro 90s-styled terminal game where you fill out increasingly absurd job applications, complete ridiculous CAPTCHAs, and race against time to get hired!

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 🌟 Features

- **10 Unique Levels**: From mundane data entry to God-Emperor of Form Filling
- **Progressive Difficulty**: Questions start normal, then get hilariously absurd
- **Fun CAPTCHAs**: Math problems, word verification, image selection, sliders, and philosophical questions
- **Scoring System**: Combo multipliers, time bonuses, and accuracy rewards
- **High Scores**: Track your best performances across all levels
- **90s Aesthetic**: Colorful retro terminal graphics with rainbow text and ASCII art
- **Level Unlocking**: Beat levels to unlock new challenges
- **Statistics Tracking**: Monitor your jobs applied count and personal bests

## 🎯 Game Mechanics

### Scoring
- **Base Points**: 100 points per correct answer
- **Time Bonus**: Up to 50 bonus points for fast answers
- **Combo System**: Chain correct answers for multipliers (up to x10)
- **CAPTCHA Bonus**: 500 points for successful verification
- **Level Completion**: Massive bonuses based on speed, accuracy, and max combo

### Questions
Questions evolve as you progress:
1. **Levels 1-2**: Normal job application questions
2. **Levels 3-4**: Corporate buzzwords and getting weird
3. **Levels 5-6**: Speed rounds and trivia
4. **Levels 7-8**: Random chaos and existential questions
5. **Levels 9-10**: Ultimate challenge mixing everything

## 🚀 Installation

### Requirements
- Python 3.7 or higher
- pip (Python package manager)

### Setup

```bash
# Clone or download the repository
cd TheAppGame

# Install dependencies
pip install -r requirements.txt

# Run the game
python3 the_application.py
```

Or make it executable and run directly:

```bash
chmod +x the_application.py
./the_application.py
```

## 🎮 How to Play

### Main Menu
1. **START GAME**: Begin from Level 1
2. **LEVEL SELECT**: Choose any unlocked level
3. **VIEW HIGH SCORES**: See your achievements
4. **EXIT**: Quit the game

### During Gameplay
- Type your answers when prompted
- Answer quickly for time bonuses
- Keep your combo alive by answering correctly
- Complete CAPTCHAs to finish each level
- Type 'quit' during a question to exit

### Tips for High Scores
- **Speed matters**: Faster correct answers = more points
- **Maintain combos**: Wrong answers reset your multiplier
- **Know the trivia**: Some questions have specific answers
- **Practice CAPTCHAs**: Get familiar with all types
- **Play all levels**: Later levels offer bigger bonuses

## 📊 Game Levels

| Level | Job Title | Difficulty | Questions |
|-------|-----------|------------|-----------|
| 1 | Junior Data Entry Clerk | ⭐ | 5 |
| 2 | Assistant Manager | ⭐⭐ | 7 |
| 3 | Synergy Optimization Specialist | ⭐⭐ | 8 |
| 4 | Chief Meme Officer | ⭐⭐⭐ | 10 |
| 5 | Professional Question Answerer | ⭐⭐⭐⭐ | 12 |
| 6 | Cultural Knowledge Validator | ⭐⭐⭐ | 9 |
| 7 | Reality Distortion Field Engineer | ⭐⭐⭐⭐ | 10 |
| 8 | Existential Question Processor | ⭐⭐⭐⭐ | 11 |
| 9 | Supreme Overlord of Application Forms | ⭐⭐⭐⭐⭐ | 13 |
| 10 | God-Emperor of Form Filling | ⭐⭐⭐⭐⭐ | 15 |

## 🎨 CAPTCHA Types

- **Math CAPTCHA**: Solve simple arithmetic
- **Word CAPTCHA**: Type distorted corporate buzzwords
- **Image Selection**: Pick all items matching a category
- **Slider CAPTCHA**: Move to the correct position
- **Absurd CAPTCHA**: Answer philosophical questions

## 💾 Save System

The game automatically saves:
- Overall high score
- High score for each level
- Number of jobs applied (times played)
- Unlocked levels

Save file: `game_save.json` (created automatically)

## 🏆 Achievements to Chase

- Complete all 10 levels
- Get a 10x combo multiplier
- Achieve 100% accuracy on a level
- Beat a level in under 60 seconds
- Score over 50,000 points
- Apply to 100+ jobs

## 🛠️ Technical Details

### Project Structure
```
TheAppGame/
├── the_application.py  # Main game loop and logic
├── ui.py              # UI rendering and 90s aesthetics
├── game_state.py      # Save/load system
├── levels.py          # Level definitions and questions
├── captcha.py         # CAPTCHA system
├── scoring.py         # Scoring and combo system
├── requirements.txt   # Dependencies
└── README.md         # This file
```

### Dependencies
- `colorama`: For colorful terminal output

## 🐛 Troubleshooting

**Colors not displaying correctly?**
- Make sure your terminal supports ANSI colors
- Try a different terminal emulator

**Game running slowly?**
- Some terminals may have performance issues with rapid screen clearing
- Try running in a native terminal instead of IDE terminal

**Save file issues?**
- Delete `game_save.json` to reset progress
- Make sure the game has write permissions in its directory

## 🎮 Example Gameplay

```
████████╗██╗  ██╗███████╗
╚══██╔══╝██║  ██║██╔════╝
   ██║   ███████║█████╗
   ██║   ██╔══██║██╔══╝
   ██║   ██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝

SCORE: 5,420 | HIGH SCORE: 12,890 | COMBO x5!

Level 4 - Question 3/10
────────────────────────────────────────────────────────────────────────────────

Is a hot dog a sandwich? (yes/no)

[You have 6 seconds to answer]

➤ Answer:
```

## 📝 License

MIT License - Feel free to use and modify!

## 🎉 Fun Facts

- There are over 100 unique questions across all levels
- The meaning of life is actually 42 (it's in the game!)
- Some CAPTCHAs are intentionally absurd
- The final level is truly the boss fight of applications
- Your "jobs applied" counter is basically a measure of dedication (or madness)

---

**Made with 💙 and way too much coffee**

*Remember: The real job was the applications we filled along the way.*

🎮 **Ready to get hired? Run the game and start applying!** 🎮
