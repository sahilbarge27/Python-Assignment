import logging

def ConfigureLogger(logfile):
    try:
        logging.basicConfig(
            filename=logfile,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    except Exception as e:
        print("Logger configuration failed:", e)