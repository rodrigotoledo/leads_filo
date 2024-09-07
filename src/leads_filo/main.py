from leads_filo.crew import LeadsFiloCrew

def main():
    # Inicializa a crew e executa as tarefas sequenciais
    crew = LeadsFiloCrew()
    
    # Executa a crew configurada no crew.py
    crew.crew().run()

if __name__ == "__main__":
    main()
