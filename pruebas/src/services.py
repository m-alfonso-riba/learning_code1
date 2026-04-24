from db import add_task,show_list,mark_done
from schemas import Task
import logging

def create_task(text):
    logging.info("Tare creada con exito!")
    add_task(text)

def show_the_list():
    rows = show_list()
    return [Task(*row) for row in rows]

def mark_as_done(task_id):
    logging.info("Tarea completada!")
    mark_done(task_id)
