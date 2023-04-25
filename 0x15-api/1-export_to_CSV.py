#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,"""
import csv

import requests
from sys import argv


def to_cvs():
    """return API data """
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    for u in users.json():
        if u.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (u.get('name'))
            break

    TASK_STATUS_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))
    """import to cvs"""
    filename = "{}.csv".format(argv[1])
    with open(filename, 'w') as cvsfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(cvsfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for t in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1],
                             "USERNAME": EMPLOYEE_NAME,
                             "TASK_COMPLETED_STATUS": t[0],
                             "TASK_TITLE": t[1]})


if __name__ == "__main__":
    to_cvs()
