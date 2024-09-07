from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from leads_filo.tools.capturar_leads import captura_leads_de_ambas_contas
from leads_filo.tools.reativar_clientes import reativar_ambas_contas

@CrewBase
class LeadsFiloCrew():
    """LeadsFilo crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def lead_capturer(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_capturer'],
            verbose=True
        )

    @agent
    def customer_reactivator(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_reactivator'],
            verbose=True
        )

    @agent
    def new_customer_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['new_customer_analyst'],
            verbose=True
        )

    @agent
    def lead_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_manager'],
            verbose=True
        )

    @task
    def lead_capture_task(self) -> Task:
        return Task(
            config=self.tasks_config['lead_capture_task'],
            execute=captura_leads_de_ambas_contas,  # Função que captura os leads das duas contas
            verbose=True
        )

    @task
    def customer_reactivation_task(self) -> Task:
        return Task(
            config=self.tasks_config['customer_reactivation_task'],
            execute=reativar_ambas_contas,  # Função que reativa os clientes inativos em ambas as contas
            verbose=True
        )

    @task
    def new_customer_task(self) -> Task:
        return Task(
            config=self.tasks_config['new_customer_task'],
            # Adicione a função de captura de novos clientes se houver
            verbose=True
        )

    @task
    def daily_report_task(self) -> Task:
        return Task(
            config=self.tasks_config['daily_report_task'],
            output_file='daily_report.md',  # Exemplo de saída de um relatório diário
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the LeadsFilo crew"""
        return Crew(
            agents=self.agents,  # Agentes criados pelos decoradores @agent
            tasks=self.tasks,    # Tarefas criadas pelos decoradores @task
            process=Process.sequential,  # Processamento sequencial das tarefas
            verbose=True,
        )
