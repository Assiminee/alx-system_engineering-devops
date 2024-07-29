#!/usr/bin/python3
"""
communicates with jsonplaceholder api to get
todos of employee with <userId> (passed as
command line argument) and creates json file
containing all todos
"""

import json
import requests
import sys


def employeeTodosJson():
    """
    creates json file containing employee todos
    """
    if len(sys.argv) < 2:
        return

    userId = sys.argv[1]

    todoURL = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    userURL = f"https://jsonplaceholder.typicode.com/users/{userId}"

    todoResp = requests.get(todoURL).json()
    userResp = requests.get(userURL).json()

    username = userResp.get('username')

    jsonData = {f"{userId}": []}

    for todo in todoResp:
        keys = ['task', 'completed', 'username']
        todo['task'] = todo.pop('title')
        todo['username'] = username

        jsonData[f"{userId}"].append({key: todo[key] for key in keys})

    with open(f"{userId}.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)


if __name__ == "__main__":
    employeeTodosJson()
