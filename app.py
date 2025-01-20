from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hiveai.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Models
    class Agent(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        capabilities = db.Column(db.String(500), nullable=False)
        status = db.Column(db.String(50), default='idle')

        def to_dict(self):
            return {
                "id": self.id,
                "name": self.name,
                "capabilities": self.capabilities,
                "status": self.status
            }

    class Collaboration(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        description = db.Column(db.String(500), nullable=False)
        agents = db.relationship('Agent', secondary='collaboration_agents', back_populates='collaborations')

    collaboration_agents = db.Table(
        'collaboration_agents',
        db.Column('collaboration_id', db.Integer, db.ForeignKey('collaboration.id'), primary_key=True),
        db.Column('agent_id', db.Integer, db.ForeignKey('agent.id'), primary_key=True)
    )

    # Backref for Agent model
    Agent.collaborations = db.relationship(
        'Collaboration',
        secondary=collaboration_agents,
        back_populates='agents'
    )

    # Create database tables if not exist
    with app.app_context():
        db.create_all()

    @app.route('/agents', methods=['POST'])
    def create_agent():
        data = request.get_json() or {}
        app.logger.info(f"CREATE_AGENT ENDPOINT: Received data: {data}")

        name = data.get('name')
        capabilities = data.get('capabilities')

        if not name or not capabilities:
            app.logger.warning("CREATE_AGENT ENDPOINT: Name or capabilities missing.")
            return jsonify({"error": "Name and capabilities are required"}), 400

        new_agent = Agent(name=name, capabilities=capabilities)
        db.session.add(new_agent)
        db.session.commit()

        app.logger.info(f"CREATE_AGENT ENDPOINT: Created Agent with ID={new_agent.id}")
        return jsonify(new_agent.to_dict()), 201

    @app.route('/agents', methods=['GET'])
    def get_agents():
        app.logger.info("GET_AGENTS ENDPOINT: Listing all agents.")
        agents = Agent.query.all()
        app.logger.info(f"GET_AGENTS ENDPOINT: Found {len(agents)} agents.")
        return jsonify([agent.to_dict() for agent in agents]), 200

    @app.route('/agents/<int:agent_id>/status', methods=['PUT'])
    def update_agent_status(agent_id):
        app.logger.info(f"UPDATE_AGENT_STATUS ENDPOINT: Agent ID={agent_id}")
        agent = Agent.query.get_or_404(agent_id)

        data = request.get_json() or {}
        status = data.get('status')
        app.logger.info(f"UPDATE_AGENT_STATUS ENDPOINT: Requested status update to: {status}")

        valid_statuses = ['idle', 'active', 'error']
        if status not in valid_statuses:
            app.logger.warning(f"UPDATE_AGENT_STATUS ENDPOINT: Invalid status {status}.")
            return jsonify({"error": f"Invalid status. Use one of {valid_statuses}"}), 400

        agent.status = status
        db.session.commit()

        app.logger.info(f"UPDATE_AGENT_STATUS ENDPOINT: Updated status of Agent ID={agent.id} to {agent.status}")
        return jsonify(agent.to_dict()), 200

    @app.route('/multi-agent/create', methods=['POST'])
    def create_collaboration():
        data = request.get_json() or {}
        app.logger.info(f"CREATE_COLLABORATION ENDPOINT: Received data: {data}")

        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            app.logger.warning("CREATE_COLLABORATION ENDPOINT: Name or description missing.")
            return jsonify({"error": "Name and description are required"}), 400

        new_collaboration = Collaboration(name=name, description=description)
        db.session.add(new_collaboration)
        db.session.commit()

        app.logger.info(f"CREATE_COLLABORATION ENDPOINT: Created Collaboration with ID={new_collaboration.id}")
        return jsonify({
            "id": new_collaboration.id,
            "name": new_collaboration.name,
            "description": new_collaboration.description
        }), 201

    @app.route('/multi-agent/<int:collaboration_id>/assign', methods=['POST'])
    def assign_agents(collaboration_id):
        app.logger.info(f"ASSIGN_AGENTS ENDPOINT: Collaboration ID={collaboration_id}")
        collaboration = Collaboration.query.get_or_404(collaboration_id)

        data = request.get_json() or {}
        agent_ids = data.get('agent_ids')

        if not agent_ids:
            app.logger.warning("ASSIGN_AGENTS ENDPOINT: agent_ids is missing or empty.")
            return jsonify({"error": "Agent IDs are required"}), 400

        agents = Agent.query.filter(Agent.id.in_(agent_ids)).all()
        for agent in agents:
            collaboration.agents.append(agent)

        db.session.commit()
        app.logger.info(
            f"ASSIGN_AGENTS ENDPOINT: Assigned {len(agents)} agent(s) to Collaboration ID={collaboration.id}")
        return jsonify({
            "message": f"Assigned {len(agents)} agents to collaboration '{collaboration.name}'"
        }), 200

    @app.route('/multi-agent/<int:collaboration_id>/agents', methods=['GET'])
    def view_agents_in_collaboration(collaboration_id):
        app.logger.info(f"VIEW_AGENTS_IN_COLLAB ENDPOINT: Collaboration ID={collaboration_id}")
        collaboration = Collaboration.query.get_or_404(collaboration_id)
        agent_list = [agent.to_dict() for agent in collaboration.agents]
        app.logger.info(
            f"VIEW_AGENTS_IN_COLLAB ENDPOINT: {len(agent_list)} agent(s) found in Collaboration ID={collaboration_id}")
        return jsonify(agent_list), 200

    @app.route('/multi-agent/<int:collaboration_id>/progress', methods=['GET'])
    def get_collaboration_progress(collaboration_id):
        app.logger.info(f"GET_COLLABORATION_PROGRESS ENDPOINT: Collaboration ID={collaboration_id}")
        collaboration = Collaboration.query.get_or_404(collaboration_id)
        agents_info = [
            {"agent_id": agent.id, "name": agent.name, "status": agent.status}
            for agent in collaboration.agents
        ]
        app.logger.info(f"GET_COLLABORATION_PROGRESS ENDPOINT: Returning progress for {len(agents_info)} agents.")
        return jsonify({
            "collaboration_id": collaboration.id,
            "agents_progress": agents_info
        }), 200

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True)
