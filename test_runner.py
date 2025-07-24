import os
import traceback
from tests import test_login
from ai_suggester import suggest_fixes
from utils.self_healing import heal_selectors

LOG_FILE = "logs/test_log.txt"

def run_tests():
    try:
        test_login.test_valid_login()
    except Exception as e:
        log_error(str(e))
        suggest_fixes(LOG_FILE)
        heal_selectors()
        print("Re-running tests after healing...")
        try:
            test_login.test_valid_login()
        except Exception as e:
            print("Tests failed again. Manual intervention needed.")
            log_error("Second attempt failed: " + str(e))

def log_error(error_msg):
    with open(LOG_FILE, "a") as log:
        log.write(error_msg + "\n")
