import os
from typing import List, Dict, Any
from loguru import logger

class BaseAgent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        logger.info(f"Agent {self.name} initialized as {self.role}")

    def execute(self, task: str) -> str:
        logger.info(f"Agent {self.name} executing task: {task}")
        # Placeholder for actual LLM call logic
        return f"Result from {self.name}: Task '{task}' completed successfully."

class TaskOrchestrator:
    def __init__(self):
        self.agents: Dict[str, BaseAgent] = {}
        logger.info("Task Orchestrator initialized")

    def register_agent(self, agent: BaseAgent):
        self.agents[agent.name] = agent
        logger.info(f"Registered agent: {agent.name}")

    def run_workflow(self, workflow_tasks: List[Dict[str, str]]) -> List[str]:
        results = []
        for task_info in workflow_tasks:
            agent_name = task_info.get("agent")
            task_desc = task_info.get("description")
            
            if agent_name in self.agents:
                result = self.agents[agent_name].execute(task_desc)
                results.append(result)
            else:
                logger.error(f"Agent {agent_name} not found!")
        
        return results

if __name__ == "__main__":
    # Example Usage
    orchestrator = TaskOrchestrator()
    
    researcher = BaseAgent("ResearchBot", "Data Analyst")
    writer = BaseAgent("WriteBot", "Content Creator")
    
    orchestrator.register_agent(researcher)
    orchestrator.register_agent(writer)
    
    tasks = [
        {"agent": "ResearchBot", "description": "Analyze market trends for GenAI"},
        {"agent": "WriteBot", "description": "Summarize the analysis into a blog post"}
    ]
    
    workflow_results = orchestrator.run_workflow(tasks)
    for res in workflow_results:
        print(res)