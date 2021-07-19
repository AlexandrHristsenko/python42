def convert(seconds):
    if seconds <= 86400:
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        print(f'{hours}:{minutes}:{seconds}')

    else:
        print('Error 404, time not found')

convert(int(input()))