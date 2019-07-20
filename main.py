from ics import Calendar,Event
c = Calendar()
with open('plan.txt',"r") as f:
    lines = f.readlines()
    date = lines[0]
    c = Calendar()
    for i in range(len(lines)-1):
        if i/2 == i//2:
            time = lines[i+1]
        else:
            name = lines[i+1]
            e = Event()
            e.name = name
            e.begin = date+"T"+time[:5]+":00+08:00"
            e.end = date+"T"+time[-6:-1]+":00+08:00"
            c.events.add(e)

open('p.ics', 'w').writelines(c)
