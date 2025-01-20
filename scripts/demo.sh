#!/usr/bin/env bash

# Colored output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting system check...${NC}"

# 1. Create a new agent
echo -e "${YELLOW}Creating a new agent...${NC}"
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Agent A","capabilities":"Basic capability"}' \
  http://127.0.0.1:5000/agents \
  | jq .

# 2. List all agents
echo -e "${YELLOW}Listing all agents...${NC}"
curl -s -X GET http://127.0.0.1:5000/agents | jq .

# 3. Create a new collaboration
echo -e "${YELLOW}Creating a new collaboration...${NC}"
COLLAB_RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Collab 1","description":"Test collaboration"}' \
  http://127.0.0.1:5000/multi-agent/create)
echo $COLLAB_RESPONSE | jq .

COLLAB_ID=$(echo $COLLAB_RESPONSE | jq .id)

# 4. Assign the agent to the new collaboration
echo -e "${YELLOW}Assigning the newly created agent to the collaboration...${NC}"
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"agent_ids":[1]}' \
  http://127.0.0.1:5000/multi-agent/$COLLAB_ID/assign | jq .

# 5. Check the collaboration progress
echo -e "${YELLOW}Checking collaboration progress...${NC}"
curl -s -X GET \
  http://127.0.0.1:5000/multi-agent/$COLLAB_ID/progress | jq .

echo -e "${GREEN}System check completed!${NC}"
