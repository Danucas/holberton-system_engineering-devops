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
    us_url = "https://jsonplaceholder.typicode.com/users"
    tasks_url = "/todos"
    users = requests.get(us_url).json()
    all_tasks = {}
    for user in users:
        url = us_url + '/' + str(user.get("id"))
        url += tasks_url
        todos = requests.get(url).json()
        user_tasks = []
        for task in todos:
            tmp_dict = {}
            tmp_dict["task"] = str(task.get("title"))
            tmp_dict["completed"] = task.get("completed")
            tmp_dict["username"] = str(user.get("username"))
            user_tasks.append(tmp_dict)
        all_tasks[str(user.get("id"))] = user_tasks
    with open("todo_all_employees.json", "w") as jsonf:
        json.dump(all_tasks, jsonf)


if __name__ == '__main__':
    main()
