#!/usr/bin/python3
"""
communicates with jsonplaceholder api to get
todos of employee with <userId> (passed as
command line argument) and saves it as csv
"""

import csv
import requests
import sys


def createCsv():
    """
    Gets employee todos and saves
    them in a csv file
    """
    if len(sys.argv) < 2:
        return

    userId = sys.argv[1]

    todoURL = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    userURL = f"https://jsonplaceholder.typicode.com/users/{userId}"

    todoResp = requests.get(todoURL).json()
    userResp = requests.get(userURL).json()

    fieldnames = ['userId', 'username', 'completed', 'title']

    with open(f"{userId}.csv", 'a+') as csvFile:
        writer = csv.DictWriter(
            csvFile, fieldnames=fieldnames,
            quotechar='"', quoting=csv.QUOTE_ALL)

        for todo in todoResp:
            todo['username'] = userResp.get('username')
            todo = {key: todo[key] for key in fieldnames}
            writer.writerow(todo)


if __name__ == "__main__":
    createCsv()
