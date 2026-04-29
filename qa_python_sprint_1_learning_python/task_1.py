time = '1h 45m,360s,25m,30m 120s,2h 60s'
minutes_sum = 0
time_list = time.replace(',', ' ').split(' ')
for time in time_list:
    if 'h' in time:
        hours = int(time.replace('h', ''))
        minutes_sum += hours * 60
    if 'm' in time:
        minutes = int(time.replace('m', ''))
        minutes_sum += minutes
    if 's' in time:
        second = int(time.replace('s', ''))
        minutes_sum += second // 60
print(f'Общее количество минут: {minutes_sum}')