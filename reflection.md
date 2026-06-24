# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
Game started on normal mode. Asked to guess number between 1-100. 7 Attempts remaining
- List at least two concrete bugs you noticed at the start  
   hints are backwards. Game says higher as a hint when it should be lower. Different modes have different ranges, such as easy being between 1 and 20. However the secret number is still sometimes above 20, such as 71
  The new game button also doesnt work if a level has been failed or passed. A refresh is needed to start a new game. The hard mode isnt actually harder (0-50), while normal is 0-100

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 50| Hint of go HIGHER | Hint of go LOWER| Secret NUmber - 74 |
| 100| go LOWER | go HIGHER | None, secret num still 74 |
| 5| go HIGHER| go LOWE | None|
Easy Level -> when game failed, restart button should work -> output is "game over, start a new game..."

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
AI suggested that the messages were flipped, and that when the guess was higher the message should actually be go LOWER. tHis was the correct fix, as that is how the logic of the game works. If the guess is too lowe, the person has to guess higher the next time. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
"New Game" resets attempts to 0 but the initial state uses 1 (lines 96, 135)
This was slightly misleading, as it doesnt actually hit at the core of why the game didnt reset correctly. The correct fix is that the new game didnt update correctly since the status, st.session_state.status didnt update

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided if a bug was really fixed by testing the different adge cases multiple times. For example, to check if the high low bug was fixed, I tried using both the normal and hard mode. I tested using negative numbers, boundary numbers, and numbers out of the range. For each of these cases the output was as expected. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Another test I used to test if the reset game wprled correctly was purposly faoling an attempt, and then using the new game button. I also tried this when a game was won, to see if it would create a new game. This was a manual test i completed. I did it when passing a hard level and failing a normal level. 
- Did AI help you design or understand any tests? How?
AI wasnt super helpful with any of these tests, especially the manual ones, since they are pretty intuitaive already

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
 A rerun basically happens any time you interact with a button on the screen, so something like the submit. It runs a specific file. Session state is something that persists even across reruns. The issue with the restart was that the status persisted even across the reruns, instead of it being manually reset

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  A strategy I learned was being able to ask the AI to refactor the code, as it removes alot of manual labor that I would have to do on my own. 
- What is one thing you would do differently next time you work with AI on a coding task?
I would want to try doing more of the fixes myself and ask AI to check it, as I feel like it helps me think through what needs to be changed more if I make some of the changes myself. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project made me realize that AI can generate decent anigh code, but it might to better with fixing code that is already written rather than writing something new from scratch. For example when generating the commit message, the AI coudnt properly figure out the final commits, and for a larger message it was way too many lines. 
