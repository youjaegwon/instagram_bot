import datetime

# 포맷에 맞는 현재시간


def getNowDateTime(strDt):
    now = datetime.datetime.utcnow()
    return now.strftime(strDt)
