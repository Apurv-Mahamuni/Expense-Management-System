# 🚀 **Expense Management System**

This project is an **Expense Management System** that integrates a **Streamlit frontend** application and a **FastAPI backend** server to allow users to track and manage their expenses seamlessly.

---

## 🌟 **Features**

- **Streamlit Frontend**: An interactive, user-friendly web interface to view and manage your expenses.
- **FastAPI Backend**: A high-performance API server for handling the business logic and database interactions.
- **Database Support**: The system interacts with a database to store expense data.

---

## 📂 **Project Structure**

PROJECT_EXPENSE_TRACKER/
├── backend/                # FastAPI backend code
│   ├── Db_Helper.py       # Helper functions for database interactions
│   ├── logging_setup.py   # Logging configuration for the backend
│   └── server.py          # FastAPI server setup
├── frontend/               # Streamlit frontend code
│   ├── add_update_ui.py    # UI for adding/updating expenses
│   ├── analytics_month.py # Monthly expense analytics
│   ├── analytics_ui.py    # UI for displaying analytics
│   └── app.py             # Main Streamlit app
├── tests/                  # Test cases for frontend and backend
│   ├── backend/           # Backend tests
│   └── frontend/          # Frontend tests
├── requirements.txt        # Required Python packages for the project
├── README.md               # Project overview and setup instructions

---

## 🔧 **Setup Instructions**

### 1️⃣ **Clone the repository**

First, clone the repository to your local machine and navigate into the project directory:

```bash
git clone https://github.com/yourusername/expense-management-system.git
cd expense-management-system 
```

### 2️⃣ **Install dependencies**

Install the required Python packages for both the frontend and backend:

```bash
pip install -r requirements.txt
```

### 3️⃣ **Run the FastAPI server**

Start the FastAPI server. The --reload flag ensures the server automatically restarts during development:

```bash
uvicorn server.server:app --reload
```
The API server will now be running on http://localhost:8000.

### 4️⃣ **Run the Streamlit app**   
   
Start the Streamlit app. This will launch the user interface in your browser:

```bash
streamlit run frontend/app.py
```

The frontend will be available at http://localhost:8501.

---

## 🛠 **Technologies Used**

• Frontend: Streamlit

• Backend: FastAPI, Pydantic

• Database: MySQL

• Testing: Pytest

---