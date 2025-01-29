AutoTask AI ⚡


An intelligent and easy-to-use task management system using AI for task classification, task tracking, and productivity visualization. Built with Python, Streamlit, AI, and SQLite.

Overview
Welcome to the AutoTask AI! This application helps you manage tasks efficiently by adding them, tracking their status, clearing completed tasks, and using AI for task classification. It uses a combination of Python, Streamlit, and AI-powered classification for a seamless experience. It also saves your tasks in a database using SQLite for persistence.

Features
Task Management: Add, delete, and mark tasks as completed
AI Task Classification: Automatically classify tasks as "Work", "Personal", "Urgent", etc.
Task Filtering: Filter tasks by status (Pending, Completed, or All)
Progress Tracking: See the percentage of completed tasks with a progress bar
Data Visualization: View a pie chart showing the distribution of task statuses (Pending vs. Completed)
Database Storage: Tasks are saved and retrieved from an SQLite database for persistence


Installation
Clone the repository
Open your terminal/command prompt and run the following:
bash
Copy
Edit
git clone https://github.com/your-username/to-do-list-ai.git
cd to-do-list-ai
Install required dependencies
Use pip to install the necessary libraries:

bash
Copy
Edit
pip install streamlit pandas matplotlib transformers sqlite3



Usage

Add a Task
To add a task to the list:
Enter a task description (e.g., "Complete Python Course").
Select a priority level (High, Medium, Low).
Click "Add Task" to add it to the list.
Example:
Task Description: "Complete Python Course"
Priority: High
View and Manage Tasks
You can manage your tasks by:

Viewing tasks in the list.
Marking a task as Done by clicking the "Mark as Done" button.
Delete tasks by clicking the "Delete" button.
Example:
Task: "Complete Python Course" (Pending)
Click "Mark as Done" for this task to mark it as completed.
Clear Completed Tasks
To clear all completed tasks from the list:

Click "Clear Completed".
Example:
If you have the following tasks:

"Complete Python Course" (Done)
"Buy Groceries" (Pending)
After clicking "Clear Completed", the "Complete Python Course" task will be removed from the list.

Progress Bar & Task Distribution
A progress bar will show the percentage of tasks marked as "Done".
A pie chart will show the distribution of tasks: Pending vs. Completed.
Example:
If you have 4 tasks:

2 tasks completed and 2 pending, the pie chart will show a 50% completion rate.
AI Task Classification
Enter a task description in the input field.
Click "Classify Task" to automatically classify the task.
Example:
Task Description: "Prepare for AI Certification Exam"
AI Classification Result: Learning
Contributing
We welcome contributions to improve this project. If you have any suggestions, issues, or ideas for improvement, feel free to:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to your fork (git push origin feature-branch).
Open a pull request.


