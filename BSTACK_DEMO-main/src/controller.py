import os
from session_handler import execute_locally, execute_remotely
from test_steps import run_session
import json
from threading import Thread

os.environ["PYTHONIOENCODING"] = "utf-8"
username = os.getenv('BROWSERSTACK_USERNAME')
access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
test_env = os.getenv('TEST_ENV')

if test_env=='local':
    try:
        driver = execute_locally()
    except:
        print('Error! Executing execute_locally()')
    
    try:
        run_session(driver)
        
    except:
        print('Error! In Local Session')
else:
    drivers = []
    try:
        conf = open('config.json')
    except:
        print('Error! Cannot Open config.json')
    else:
        des_caps = json.load(conf)
        for cap in des_caps['capabilities']:
            _driver=execute_remotely(username, access_key, cap)
            drivers.append(_driver)
        for driver in drivers:
            Thread(target=run_session, args=(driver,)).start()
    finally:
        conf.close()
