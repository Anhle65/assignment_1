def to_seconds(time_string):
    """Take time string of form 'hh:mm:ss' and 
    return number of seconds elapsed since start of day.
    """
    new_str = time_string.split(':')
    second_total = int(new_str[0])*3600 + int(new_str[1])*60 + int(new_str[2])
    return second_total

def new_task(task_id, start_string):
    """return the task and elapsed time"""
    return (task_id, [to_seconds(start_string)])
def start_task(tasks, task_id):
    """print tasks in list and return time elapsed"""
    if len(tasks) == 0 or len(tasks[-1][-1]) == 2 :
        time_set = input("Please enter a time (hh:mm:ss): ")
        task = new_task(task_id, time_set)
        tasks.append(task)
    elif len(tasks[-1][-1]) == 1:
        print("Can't start a timer, one is already running")
def end_active_task(tasks):
    """stops the running task"""
    if len(tasks) == 0 or len(tasks[-1][-1]) == 2:
        print("No timer is currently running")
    else:
        time_end = input("Please enter a time (hh:mm:ss): ")
        new = list(tasks[-1])
        time_add = (to_seconds(time_end))
        new[-1].append(time_add)
def read_list(prompt):
    """Return a list which seperated bt comma from the input """
    result = []
    data = input(prompt)
    for content in data.split(',') :
        result.append(content.strip())
    return result
def delete_task(tasks):
    """remove the task which running or completed timer"""
    if len(tasks) == 0 or len(tasks[-1][-1]) == 0:
        print("Can't remove task when none exist")
    elif len(tasks[-1][-1]) == 1 or len(tasks[-1][-1]) == 2: 
        tasks.clear()
def final():
    """choose the commands and print the result"""
    print("""Commands:
    [s] start
    [e] end active timer
    [d] delete
    [r] report
    [q] quit
            """)
    choice = input("Select command: ")
    tasks = []
    while choice != 'q':
        if choice == 'Q':
            break
        elif choice == 's' or choice == 'S':
            start_task(tasks, read_list('Enter task IDs: '))
        elif choice == 'e' or choice == 'E':
            end_active_task(tasks)
        elif choice == 'd' or choice == 'D':
            delete_task(tasks)
        elif choice == 'r' or choice == 'R':
            print("Report:")
            for i in range(len(tasks)):
                if len(tasks[-1][-1]) == 2:
                    print(f"    ({','.join(tasks[i][0])}) {tasks[i][-1][0]}:{tasks[i][-1][-1]}")
        else:
            print('Command is not valid')
        choice = input("Select command: ")
final()
