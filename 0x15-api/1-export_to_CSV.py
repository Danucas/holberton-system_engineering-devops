#!/usr/bin/python3
"""
Makes requet to JSONPlaceholder API
and saves it as .csv
"""


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
    # print(todos)
    user = requests.get(us_url).json()
    # print(user)
    with open("{}.csv".format(sys.argv[1]), "w") as csv_file:
        for task in todos:
            csv_file.write('"{}",'.format(sys.argv[1]))
            csv_file.write('"{}",'.format(user.get("name")))
            csv_file.write('"{}",'.format(task.get("completed")))
            csv_file.write('"{}"'.format(task.get("title")))
            csv_file.write('\n')
    csv_file.close()


if __name__ == '__main__':
    main()
