"""
    RED HERRING!!!!
    naming this file schedule.py clashed with the schedule module!!! 
    
    REMEMBER!!!!
"""

### pip3 install schedule

import schedule, time

def job():
    print('Do some job - send bulk emails etc.')

schedule.every(1).minutes.do(job) ### runs things in the background!!
schedule.every().hour.do(job)
schedule.every().day.at("12:00").do(job)

if __name__ == '__main__':
    while 1:
        schedule.run_pending()
        print('Doing some background work')
        time.sleep(1)