import time
import logging
from utils import get_failed_logins

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")

def detect_brute_force():
    """Monitor failed login attempts and detect brute-force attacks."""
    logging.info("Brute Force Detection System Started...")
    
    while True:
        failed_attempts = get_failed_logins()
        
        if failed_attempts:
            logging.warning(f"Detected {len(failed_attempts)} failed login attempts!")
            for attempt in failed_attempts:
                logging.info(attempt)

        time.sleep(60)  # Check logs every minute

if __name__ == "__main__":
    detect_brute_force()
