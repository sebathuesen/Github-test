import sys
import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append('[ ] ' + task)
    save_tasks(tasks)
    print(f'Added: {task}')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
        return
    for idx, task in enumerate(tasks, 1):
        print(f'{idx}. {task}')

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        if tasks[index-1].startswith('[ ]'):
            tasks[index-1] = tasks[index-1].replace('[ ]', '[x]', 1)
            save_tasks(tasks)
            print(f'Task {index} marked as done.')
        else:
            print('Task already marked as done.')
    else:
        print('Invalid task number.')

def main():
    if len(sys.argv) < 2:
        print('Usage: python todo.py [add|list|done] ...')
        return
    cmd = sys.argv[1]
    if cmd == 'add' and len(sys.argv) > 2:
        add_task(' '.join(sys.argv[2:]))
    elif cmd == 'list':
        list_tasks()
    elif cmd == 'done' and len(sys.argv) == 3 and sys.argv[2].isdigit():
        mark_done(int(sys.argv[2]))
    else:
        print('Invalid command or arguments.')

if __name__ == '__main__':
    main() 