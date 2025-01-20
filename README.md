# HIVEAI 🐝 - Multi-Agent Collaboration Platform

[![PyPI version](https://badge.fury.io/py/hiveagentai.svg)](https://pypi.org/project/hiveagentai/)
[![GitHub stars](https://img.shields.io/github/stars/hiveagent/hiveagentai.svg?style=social)](https://github.com/hiveagent/hiveagentai/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/hiveagent/hiveagentai.svg)](https://github.com/hiveagent/hiveagentai/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/hiveagent/hiveagentai.svg)](https://github.com/hiveagent/hiveagentai/pulls)

---

## Table of Contents
- [Introduction](#introduction)
- [Key Features 🚀](#key-features-)
- [Platform Architecture 🏗️](#platform-architecture-)
- [🚨 Setup Instructions](#-setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Install Dependencies](#install-dependencies-)
  - [Running the API](#running-the-api-)
- [📚 Available Endpoints](#-available-endpoints)
  - [Agent Management 🤖](#agent-management-)
  - [Collaboration Management 🤝](#collaboration-management-)
  - [Agent Status and Progress 📊](#agent-status-and-progress-)
- [🛠️ Example Usage](#-example-usage)
- [🔧 Technologies Used](#-technologies-used)
- [License 📜](#license-)
- [💬 Support](#-support)

---

## Introduction

Welcome to **HIVEAI**! 🧠✨ A powerful platform designed to manage and orchestrate **multiple AI agents** working together collaboratively on complex tasks. Think of it as a **smart hive** where agents combine their intelligence to achieve shared goals! 🤖💡

With HIVEAI, you can:
- Create and manage **AI agents** 🛠️
- Launch **collaborative projects** where agents work together 🤝
- **Track progress** and monitor the status of your agents in real-time 📊

---

## Key Features 🚀
- **Agent Management**: Create AI agents with customizable capabilities 🤖  
- **Collaboration Projects**: Define projects where agents collaborate to achieve common goals 🧑‍🤝‍🧑  
- **Agent Assignment**: Assign agents to specific tasks within collaboration projects 🎯  
- **Collaboration Monitoring**: Track progress and performance of agents within each project 📈  

---

## Platform Architecture 🏗️
- **Flask**: Lightweight Python web framework for creating the API 🌐  
- **SQLAlchemy**: ORM for managing and accessing the database 🗄️  
- **SQLite**: A simple and effective local database 🛠️  

---

## 🚨 Setup Instructions

### Prerequisites:
- Python 3.10 or higher 🐍
- A virtual environment (optional but recommended) 🌱

### Install Dependencies 💻:

1. Clone this repository:
   ```bash
   git clone hhttps://github.com/hiveagent/hiveagentai.git
   cd hiveagentai
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

For issues, bugs, or suggestions, feel free to open an issue or contribute via a pull request on the [GitHub repository](https://github.com/hiveagent/hiveagentai).

Let's create smarter AI together! 🤖💡✨