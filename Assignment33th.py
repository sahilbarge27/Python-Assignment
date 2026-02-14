import psutil
import logging

def DisplayThreadInfo():
    try:
        for proc in psutil.process_iter(['pid', 'name', 'num_threads']):
            try:
                logging.info(
                    f"Process Name: {proc.info['name']} | "
                    f"PID: {proc.info['pid']} | "
                    f"Thread Count: {proc.info['num_threads']}"
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    except Exception as e:
        logging.error(f"Thread Monitoring Error: {e}")