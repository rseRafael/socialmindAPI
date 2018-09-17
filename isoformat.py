from datetime import datetime as dt
import os

def isoformat(isoformat):
    if type(isoformat) != str:
        return None
    if len(isoformat) < 16:
        return None
    else:
        if len(isoformat) > 16:
            isoformat = isoformat[0:16]
        try:
            date = []
            arr = isoformat.split("-")
            for i in range(len(arr)-1):
                date.append(arr[i])
            arr2 = arr[len(arr)-1].split("T")
            for i in range(len(arr2)-1):
                date.append(arr2[i])
            arr3 = arr2[len(arr2)-1].split(":")
            for i in range(len(arr3)):
                date.append(arr3[i])
            print(date)
            for i in range(len(date)):
                date[i] = int(date[i])
                if date[i] == None:
                    break
            year  = None
            month = None
            day = None
            hour = None
            minute = None
            if(len(date) == 5):
                year = date[0]
                month = date[1]
                day = date[2]
                hour = date[3]
                minute = date[4]

            d = dt(year, month, day, hour, minute)
            return d
        except (Exception, ValueError):
            return None
if __name__ == "__main__":
    d = dt.today()
    iso = d.isoformat()
    print(iso)
    print(isoformat(d.isoformat()))
    
