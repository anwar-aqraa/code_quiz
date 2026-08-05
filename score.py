import json
from datetime import datetime


def save_score(name, category, score):

    result = {
        "name": name,
        "category": category,
        "score": score,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }


    with open("scores.json", "r") as file:
        scores = json.load(file)


    scores.append(result)


    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)



def show_scores():

    with open("scores.json", "r") as file:
        scores = json.load(file)


    if not scores:
        print("\nNo scores yet!")
        return


    scores = sorted(
        scores,
        key=lambda x: x["score"],
        reverse=True
    )


    print("\n========== High Scores ==========")


    for index, score in enumerate(scores[:10]):

        print(
            f"{index+1}. "
            f"{score['name']} - "
            f"{score['category']} - "
            f"{score['score']} pts "
            f"({score['date']})"
        )



def show_statistics():

    with open("scores.json", "r") as file:
        scores = json.load(file)


    if not scores:
        print("\nNo statistics available!")
        return


    total_games = len(scores)

    total_score = sum(
        score["score"]
        for score in scores
    )

    average = total_score / total_games


    best = max(
        scores,
        key=lambda x: x["score"]
    )


    print("\n========== Statistics ==========")

    print(f"Total games: {total_games}")
    print(f"Average score: {average:.2f}")

    print(
        f"Best player: {best['name']} "
        f"with {best['score']} pts"
    )
