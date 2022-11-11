import pymysql
import redis
import datetime
from dateutil.relativedelta import relativedelta
from my_settings import DATABASES


conn = pymysql.connect(host=DATABASES['HOST'], port=DATABASES['PORT'], user=DATABASES['USER'], password=DATABASES['PASSWORD'], db=DATABASES['NAME'], charset='utf8')
cur = conn.cursor()

now = datetime.datetime.now()
now = now + relativedelta(seconds=-(now.second % 5))

period = 'month'

if period == 'month':
    start = 2592000  # 60 * 60 * 24 * 30
    delta = 86400  # 60 * 60 * 24
    data_count = 30
    period_now = datetime.datetime(now.year, now.month, now.day, 0, 0, 0) + relativedelta(seconds=-1)

elif period == 'week':
    start = 604800  # 60 * 60 * 24 * 7
    delta = 43200  # 60 * 60 * 12
    data_count = 14
    if now.hour >= 12:
        period_now = datetime.datetime(now.year, now.month, now.day, 12, 0, 0)
    elif now.hour < 12:
        period_now = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)

elif period == 'day':
    start = 86400  # 60 * 60 * 24
    delta = 3600  # 60 * 60
    data_count = 24
    period_now = datetime.datetime(now.year, now.month, now.day, now.hour, 0, 0)

sql = "select id, number from patient"
cur.execute(sql)
result = cur.fetchall()

for data in result:
    patient_id = data[0]
    patient_number = data[1]

    period_temperature = []
    period_bpm = []
    period_oxygen_saturation = []

    period_start = period_now + relativedelta(seconds=-start)

    while period_start < period_now:

        period_end = period_start + relativedelta(seconds=delta)

        sql = "select max(temperature), min(temperature), max(bpm), min(bpm), max(oxygen_saturation), min(oxygen_saturation) from patient_status where patient_id=%s and now > %s and now <= %s and temperature > 0"
        vals = (patient_id, period_start, period_end)
        cur.execute(sql, vals)
        period_health = cur.fetchall()

        max_temperature = period_health[0][0]
        min_temperature = period_health[0][1]

        max_bpm = period_health[0][2]
        min_bpm = period_health[0][3]

        max_oxygen_saturation = period_health[0][4]
        min_oxygen_saturation = period_health[0][5]

        if max_temperature:
            
            if period == 'month':
                period_value = period_end.strftime('%Y-%m-%d')
            else:
                period_value = period_start.strftime('%Y-%m-%d %H:%M:%S')

            temperature = {
                '시간': period_value,
                '최대': max_temperature,
                '최소': min_temperature
            }
            period_temperature.append(temperature)

            bpm = {
                '시간': period_value,
                '최대': max_bpm,
                '최소': min_bpm
            }

            period_bpm.append(bpm)
            
            oxygen_saturation = {
                '시간': period_value,
                '최대': max_oxygen_saturation,
                '최소': min_oxygen_saturation
            }

            period_oxygen_saturation.append(oxygen_saturation)
        
        period_start = period_end

    tmp_temperature = []
    tmp_bpm = []
    tmp_oxygen_saturation = []

    if len(period_temperature) < data_count:
        
        for i in range(1, data_count - len(period_temperature) + 1):
            now_datetime = period_now + relativedelta(seconds=-start) + relativedelta(seconds=(i * delta))
            if period == 'month':
                tmp_now = now_datetime.strftime('%Y-%m-%d')

            elif period == 'week':
                tmp_now = (now_datetime + relativedelta(seconds=-delta)).strftime('%Y-%m-%d %H:%M:%S')

            elif period == 'day':
                tmp_now = (now_datetime + relativedelta(seconds=-delta)).strftime('%Y-%m-%d %H:%M:%S')

            temperature = {
                '시간': tmp_now,
                '최대': 0.0,
                '최소': 0.0
            }
            tmp_temperature.append(temperature)

            bpm = {
                '시간': tmp_now,
                '최대': 0,
                '최소': 0
            }
            tmp_bpm.append(bpm)

            oxygen_saturation = {
                '시간': tmp_now,
                '최대': 0,
                '최소': 0
            }
            tmp_oxygen_saturation.append(oxygen_saturation)

    result_temperature = tmp_temperature + period_temperature
    result_bpm = tmp_bpm + period_bpm
    result_oxygen_saturation = tmp_oxygen_saturation + period_oxygen_saturation

    # print(result_temperature)
    connect = redis.StrictRedis(host=DATABASES['HOST'], port=6379, db=1, charset='utf-8', decode_responses=True, password=DATABASES['PASSWORD'])

    for i in range(data_count):

        connect.hmset(f'{patient_number}_temperature_month_{i+1}', result_temperature[i])
        connect.hmset(f'{patient_number}_bpm_month_{i+1}', result_bpm[i])
        connect.hmset(f'{patient_number}_oxygen_saturation_month_{i+1}', result_oxygen_saturation[i])

conn.close()