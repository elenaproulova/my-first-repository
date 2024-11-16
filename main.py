task_list = []
done_task_list = []

class Task():
    def __init__(self, description, deadline, status=0):
        self.description = description
        self.deadline = deadline
        self.status = status

    def add_task(self):
        if self.status == 1:
            print(f"Задача {self.description} уже выполнена, она добавится в список завершенных задач")
            done_task_list.append(self.description)
        else:
            task_list.append(self.description)
            print(f"Задача {self.description} добавлена")

    def done_task(self):
        if self.status == 0:
            self.status = 1
            task_list.remove(self.description)
            done_task_list.append(self.description)
            print(f"Задача {self.description} отмечена выполненной")
        else:
            print(f"Задача {self.description} уже выполнена")
        print(f"Список выполненных задач:{done_task_list}")

    def current_list(self):
        print(f"Список текущих задач:{task_list}")

task1 = Task(description="Купить молока", deadline="15.11")
task1.add_task()
task1.done_task()
task1.current_list()
task2 = Task(description = "Помыть полы", deadline="16.11")
task3 = Task(description = "Приготовить обед", deadline="16.11", status=1)
task2.add_task()
task3.add_task()
task3.done_task()
task3.current_list()