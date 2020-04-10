from calendar import datetime
from datetime import timedelta
H, M = map(int, input().split())

set = datetime.timedelta(hours=H, minutes=M)
if 0<=H<=23 and 0<=M<=59:
    set = set - timedelta(minutes=45)
    print(set)
else:
    H, M = map(int, input().split())