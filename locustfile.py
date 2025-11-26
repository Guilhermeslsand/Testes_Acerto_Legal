import json
import random
import gevent
from locust import HttpUser, task, between


with open("tokens.json") as f:
    TOKENS = json.load(f)

class ChatApiUser(HttpUser):
    wait_time = between(10, 15)  # intervalo entre requisições

    def on_start(self):
        self.user = random.choice(TOKENS)
        self.token = self.user["accessToken"]
        self.client.headers.update({"Authorization": f"Bearer {self.token}"})

    @task
    def criar_thread(self):
        self.client.post("/rag-chat/create-thread-v2")

    # def consultar_historico(self):
    #     self.client.get("/rag-chat/historico/v2", params={"thread_id": "thread_25f587fbd0a1_1764077429"})

    # @task
    # def estatisticas_sessao(self):
    #     self.client.get("/rag-chat/session/stats")
