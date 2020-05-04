#!/usr/bin/python3
"""
Makes requet to JSONPlaceholder API
"""


import requests
import sys


def main():
    """
    use requests to retireve a json file
    """
    us_url = "https://jsonplaceholder.typicode.com/users/"
    us_url += str(sys.argv[1])
    tasks_url = us_url + "/todos"
    todos = requests.get(tasks_url).json()
    # print(todos)
    user = requests.get(us_url).json()
    # print(user)
    doned = []
    for val in todos:
        if val.get("completed"):
            doned.append(val)
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(doned),
                                                          len(todos)))
    for task in doned:
        print('\t {}'.format(task.get("title")))


if __name__ == '__main__':
    main()
