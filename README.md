# HIVEAI 🐝 - Multi-Agent Collaboration Platform

Welcome to **HIVEAI**! 🧠✨ A powerful platform designed to manage and orchestrate **multiple AI agents** working together collaboratively on complex tasks. Think of it as a **smart hive** where agents combine their intelligence to achieve shared goals! 🤖💡

With HIVEAI, you can:
- Create and manage **AI agents** 🛠️
- Launch **collaborative projects** where agents work together 🤝
- **Track progress** and monitor the status of your agents in real-time 📊

---

## Key Features 🚀:
- **Agent Management**: Create AI agents with customizable capabilities 🤖
- **Collaboration Projects**: Define projects where agents collaborate to achieve common goals 🧑‍🤝‍🧑
- **Agent Assignment**: Assign agents to specific tasks within collaboration projects 🎯
- **Collaboration Monitoring**: Track progress and performance of agents within each project 📈

## Platform Architecture 🏗️:
- **Flask**: Lightweight Python web framework for creating the API 🌐
- **SQLAlchemy**: ORM for managing and accessing the database 🗄️
- **SQLite**: A simple and effective local database 🛠️

---

## 🚨 Setup Instructions

### Prerequisites:
- Python 3.7 or higher 🐍
- A virtual environment (optional but recommended) 🌱

### Install Dependencies 💻:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/HIVEAI.git
   cd HIVEAI
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the API 🔥

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. The API will be running locally on: [http://127.0.0.1:5000/](http://127.0.0.1:5000/) 🌍

---

## 📚 Available Endpoints

### **Agent Management** 🤖

- **Create an Agent**: `POST /agents`
  - Create a new AI agent with a name and capabilities.
  - Example:
  ```json
  {
    "name": "Agent A",
    "capabilities": "Data Analysis, Machine Learning"
  }
  ```

- **List all Agents**: `GET /agents`
  - Retrieve a list of all created agents.

### **Collaboration Management** 🤝

- **Create a Collaboration**: `POST /multi-agent/create`
  - Create a new collaboration project where agents can join and work together.
  - Example:
  ```json
  {
    "name": "Project Alpha",
    "description": "Data analysis and machine learning collaboration."
  }
  ```

- **Assign Agents to a Collaboration**: `POST /multi-agent/<collaboration_id>/assign`
  - Assign agents to a specific collaboration project.
  - Example:
  ```json
  {
    "agent_ids": [1, 2]
  }
  ```

- **View Assigned Agents**: `GET /multi-agent/<collaboration_id>/agents`
  - Get a list of agents assigned to a specific collaboration.

### **Agent Status and Progress** 📊

- **Update Agent Status**: `PUT /agents/<agent_id>/status`
  - Update an agent's current status (e.g., idle, active, error).
  - Example:
  ```json
  {
    "status": "active"
  }
  ```

- **Get Collaboration Progress**: `GET /multi-agent/<collaboration_id>/progress`
  - Retrieve the progress and status of all agents within a collaboration.

---

## 🛠️ Example Usage

1. **Create an Agent**:
   ```bash
   curl -X POST http://127.0.0.1:5000/agents -H "Content-Type: application/json" -d '{"name": "Agent A", "capabilities": "Data Processing, Image Recognition"}'
   ```

2. **Create a Collaboration**:
   ```bash
   curl -X POST http://127.0.0.1:5000/multi-agent/create -H "Content-Type: application/json" -d '{"name": "Project Omega", "description": "Collaboration on data analysis."}'
   ```

3. **Assign Agents to Collaboration**:
   ```bash
   curl -X POST http://127.0.0.1:5000/multi-agent/1/assign -H "Content-Type: application/json" -d '{"agent_ids": [1, 2]}'
   ```

4. **Check Collaboration Progress**:
   ```bash
   curl http://127.0.0.1:5000/multi-agent/1/progress
   ```

---

## 🔧 Technologies Used:
- **Flask**: Lightweight Python web framework for building APIs 🌍
- **Flask-SQLAlchemy**: ORM to easily manage database records 📄
- **SQLite**: Lightweight database for persistent storage 🗄️
- **Python 3.7+**: The programming language powering the backend 🐍

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 💬 Support

For issues, bugs, or suggestions, feel free to open an issue or contribute via a pull request on the [GitHub repository](https://github.com/hiveagent/HIVEAI).

Let's create smarter AI together! 🤖💡✨
```
