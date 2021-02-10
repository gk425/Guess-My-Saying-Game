# Guess-My-Saying-Game
## Introduction
- In the game, the player is given a popular saying with all the letters blanked out. The player must guess what the saying is, one letter at a time. To win, the player must guess the saying with fewer than 10 wrong guesses. The saying is randomly picked from the “Sayings.txt” file, which the player has to guess.

## Features
1. The program does not make distinctions between uppercase and lowercase letter guesses, though it displays the letter as it appears in the original saying.  (For example, if the original saying is “Hello, World!”, the player should initially see “_____, _____!”, and if the player guesses ‘w’, that should count as a correct guess.  The next display should be “_____, W____!”)
2. The program remembers what wrong guesses the player already made. If the player repeats a wrong guess, the program tells the player that they already tried that letter, and doesn’t count it again towards the number of wrong guesses.
3. The program handles gracefully cases where the player’s input isn’t just a letter.   Inputs to watch out for:
  - If the player didn’t enter anything, just hit Enter.
  - If the player wrote something that’s more than one character long (e.g., ‘ex’).
  - If the player gave a character that is not a letter (e.g., ‘2’)
4. Instead of ending the game after one saying or 10 wrong guesses, the program asks if the player wants to play again.  If yes, it plays again.  If no, the program ends.

## Screen Shot Image
![Screen Shot 2021-02-10 at 12 54 20 AM](https://user-images.githubusercontent.com/75402947/107471105-8e9f1e80-6b3a-11eb-83d6-754f6542510f.png)
