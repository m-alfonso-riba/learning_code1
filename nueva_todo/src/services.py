from models import Task
from db import insert_task, show_the_list, mark_done
import logging


def create_task(text):
    logging.info("creando tarea")
    insert_task(text)


def show_list():
    rows = show_the_list()
    return [Task(*row) for row in rows]


def mark_as_done(task_id):
    logging.info("marcando tarea como realizada")
    mark_done(task_id)
