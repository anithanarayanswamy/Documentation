# Welcome to MkDocs
## Overview

The **Todo App** is a simple Flask-based application that allows users to manage a todo list. It includes the ability to add new items, toggle their completion status, and delete them from the list.

The application serves a simple web interface that interacts with a backend data structure to store and modify todos. Below is the breakdown of the app's structure and key functionality.


## Project layout

    My-documentation/
    ├── todo-app/
    │   ├── app.py
    │   ├── templates/
    │   │   └── index.html
    │   ├── models/
    │   │   └── todo.json
    │   ├── tests/
    │   │   └── test.py
    ├── requirements.txt
    ├── mkdocs.yml
    └── docs/
        ├── index.md
        ├── test.md
        ├── todo-app.md


## Bringing the Todo App Up

To run the Flask application, use the following steps:

1. **Start the Flask application** (in one terminal):
    ```bash
    python app.py
    ```

2. **Verify the model** (in another terminal):
    ```bash
    altwalker check models/todo.json tests/test.py
    ```

3. **Run the tests**:
    ```bash
    altwalker online -m models/todo.json "random(vertex_coverage(100))" tests/test.py
    ```

### Notes

- The application runs on [http://localhost:5000](http://localhost:5000).
- Tests use **Selenium WebDriver** with **Chrome**.
- Ensure that Chrome browser is installed on your machine.
- The model includes cleanup steps to properly close browser sessions.

**Test Execution Process**:
1. Verify the model:
    ```bash
    altwalker check models/todo.json tests/test.py
    ```
2. Then, run the tests:
    ```bash
    altwalker online -m models/todo.json "random(vertex_coverage(100))" tests/test.py
    ```

---

## Additional Documentation Files

- **[todo-app.md](todo-app.md)**: Detailed description of the Flask Todo App implementation.
- **[test.md](test.md)**: Explanation of the Todo App test model and how it's structured.

