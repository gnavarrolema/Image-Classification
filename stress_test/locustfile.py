from locust import HttpUser, between, task
import json


class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    @task
    def index(self):
        self.client.get("http://localhost/")

    @task
    def predict(self):
        files = [("file", ("dog.jpeg", open("dog.jpeg", "rb"), "image/jpeg"))]
        headers = {}
        payload = {}
        self.client.post(
            "http://localhost/predict", headers=headers, data=payload, files=files
        )

    @task
    def feedback(self):
        headers = {"Content-Type": "application/json"}
        payload = {"prediction": "Eskimo_dog", "score": 0.9346}
        self.client.post(
            "http://localhost/feedback", headers=headers, data=json.dumps(payload)
        )


# Commands:
# locust -f locustfile.py -H http://localhost/
# docker-compose up --build --scale model=2 -d
