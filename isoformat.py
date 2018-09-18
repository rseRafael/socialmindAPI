from datetime import datetime
import os

def formatISO(isofstr):
    if type(isofstr) != str and len(isofstr) < 16:
        return None
    else:
        if len(isofstr) > 16:
            isofstr = isofstr[0:16]
        try:
            _date = []
            _date = isofstr.split("-")
            _string = _date[len(_date) - 1]
            holder = _string.split("T")
            _date.pop()
            for i in range(len(holder)-1):
                _date.append(holder[i])
            _string = holder[len(holder)-1]
            holder = _string.split(":")

            for i in range(len(holder)):
                _date.append(holder[i])

            for i in range(len(_date)):
                if type(_date[i]) != str:
                    return None
                else: 
                    _date[i] = int(_date[i])

            year, month, day, hour, minute  = ( None, None, None, None, None)  

            if len(_date) == 5:
                year = _date[0]
                month = _date[1]
                day = _date[2]
                hour = _date[3]
                minute = _date[4]
            else:
                return None

            _dateObj = datetime(year, month, day, hour, minute)
            return _dateObj

        except (Exception, ValueError):
            print(666)
            print(_date[i])
            return None


if __name__ == "__main__":
    d = dt.today()
    iso = d.isofstr()
    print(iso)
    print(isofstr(d.isofstr()))
    
