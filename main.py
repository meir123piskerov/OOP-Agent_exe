from Agent_class import Agent
from Mission_class import Mission
from Report import Report
from MissionControl import MissionControl

mission = Mission("to run","Netanya")
mission.assign(Agent("Meir", 3))
mission.brief()
agent = Agent("chaim",5)




re = Report("sudan",5,agent.code_name)
MissionControl.analyze_report(re)

