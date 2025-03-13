
import click # to create a cli
import json # to save and load the task form a file
import os  # to check if the file exist

TODO_FILE = "todo.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,"r") as file:
        return json.load(file)
def save_task(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
@click.group()
def cli():
    """ Simple Todo List Manager"""
    pass


@click.command()
@click.argument("task")
def add(task):
    """ Add a new task to the lsit"""
    tasks = load_tasks()
    tasks.append({"task":task,"done":False})
    save_task(tasks)
    click.echo(f"Task added successfully: {task}")



@click.command()
def list():
    """List all the tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No Tasks found")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❎"
        click.echo(f"{index}. {task["task"]} [{status}]")




@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Tasks {task_number} marked as completed.")
    else:
        click.echo(f"Invalikd task number: {task_number}")

@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove task form the list"""
    tasks = load_tasks()
    if 0 <task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1)
        save_task(tasks)
        click.echo(f"Remove task: {remove_task["task"]}")
    else:
        click.echo(f"Invalid task number")



cli.add_command(list)
cli.add_command(add)
cli.add_command(complete)
cli.add_command(remove)


if __name__ == "__main__":
    cli()

