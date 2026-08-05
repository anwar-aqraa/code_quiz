import json


def load_users():

    with open("users.json", "r") as file:
        return json.load(file)



def save_users(users):

    with open("users.json", "w") as file:
        json.dump(
            users,
            file,
            indent=4
        )



def create_user(username):

    user = {
        "username": username,
        "total_games": 0,
        "best_score": 0,
        "total_score": 0,
        "average_score": 0,
        "favorite_category": None,
        "history": []
    }

    users = load_users()

    users.append(user)

    save_users(users)

    return user



def get_user(username):

    users = load_users()

    for user in users:

        if user["username"].lower() == username.lower():
            return user

    return None



def login(username):

    user = get_user(username)

    if user:
        print(
            f"\nWelcome back {user['username']} 👋"
        )

        return user


    print(
        "\nNew player created 🎮"
    )

    return create_user(username)



def update_user(user):

    users = load_users()


    for index, item in enumerate(users):

        if item["username"] == user["username"]:

            users[index] = user
            break

    save_users(users)



def show_profile(user):

    print("\n====== Profile ======")

    print(
        f"Username: {user['username']}"
    )

    print(
        f"Games Played: {user['total_games']}"
    )

    print(
        f"Best Score: {user['best_score']}"
    )

    print(
        f"Average Score: {user['average_score']}"
    )

    print(
        f"Favorite Category: {user['favorite_category']}"
    )


def show_history(user):

    print("\n====== Quiz History ======")

    if len(user["history"]) == 0:
        print("No games played yet 🎮")
        return


    for index, game in enumerate(
        user["history"],
        start=1
    ):

        print("\nGame", index)

        print(
            f"Category: {game['category']}"
        )

        print(
            f"Score: {game['score']}"
        )

        print(
            f"Date: {game['date']}"
        )
