# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game loaded and looked playable, but the logic underneath was inconsistent. The biggest issue was that the hint messages did not always match the guess, so a guess that should have been "Too High" could behave differently on alternating turns. I also noticed the attempts display started one lower than expected, and starting a new game could ignore the selected difficulty range.

- The hint logic sometimes lied because the secret number was converted to a string on every other attempt, which changed how comparisons behaved.
- The attempts counter started at 1 instead of 0, so the game showed fewer attempts left than the player actually had.
- Clicking "New Game" reset the secret number to a 1-100 range even if the selected difficulty was Easy or Hard.

**Bug Reproduction Logs**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when the secret is 50 | Show "Too High" and the matching higher/lower hint | The hint could flip because the secret was sometimes treated as a string instead of a number | none |
| Open the game on first load | Show the full number of attempts allowed for the selected difficulty | Attempts left started one too low because the counter began at 1 | none |
| Choose Easy, then click New Game | Keep the secret inside the Easy range | The new secret was generated from 1 to 100 instead of the selected difficulty range | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used GitHub Copilot in VS Code to inspect the broken game logic and help me separate the UI from the core rules. One correct suggestion was to move the comparison and parsing helpers into `logic_utils.py` so the app could import the same logic everywhere; I verified that by checking the diff and confirming the logic file now contains the shared functions. One misleading idea from the original AI generated code was to convert the secret number to a string on alternating turns, which made the hint logic behave inconsistently. I rejected that approach after tracing why the high/low hints changed between attempts.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when the logic in `app.py` and `logic_utils.py` matched the behavior I expected from the game rules: guesses were compared numerically, the secret stayed inside the selected difficulty range, and the score only changed on a win. I added targeted pytest cases for `check_guess`, `parse_guess`, and `update_score` so the exact bug behavior was covered in a repeatable way. AI helped me identify what to test by pointing out that the original bug came from inconsistent state and type handling, which turned into the tests for blank input, correct hint output, and score updates.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Streamlit reruns the script every time the user clicks a button or changes an input, so the app has to rebuild its interface from top to bottom on each interaction. Session state is the part that survives those reruns, which is why it is useful for keeping the secret number, attempts, and score from resetting on every click. In this project, the bug happened because the game logic was not treating session state consistently, so the app looked fresh even when the hidden state was drifting.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is writing a small test for the exact behavior I am debugging before I try to fix anything else. Next time I work with AI, I would ask it to explain the logic step by step before letting it rewrite code, because that makes it easier to spot when it is proposing a fix that only looks plausible. This project made me treat AI generated code as a draft that still needs human verification, especially when state and type conversions can hide bugs that are not obvious from the UI.
