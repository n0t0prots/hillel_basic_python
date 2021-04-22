import time


def countdown(func):
    def timer_of_task():
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        func()
    return timer_of_task()


@countdown
def what_time_is_it_now():
    print(time.strftime('%H:%M'))


what_time_is_it_now()
