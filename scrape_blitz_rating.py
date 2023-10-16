import lichess


def get_rating(user):
    myClient = lichess.Client()
    rating = myClient.get_stats(f'{user}', 'blitz')
    rating_figure = rating['perf']['glicko']['rating']
    return rating_figure


def main():
    print('Type the username of player')
    print('Type "stop" to exit')
    while True:
        user = input('> ')
        if user == 'stop':
            break
        rating = get_rating(user)
        print(f"{user}'s rating is {rating}")


if __name__ == '__main__':
    main()