from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up SQLite database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hiveai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Agent Model
class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capabilities = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(50), default='idle')

# Define Collaboration Model
class Collaboration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    agents = db.relationship('Agent', secondary='collaboration_agents', back_populates='collaborations')

# Association table for many-to-many relationship between Collaboration and Agent
collaboration_agents = db.Table('collaboration_agents',
    db.Column('collaboration_id', db.Integer, db.ForeignKey('collaboration.id'), primary_key=True),
    db.Column('agent_id', db.Integer, db.ForeignKey('agent.id'), primary_key=True)
)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/agents', methods=['POST'])
def create_agent():
    data = request.get_json()
    name = data.get('name')
    capabilities = data.get('capabilities')

    if not name or not capabilities:
        return jsonify({"error": "Name and capabilities are required"}), 400

    new_agent = Agent(name=name, capabilities=capabilities)
    db.session.add(new_agent)
    db.session.commit()
    
    return jsonify({"id": new_agent.id, "name": new_agent.name, "capabilities": new_agent.capabilities}), 201

@app.route('/agents', methods=['GET'])
def get_agents():
    agents = Agent.query.all()
    agents_list = [{"id": agent.id, "name": agent.name, "capabilities": agent.capabilities} for agent in agents]
    return jsonify(agents_list)

@app.route('/multi-agent/create', methods=['POST'])
def create_collaboration():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name or not description:
        return jsonify({"error": "Name and description are required"}), 400

    new_collaboration = Collaboration(name=name, description=description)
    db.session.add(new_collaboration)
    db.session.commit()

    return jsonify({"id": new_collaboration.id, "name": new_collaboration.name, "description": new_collaboration.description}), 201

@app.route('/multi-agent/<int:collaboration_id>/assign', methods=['POST'])
def assign_agents(collaboration_id):
    collaboration = Collaboration.query.get_or_404(collaboration_id)
    data = request.get_json()
    agent_ids = data.get('agent_ids')

    if not agent_ids:
        return jsonify({"error": "Agent IDs are required"}), 400

    agents = Agent.query.filter(Agent.id.in_(agent_ids)).all()
    for agent in agents:
        collaboration.agents.append(agent)

    db.session.commit()
    
    return jsonify({"message": f"Assigned {len(agents)} agents to collaboration '{collaboration.name}'"}), 200

@app.route('/multi-agent/<int:collaboration_id>/agents', methods=['GET'])
def view_agents_in_collaboration(collaboration_id):
    collaboration = Collaboration.query.get_or_404(collaboration_id)
    agents_list = [{"id": agent.id, "name": agent.name, "capabilities": agent.capabilities} for agent in collaboration.agents]
    return jsonify(agents_list)

@app.route('/agents/<int:agent_id>/status', methods=['PUT'])
def update_agent_status(agent_id):
    agent = Agent.query.get_or_404(agent_id)
    data = request.get_json()
    status = data.get('status')

    if status not in ['idle', 'active', 'error']:
        return jsonify({"error": "Invalid status"}), 400

    agent.status = status
    db.session.commit()

    return jsonify({"id": agent.id, "name": agent.name, "status": agent.status})

@app.route('/multi-agent/<int:collaboration_id>/progress', methods=['GET'])
def get_collaboration_progress(collaboration_id):
    collaboration = Collaboration.query.get_or_404(collaboration_id)
    agents = collaboration.agents
    progress = []

    for agent in agents:
        progress.append({
            "agent_id": agent.id,
            "name": agent.name,
            "status": agent.status
        })

    return jsonify({"collaboration_id": collaboration.id, "agents_progress": progress})

if __name__ == '__main__':
    app.run(debug=True)
