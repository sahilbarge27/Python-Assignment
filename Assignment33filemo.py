import psutil
import logging

def DisplayOpenFilesInfo():
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                files = proc.open_files()
                file_count = len(files)

                logging.info(
                    f"Process Name: {proc.info['name']} | "
                    f"PID: {proc.info['pid']} | "
                    f"Open Files: {file_count}"
                )

            except psutil.AccessDenied:
                logging.warning(
                    f"Process Name: {proc.info['name']} | "
                    f"PID: {proc.info['pid']} | Access Denied"
                )

            except psutil.NoSuchProcess:
                continue

    except Exception as e:
        logging.error(f"Open File Monitoring Error: {e}")