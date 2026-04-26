<div align="center">

# 🎯 Guessing Game

![Python](https://img.shields.io/badge/Python-3.x-00ff41?style=for-the-badge&logo=python&logoColor=00ff41&labelColor=0d1117)
![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-00ff41?style=for-the-badge&labelColor=0d1117)
![Status](https://img.shields.io/badge/Status-Complete-00ff41?style=for-the-badge&labelColor=0d1117)

> **Project #1 — My first ever Python project. Started from zero. 🖤**

</div>

---

## 💡 What It Does

```
Computer picks a secret number between 1 and 100.
You keep guessing until you find it.
Too high? Too low? It tells you.
Get it right → You win. 🎉
```

---

## 🎮 Demo

```bash
WELCOME TO THE GUESSING GAME!
> Enter your guess between 1 and 100: 50
  Too low, try again!
> Enter your guess between 1 and 100: 75
  Too high, try again!
> Enter your guess between 1 and 100: 63
  Congratulations! You guessed the number: 63 🎉
```

---

## ▶️ Run It

```bash
python guessing_game.py
```

---

## 🧠 Concepts Used

| Concept | Purpose |
|---------|---------|
| `random.randint(1, 100)` | Generate the secret number |
| `int(input())` | Get user's guess as a number |
| `while True` | Keep asking until correct |
| `if / elif / else` | Check if too high, too low, or correct |
| `break` | Exit loop when user wins |

---

## 💻 Source Code

```python
import random

secret_number = random.randint(1, 100)
print("WELCOME TO THE GUESSING GAME!")

while True:
    guess = int(input("Enter your guess between 1 and 100: "))
    if guess < secret_number:
        print("Too low, try again!")
    elif guess > secret_number:
        print("Too high, try again!")
    elif guess == secret_number:
        print("Congratulations! You guessed the number:", secret_number)
        break
    else:
        print("Invalid input, please enter a number between 1 and 100")
```

---

<div align="center">

[🔙 Back to Portfolio](../README.md) • [👤 My Profile](https://github.com/AYDINKHAN)

</div>
