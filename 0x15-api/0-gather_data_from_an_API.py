#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,"""
import requests
from sys import argv


def display():
    """ Get information from API """
    global EMPLOYEE_NAME
    url = "https://jsonplaceholder.typecode.com"
    users = requests.get('{}/users/'.format(url))
    for u in users.json():
        if u.get('id') == int(argv[1]):
            EMPLOYEE_NAME = u.get('name')
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []
    todos = requests.get('{}/todos?userId={}'.format(url, argv[1]))
    for t in todos.json():
        if t.get('completed') is True:
            NUMBER_OF_DONE_TASKS += 1
            TASK_TITLE.append(t.get('title'))
        TOTAL_NUMBER_OF_TASKS += 1

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks("
        f"{NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"
    )
    for t in TASK_TITLE:
        print("\t {}".format(t))


if __name__ == "__main__":
    display()
