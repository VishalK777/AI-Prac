def schedule_jobs(jobs):
    sorted_jobs = sorted(jobs, key=lambda x: x['deadline'])
    schedule = []
    current_time = 0

    for job in sorted_jobs:
        if current_time + job['duration'] <= job['deadline']:
            schedule.append(job)
            current_time += job['duration']

    return schedule

jobs = [
    {'duration': 3, 'deadline': 6},
    {'duration': 2, 'deadline': 4},
    {'duration': 4, 'deadline': 8},
    {'duration': 1, 'deadline': 5}
]

schedule = schedule_jobs(jobs)
print(schedule)
