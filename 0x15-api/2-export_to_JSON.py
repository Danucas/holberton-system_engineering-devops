#!/usr/bin/python3
"""
Makes request to JSONPlaceholder API
and save response as .csv
"""


import json
import requests
import sys


def main():
    """
    use requests to retireve a json file
    and saves it as csv file
    """
    us_url = "https://jsonplaceholder.typicode.com/users/"
    us_url += str(sys.argv[1])
    tasks_url = us_url + "/todos"
    todos = requests.get(tasks_url).json()
    user = requests.get(us_url).json()
    tasks = []
    for task in todos:
        tmp_dict = {}
        tmp_dict["task"] = str(task.get("title"))
        tmp_dict["completed"] = task.get("completed")
        tmp_dict["username"] = str(user.get("username"))
        tasks.append(tmp_dict)
    user_todo = {}
    user_todo[str(sys.argv[1])] = tasks
    print(json.dumps(user_todo))
    with open("{}.json".format(sys.argv[1]), "w") as jsonf:
        json.dump(user_todo, jsonf)


if __name__ == '__main__':
    main()
