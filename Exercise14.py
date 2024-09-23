# Prompt user for the number of seconds
totSeconds = int(input("Enter the number of seconds: "))

# Calculate number of seconds to minutes and seconds if greater than 60
if totSeconds >= 60:
    minutes = totSeconds // 60
    seconds = totSeconds % 60
    

    if totSeconds >= 3600:
        hours = totSeconds // 3600
        remainingSeconds = totSeconds % 3600
        minutes = remainingSeconds // 60
        seconds = remainingSeconds % 60

        if totSeconds >= 86400:
            days = totSeconds // 84600
            remainingSeconds = totSeconds % 86400
            hours = remainingSeconds // 3600
            remainingSeconds %= 3600
            minutes = remainingSeconds // 60
            seconds = remainingSeconds % 60 
            print(f'Days {days} Hours {hours} Minutes {minutes} Seconds {seconds}')