#!/usr/bin/python3
"""
Makes request to JSONPlaceholder API
and save response as .csv
"""


import csv
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
    with open("{}.csv".format(sys.argv[1]), "w") as csv_file:
        fields = ["USER_ID",
                  "USER_NAME",
                  "TASK_COMPLETED_STATUS",
                  "TASK_TITLE"]
        writer = csv.DictWriter(csv_file,
                                fieldnames=fields,
                                quoting=csv.QUOTE_ALL)
        for task in todos:
            tmp_dict = {}
            tmp_dict[fields[0]] = str(sys.argv[1])
            tmp_dict[fields[1]] = str(user.get("username"))
            tmp_dict[fields[2]] = str(task.get("completed"))
            tmp_dict[fields[3]] = str(task.get("title"))
            writer.writerow(tmp_dict)


if __name__ == '__main__':
    main()
