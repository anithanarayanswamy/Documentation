# TODO App Test

## Model States

The test model consists of the following three states:

- **start**: Initial state with browser setup.
- **empty**: Todo list is empty.
- **list**: Todo list has items.

### Model Edges (Actions)

- **initialize**: Start the application.
- **add_todo**: Add a new todo item.
- **toggle_todo**: Mark/unmark todo as completed.
- **delete_todo**: Remove a todo item.
- **cleanup**: Clean up resources.

The test generator creates test sequences based on this model, ensuring thorough coverage of the todo application's functionality.

::: todo-app.tests.test.TodoModel
