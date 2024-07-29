#!/usr/bin/python3

import requests
import sys


def display_info():
    if len(sys.argv) < 2:
        return

    userId = sys.argv[1]

    todoURL = f"https://jsonplaceholder.typicode.com/todos?userId={userId}"
    userURL = f"https://jsonplaceholder.typicode.com/users/{userId}"

    todoResp = requests.get(todoURL).json()
    userResp = requests.get(userURL).json()

    name = userResp.get('name')
    completedTasks = sum(todo.get('completed') for todo in todoResp)
    totalTasks = len(todoResp)

    print(f"Employee {name} is done with tasks({completedTasks}/{totalTasks}):")

    for todo in todoResp:
        if todo.get('completed'):
            print(f"\t {todo.get('title')}")


if __name__ == "__main__":
    display_info()
