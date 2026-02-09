import datetime
import pickle
import csv


#['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', 
#'__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
#'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']

print(datetime.time(hour=2,minute=25,second=55))
print(datetime.timedelta(days=3,weeks=4,hours=19,minutes=45,seconds=23))
print(datetime.datetime(year=2022,month=9,day=5,hour=14,minute=45,second=5,microsecond=39))

print(pickle.TUPLE)


#['QUOTE_MINIMAL', 'QUOTE_ALL', 'QUOTE_NONNUMERIC', 'QUOTE_NONE', 'QUOTE_STRINGS',
# 'QUOTE_NOTNULL', 'Error', 'Dialect', 'excel', 'excel_tab', 'field_size_limit', 'reader',
# 'writer', 'register_dialect', 'get_dialect', 'list_dialects', 'Sniffer', 'unregister_dialect', 'DictReader', 'DictWriter', 'unix_dialect']
