from datetime import datetime

dt = datetime(2025, 4, 26, 17, 32, 3)

# Преобразуем обратно в unixtime
timestamp = int(dt.timestamp())

print(timestamp)