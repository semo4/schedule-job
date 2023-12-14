
import schedule
import requests
import time
from datetime import datetime


def main():
    print('Start Build Premium Articles')
    call_num = 0
    url = 'http://localhost:3000/build-premium-articles'
    headers = {'Authorization': 'Bearer your token'}
    res = requests.post(url, headers=headers)
    print(res)
    if res.status_code == 200:
        print("Job finished successfully")
    else:
        print("Job falied")
    call_num += 1
    print(f'finihed Build Premium Articles, With Call Number {call_num}')


if __name__ == '__main__':
    print(
        f'Start Schedule To Build Premium Articles, Start at {datetime.now()}')
    schedule.every(5).minutes.do(main)
    print('Finihed Schedule Build Premium Articles')
    while True:
        schedule.run_pending()
        time.sleep(1)
