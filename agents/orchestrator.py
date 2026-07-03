from agents.knowledge_agent import KnowledgeAgent
from agents.civilization_agent import CivilizationAgent
from agents.science_agent import ScienceAgent
from agents.evidence_agent import EvidenceAgent
from agents.application_agent import ApplicationAgent
from agents.report_agent import ReportAgent


class SHRUSETVAOrchestrator:

    def __init__(self):

        self.knowledge = KnowledgeAgent()
        self.civilization = CivilizationAgent()
        self.science = ScienceAgent()
        self.evidence = EvidenceAgent()
        self.application = ApplicationAgent()
        self.report = ReportAgent()

    def run(self, query):

        knowledge = self.knowledge.process(query)

        civilization = self.civilization.process(query)

        science = self.science.process(query)

        evidence = self.evidence.process(query)

        application = self.application.process(query)

        final_report = self.report.process(
            knowledge,
            civilization,
            science,
            evidence,
            application
        )

        return final_report