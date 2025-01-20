#!/usr/bin/env bash

# Colored output
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

clear
echo -e "${GREEN}===================================================="
echo -e "        HiveAI System Check Script (Agents)         "
echo -e "====================================================${NC}"

# 1. Create a new agent
echo -e "${YELLOW}Step 1: Creating a new agent...${NC}"
AGENT_RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Agent A","capabilities":"Basic capability"}' \
  http://127.0.0.1:5000/agents)

echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$AGENT_RESPONSE" | jq .

AGENT_ID=$(echo "$AGENT_RESPONSE" | jq .id)
if [ "$AGENT_ID" == "null" ]; then
  echo -e "${RED}[ERROR] Failed to create agent. Exiting...${NC}"
  exit 1
fi
echo -e "${GREEN}[SUCCESS] Agent created with ID: $AGENT_ID${NC}"
sleep 2
clear

# 2. List all agents
echo -e "${YELLOW}Step 2: Listing all agents...${NC}"
AGENTS_LIST=$(curl -s -X GET http://127.0.0.1:5000/agents)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$AGENTS_LIST" | jq .
echo -e "${GREEN}[SUCCESS] Retrieved list of all agents.${NC}"
sleep 2
clear

# 3. Update the newly created agent's status
echo -e "${YELLOW}Step 3: Updating the newly created agent's status to 'active'...${NC}"
STATUS_UPDATE_RESPONSE=$(curl -s -X PUT \
  -H "Content-Type: application/json" \
  -d '{"status":"active"}' \
  http://127.0.0.1:5000/agents/$AGENT_ID/status)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$STATUS_UPDATE_RESPONSE" | jq .
echo -e "${GREEN}[SUCCESS] Agent status updated to 'active'.${NC}"
sleep 2
clear


echo -e "${GREEN}===================================================="
echo -e "   HiveAI System Check Script (Collaborations)      "
echo -e "====================================================${NC}"

# 4. Create a new collaboration
echo -e "${YELLOW}Step 4: Creating a new collaboration...${NC}"
COLLAB_RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"name":"Collab 1","description":"Test collaboration"}' \
  http://127.0.0.1:5000/multi-agent/create)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$COLLAB_RESPONSE" | jq .

COLLAB_ID=$(echo "$COLLAB_RESPONSE" | jq .id)
if [ "$COLLAB_ID" == "null" ]; then
  echo -e "${RED}[ERROR] Failed to create collaboration. Exiting...${NC}"
  exit 1
fi
echo -e "${GREEN}[SUCCESS] Collaboration created with ID: $COLLAB_ID${NC}"
sleep 2
clear

# 5. Assign the newly created agent to the collaboration
echo -e "${YELLOW}Step 5: Assigning Agent (ID=$AGENT_ID) to Collaboration (ID=$COLLAB_ID)...${NC}"
ASSIGN_RESPONSE=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d "{\"agent_ids\":[$AGENT_ID]}" \
  http://127.0.0.1:5000/multi-agent/$COLLAB_ID/assign)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$ASSIGN_RESPONSE" | jq .
echo -e "${GREEN}[SUCCESS] Agent assigned to collaboration.${NC}"
sleep 2
clear

# 6. List agents in the collaboration
echo -e "${YELLOW}Step 6: Listing agents in the collaboration...${NC}"
COLLAB_AGENTS=$(curl -s -X GET \
  http://127.0.0.1:5000/multi-agent/$COLLAB_ID/agents)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$COLLAB_AGENTS" | jq .
echo -e "${GREEN}[SUCCESS] Retrieved list of agents in the collaboration.${NC}"
sleep 2
clear

# 7. Check the collaboration progress
echo -e "${YELLOW}Step 7: Checking collaboration progress...${NC}"
PROGRESS_RESPONSE=$(curl -s -X GET \
  http://127.0.0.1:5000/multi-agent/$COLLAB_ID/progress)
echo -e "${CYAN}[INFO] Server Response:${NC}"
echo "$PROGRESS_RESPONSE" | jq .
echo -e "${GREEN}[SUCCESS] Collaboration progress checked successfully.${NC}"
sleep 2
clear

echo -e "${GREEN}===================================================="
echo -e "           HiveAI System Check Completed!           "
echo -e "====================================================${NC}"
