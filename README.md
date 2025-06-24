# 📝 Task Manager API

A simple, lightweight **Task Manager backend API** built with **FastAPI** for freelancers and developers who need to track their tasks efficiently. This API supports full **CRUD operations** and includes data validation for task status and priority.

---

## 🚀 Live Demo

Test the live API using Swagger UI here:  
🔗 [https://task-manager-api-lovat.vercel.app/docs](https://task-manager-api-lovat.vercel.app/docs)

---

## 📦 Features

- ✅ Create, Read, Update, and Delete tasks
- 🧠 Validation for `status` and `priority` using Enums
- ⚙️ Auto-incremented `id` for each task
- 📄 Built-in Swagger UI documentation
- 🌐 Deployed to the cloud using Vercel
- 💻 Fully tested locally and in production

---

## 🧠 Tech Stack

- **FastAPI** (Python web framework)
- **Pydantic** (data validation)
- **Uvicorn** (ASGI server)
- **Enum** (for status/priority validation)
- **Vercel** (for deployment)
- **Git & GitHub** (version control)

---

## 🛠️ Installation & Running Locally

### 1. Clone the repository

git clone https://github.com/your-username/task-manager-api.git
cd task-manager-api

### 2. Create a virtual environment

### 3. Install dependencies
pip install -r requirements.txt
### 4. Start the FastAPI server
uvicorn main:app --reload

### 5. Open Swagger UI in your browser
Visit:
http://localhost:8000/docs

## 🧪 Example API Usage
#### ✅ Create a Task (POST /tasks)

{
  "title": "Build FastAPI app",
  "description": "Finish backend code",
  "status": "in_progress",
  "priority": "high"
}
#### 📥 Get All Tasks (GET /tasks)
No request body needed.

#### 🛠️ Update a Task (PUT /tasks/1)

{
  "title": "Update FastAPI app",
  "description": "Refactor endpoints",
  "status": "completed",
  "priority": "medium"
}
#### ❌ Delete a Task (DELETE /tasks/1)
No request body needed.

#### ✅ Accepted Values for Validation
Status Options:

"pending"

"in_progress"

"completed"

Priority Options:

"low"

"medium"

"high"
