#!/usr/bin/python3
"""
communicates with jsonplaceholder api to get
todos of all employees and creates a json file
where it dumps that data
"""

import json
import requests


def allEmployeeTodos():
    """
    Creates json file with all employee todos
    """
    userURL = f"https://jsonplaceholder.typicode.com/users"
    userResp = requests.get(userURL).json()

    jsonData = {}

    for user in userResp:
        uId = f"{user.get('id')}"
        username = user.get('username')
        jsonData[uId] = []

        todoURL = f"https://jsonplaceholder.typicode.com/todos?userId={uId}"
        todoResp = requests.get(todoURL).json()

        for todo in todoResp:
            keys = ['username', 'task', 'completed']
            todo['task'] = todo.pop('title')
            todo['username'] = username

            jsonData[uId].append({key: todo[key] for key in keys})

    with open(f"todo_all_employees.json", "w") as jsonFile:
        json.dump(jsonData, jsonFile)


if __name__ == "__main__":
    allEmployeeTodos()
