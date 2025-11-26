from locust import HttpUser, task, between

class ChatApiUser(HttpUser):
    wait_time = between(1, 3)  # intervalo entre requisições

    @task
    def criar_thread(self):
        self.client.post("/rag-chat/create-thread-v2")

    @task
    def consultar_historico(self):
        self.client.get("/rag-chat/historico/v2", params={"thread_id": "thread_25f587fbd0a1_1764077429"})

    @task
    def estatisticas_sessao(self):
        self.client.get("/rag-chat/session/stats")
