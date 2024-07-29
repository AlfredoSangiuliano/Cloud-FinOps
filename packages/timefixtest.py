
datetime = "datetime.datetime(2023, 7, 23, 21, 52, 34, 895000, tzinfo=tzlocal())"
# datetime = "2024-07-23T21:28:55.960+0000"

def fix_datetime(datetime):
    if "datetime.datetime" in datetime:
        return datetime[18:22]
    elif "+0000" in datetime:
        return datetime[0:4]


print(fix_datetime(datetime))