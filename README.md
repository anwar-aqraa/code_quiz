# 🎮 CodeQuiz

CodeQuiz is a terminal-based quiz game built with Python.

It allows users to test their knowledge of programming and development topics such as **Docker, Linux, SQL, Git, Python, and JavaScript**.

The project was built as a personal project to practice Python, file handling, user management, game logic, and building a complete application from scratch.

## ✨ Features

* 🎮 Interactive terminal quiz
* 👤 User profiles
* 📊 Player statistics
* 📜 Quiz history
* 🏆 High scores
* 🔥 Streak system for consecutive correct answers
* ⚡ Speed bonuses
* 🎯 Difficulty levels:

  * 🟢 Easy — 5 points
  * 🟡 Medium — 10 points
  * 🔴 Hard — 20 points
* 🎲 Randomized questions
* 🎨 Colored terminal output
* 📚 Multiple categories:

  * Docker
  * Linux
  * SQL
  * Git
  * Python
  * JavaScript
* 🛠️ Admin mode

  * Add questions
  * Edit questions
  * Delete questions

## 🛠️ Technologies

* Python 3
* JSON
* Colorama
* Git & GitHub

## 📁 Project Structure

```text
code_quiz/
│
├── main.py
├── quiz.py
├── questions.py
├── questions.json
├── score.py
├── scores.json
├── user.py
├── users.json
├── admin.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/anwar-aqraa/code_quiz.git
```

### 2. Enter the project directory

```bash
cd code_quiz
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Game

Start CodeQuiz with:

```bash
python3 main.py
```

You will see the main menu:

```text
========== CodeQuiz ==========
1. Start Quiz
2. My Profile
3. My History
4. Categories
5. High Scores
6. Statistics
7. Exit
```

Choose an option and follow the instructions in the terminal.

## 👤 User Profiles

When you start CodeQuiz, you enter a username.

If the user already exists, CodeQuiz welcomes them back.

Each profile stores information such as:

* Username
* Number of games played
* Best score
* Average score
* Favorite category
* Quiz history

## 🎯 Difficulty System

Questions have different difficulty levels with different base scores:

| Difficulty | Points |
| ---------- | ------ |
| 🟢 Easy    | 5      |
| 🟡 Medium  | 10     |
| 🔴 Hard    | 20     |

Players can choose a difficulty before starting a quiz.

## 🔥 Streak System

Correct answers in a row create a streak.

The game rewards longer streaks with bonus points.

For example:

```text
🔥 Current Streak: 3
🔥 Streak bonus +5
```

Getting an answer wrong breaks the streak.

## ⚡ Speed Bonus

Players can also earn bonus points for answering quickly.

```text
⚡ Speed bonus +5
```

The faster you answer correctly, the more bonus points you can earn.

## 🎲 Random Questions

Questions are shuffled every time a quiz starts.

This means the order of questions is different for every game.

## 🛠️ Admin Mode

CodeQuiz includes an admin mode for managing the question database.

Admins can:

* Add questions
* Edit questions
* Delete questions

This allows new questions to be added without manually editing `questions.json`.

## 📊 Data Storage

CodeQuiz currently uses JSON files to store application data.

### `questions.json`

Stores quiz questions, categories, difficulties, options, and correct answers.

### `users.json`

Stores player profiles and quiz history.

### `scores.json`

Stores quiz scores.

## 📦 Dependencies

The project uses:

```text
colorama
```

All required dependencies are listed in:

```text
requirements.txt
```

## 🤝 Contributing

This is a personal learning project, but suggestions and improvements are welcome.

If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request.

## 📄 License

This project is for educational and personal use.

```
```

