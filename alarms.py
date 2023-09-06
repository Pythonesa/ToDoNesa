import threading
import time
from datetime import datetime
from plyer import notification

def check_alarms(tasks):
    while True:
        current_time = datetime.now().strftime('%H:%M')
        current_date = datetime.now().strftime('%d/%m/%Y')
        
        for task_name, task_details in tasks.items():
            if 'alarm_date' in task_details and 'alarm_hour' in task_details:
                if task_details['alarm_date'] == current_date and task_details['alarm_hour'] == current_time:
                    notification.notify(
                        title='Recordatorio de Tarea',
                        message=f'¡Es hora de la tarea {task_name}!',
                        app_icon=None,
                        timeout=10,
                    )
        time.sleep(60)
        
        
