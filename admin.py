import json


def load_questions():

    with open("questions.json", "r") as file:
        return json.load(file)



def save_questions(questions):

    with open("questions.json", "w") as file:
        json.dump(
            questions,
            file,
            indent=4
        )



def add_question():

    questions = load_questions()

    print("\n====== Add Question ======")

    category = input("Category: ")

    difficulty = input(
        "Difficulty (easy/medium/hard): "
    )

    question_text = input(
        "Question: "
    )


    options = []

    for i in range(4):

        option = input(
            f"Option {i}: "
        )

        options.append(option)


    answer = int(
        input(
            "Correct answer index (0-3): "
        )
    )


    new_question = {

        "category": category,

        "difficulty": difficulty,

        "question": question_text,

        "options": options,

        "answer": answer
    }


    questions.append(new_question)


    save_questions(questions)


    print(
        "\n✅ Question Added!"
    )



def edit_question():

    questions = load_questions()


    print("\n====== Edit Question ======")


    for index, question in enumerate(
        questions,
        start=1
    ):

        print(
            f"{index}. {question['question']}"
        )


    choice = int(
        input(
            "\nChoose question number: "
        )
    )


    if choice < 1 or choice > len(questions):

        print(
            "❌ Invalid question number!"
        )

        return



    question = questions[choice - 1]


    print("\nLeave empty to keep old value")


    new_question = input(
        f"Question ({question['question']}): "
    )


    if new_question:

        question["question"] = new_question



    new_category = input(
        f"Category ({question['category']}): "
    )


    if new_category:

        question["category"] = new_category



    new_difficulty = input(
        f"Difficulty ({question['difficulty']}): "
    )


    if new_difficulty:

        question["difficulty"] = new_difficulty



    print("\nCurrent Options:")

    for i, option in enumerate(
        question["options"]
    ):

        print(
            f"{i}. {option}"
        )



    change_options = input(
        "Change options? (y/n): "
    )



    if change_options.lower() == "y":


        options = []


        for i in range(4):

            option = input(
                f"Option {i}: "
            )

            options.append(option)


        question["options"] = options



    new_answer = input(
        f"Correct answer ({question['answer']}): "
    )


    if new_answer:

        question["answer"] = int(new_answer)



    save_questions(questions)


    print(
        "\n✅ Question Updated!"
    )



def delete_question():

    questions = load_questions()


    print("\n====== Delete Question ======")


    if len(questions) == 0:

        print(
            "No questions available!"
        )

        return



    for index, question in enumerate(
        questions,
        start=1
    ):

        print(
            f"{index}. {question['question']}"
        )



    choice = int(
        input(
            "\nChoose question number to delete: "
        )
    )



    if choice < 1 or choice > len(questions):

        print(
            "❌ Invalid question number!"
        )

        return



    deleted_question = questions.pop(
        choice - 1
    )



    save_questions(
        questions
    )



    print(
        "\n🗑️ Question deleted!"
    )

    print(
        deleted_question["question"]
    )