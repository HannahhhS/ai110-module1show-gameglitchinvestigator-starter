# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
This game is a sumple number guessing game, in which the computer chooses a random number, and the user has to guess the number
- [ ] Detail which bugs you found.
The session state doesnt update correctly for a new game. Furthermore, the hints are incorect, as they are often backwards than what is expected. There are a new minor issues with the ranges of the difficulties as well. 
- [ ] Explain what fixes you applied.
The fixes that were applied fixed the high low error and the session state bug, so it correctly stays and updates as needed for a new game. Furthermore, fixes to fix the ranges of each game value were also applied. The game now runs as intented, with correct hints being given 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:


1. User enters a guess of 25 (Normal mode)
2. Game returns "Go HIGHER"
3. User enters a guess of 35 → "Go HIGHER"
4. User enters a guess of 40 -> "Go LOWER"
5. User enters 36, number guess correctly, final score of 15

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
.....                                                                                                                                           [100%]

============================================================================== 5 passed in 0.02s =======================```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
