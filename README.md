# MARKY 🗒️
### CLI Task Tracker

A simple, efficient Command-Line Interface (CLI) application to manage your daily tasks. Built in Python, this tool allows you to add, update, delete, and track the status of your tasks directly from your terminal. 

Task data is persistently saved to a local JSON file `data.json` and tasks are displayed in clean, highly readable tabular format.

## 🚀 Features

* **CRUD Operations:** Add, update, and delete your tasks effortlessly.
* **Status Tracking:** Mark tasks as `todo`, `in-progress`, or `done`.
* **Smart Listing:** View all tasks at once, or filter them by their current status.
* **Persistent Storage:** Tasks are automatically saved to a `data.json` file in the same directory, ensuring you never lose your data between sessions.
* **Dynamic IDs:** Automatically calculates and assigns the next available ID when a new task is created.
* **Beautiful UI:** Uses the `tabulate` module to render tasks in clean, formatted terminal tables.

## 🛠️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/patra-rahul/marky.git
cd marky
```
**2. Install Dependencies**
```bash
# for mac users:
pip3 install -r requirements.txt
# for windows users:
pip install -r requirements.txt
```

**3. Run the application in terminal**
```bash
# for mac users:
python3 marky.py --help
# for windows users:
python marky.py --help
```

## 💻 Usage
1. To add a new task
```bash
python3 marky.py add "write your task here"
```
2. To delete a task
```bash
python3 marky.py delete id
```
3. To update a task
```bash
python3 marky.py update id "write your updated task here"
```
4. To change the status of a task `default status: todo`
```bash
# mark-in-progress
python3 marky.py mark-in-progress id
# mark-done
python3 marky.py mark-done id
```
## Listing all tasks in tabular format
```bash
# list all together
python3 marky.py list
# list only todo tasks
python3 marky.py list todo
# list only in-progress tasks
python3 marky.py list in-progress
#list only done tasks
python3 marky.py list done
```
##

Building this CLI tracker was a fantastic exercise in mastering terminal interactions. It was my first ever complete project done without any tutorials, figuring things out googling and reading documentations. If you find this project helpful, or if you have suggestions for new features, feel free to open an issue or submit a pull request. 

Thanks for checking it out! ❤️
