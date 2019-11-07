from locust import HttpLocust, Locust, TaskSet, task
from links.links import *
import random

class UserBehavior(TaskSet):
  link = "/"

  def on_start(self):
            if len(LINKS) > 0:
                self.link = random.choice(LINKS)

  @task(1)
  def my_task(self):
      self.client.get(self.link)

class WebsiteUser(HttpLocust):
  task_set = UserBehavior
  min_wait = 20000
  max_wait = 30000

