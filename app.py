import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from transformers import pipeline

# Database setup
DB_FILE = "tasks.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def load_tasks():
    conn = sqlite3.connect(DB_FILE)
    tasks = pd.read_sql("SELECT * FROM tasks", conn)
    conn.close()
    return tasks

def save_task(task, priority, status="Pending"):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, priority, status) VALUES (?, ?, ?)", (task, priority, status))
    conn.commit()
    conn.close()

def update_task_status(task_id, status):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Load tasks
tasks = load_tasks()

# Initialize AI model for task classification
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Streamlit UI
st.title(" AutoTask AI ⚡")
st.write("Easily manage your tasks with priority levels and AI-powered classification!")

# Add a new task
st.header("➕ Add a Task")
task = st.text_input("Task Description")
priority = st.selectbox("Priority", ["High", "Medium", "Low"])

if st.button("Add Task"):
    if task.strip():
        save_task(task, priority)
        st.success(f"Task added: {task}")
        st.rerun()  # Refresh the app
    else:
        st.warning("Task description cannot be empty.")

# Task Filters
st.header("📌 View Tasks")
filter_option = st.radio("Filter by Status", ["All", "Pending", "Completed"])

if not tasks.empty:
    if filter_option != "All":
        tasks = tasks[tasks["status"] == filter_option]

    for index, row in tasks.iterrows():
        col1, col2, col3 = st.columns([5, 2, 2])
        with col1:
            st.write(f"📌 {row['task']} ({row['priority']}) - {row['status']}")
        with col2:
            if row["status"] == "Pending" and st.button("✅ Mark as Done", key=f"done-{row['id']}"):
                update_task_status(row["id"], "Completed")
                st.rerun()
        with col3:
            if st.button("❌ Delete", key=f"delete-{row['id']}"):
                delete_task(row["id"])
                st.rerun()
else:
    st.write("No tasks available. Add one above!")

# Clear completed tasks
st.header("🗑️ Clear Completed Tasks")
if st.button("Clear Completed"):
    if "Completed" in tasks["status"].values:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE status = 'Completed'")
        conn.commit()
        conn.close()
        st.success("Completed tasks cleared.")
        st.rerun()
    else:
        st.info("No completed tasks to clear.")

# Task Progress Bar
st.header("📊 Task Progress")
if not tasks.empty:
    total_tasks = len(tasks)
    completed_tasks = len(tasks[tasks["status"] == "Completed"])
    progress = completed_tasks / total_tasks if total_tasks > 0 else 0
    st.progress(progress)
    st.write(f"✅ {completed_tasks} / {total_tasks} tasks completed")
else:
    st.write("No tasks available.")

# Task Status Pie Chart
st.header("📈 Task Status Distribution")
if not tasks.empty:
    task_status_counts = tasks["status"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(task_status_counts, labels=task_status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
else:
    st.write("No tasks to visualize.")

# AI-Based Task Classification
st.header("🤖 AI Task Classification")
task_description = st.text_input("Enter Task Description for Classification")

if st.button("Classify Task"):
    candidate_labels = ["Work", "Personal", "Urgent", "Learning", "Health"]
    if task_description.strip():
        result = classifier(task_description, candidate_labels)
        st.write(f"🔍 AI Classification: **{result['labels'][0]}**")
    else:
        st.warning("Please enter a task description to classify.")

# Cache function for performance
@st.cache_data
def get_task_list():
    return load_tasks()

