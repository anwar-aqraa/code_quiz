import time


def start_quiz(questions):

    score = 0
    correct_answers = 0
    streak = 0
    max_streak = 0

    points_system = {
     "easy": 5,
     "medium": 10,
     "hard": 20
    }
    total_questions = len(questions)


    for index, question in enumerate(questions):

        start_time = time.time()


        print("\n----------------")
        print(
            f"Question {index + 1}/{total_questions}"
        )

        print(question["question"])


        for i, option in enumerate(question["options"]):
            print(f"{i}. {option}")


        while True:
            try:
                answer = int(
                    input("Your answer: ")
                )
                break

            except ValueError:
                print("Please enter a number!")


        end_time = time.time()

        elapsed = end_time - start_time


        if elapsed > 15:

            print(
                "⏰ Time's up!"
            )
            streak = 0
            continue



        if answer == question["answer"]:

            print("✅ Correct!")

            correct_answers += 1

            streak += 1


            if streak > max_streak:
                max_streak = streak


            print(
                f"🔥 Current Streak: {streak}"
            )

            points = points_system[
                  question["difficulty"]
            ]

            if elapsed < 5:
                points += 5
                print("⚡ Speed bonus +5")


            elif elapsed < 10:
                points += 2
                print("⚡ Speed bonus +2")


            if streak == 3:
                points += 5
                print("🔥 Streak bonus +5")

            elif streak == 5:
                points += 10
                print("🔥🔥 Streak bonus +10")

            elif streak == 10:
                points += 20
                print("🔥🔥🔥 Streak bonus +20")




            score += points



        else:

            print("❌ Wrong!")

            print(
                f"Correct answer: "
                f"{question['options'][question['answer']]}"
            )
            if streak > 0:
                print(
                    f"💔 Streak broken! You had {streak} correct answers."
                )

            streak = 0


    percentage = (
        correct_answers / total_questions
    ) * 100



    print("\n====================")
    print("🎮 Quiz Finished!")
    print("====================")

    print(
        f"Correct answers: "
        f"{correct_answers}/{total_questions}"
    )

    print(
        f"Score: {score} points"
    )

    print(
        f"Success rate: {percentage:.1f}%"
    )

    print(
        f"🏆 Best Streak: {max_streak}"
    )
    return score
