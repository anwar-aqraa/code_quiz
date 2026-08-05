import json


def load_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    return questions


def get_categories(questions):
    categories = []

    for question in questions:
        category = question["category"]

        if category not in categories:
            categories.append(category)

    return categories


def filter_questions(questions, category):
    filtered = []

    for question in questions:
        if question["category"] == category:
            filtered.append(question)

    return filtered


def get_difficulties(questions):

    difficulties = []

    for question in questions:
        difficulty = question["difficulty"]

        if difficulty not in difficulties:
            difficulties.append(difficulty)

    return difficulties



def filter_by_difficulty(questions, difficulty):

    filtered = []

    for question in questions:

        if question["difficulty"] == difficulty:
            filtered.append(question)

    return filtered
