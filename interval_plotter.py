from datetime import datetime, date
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import urllib
from collections import Counter

try:
	dates = urllib.parse.unquote(sys.argv[1])
	dates = dates.split('\n')[2:]
	dates = [dt.strip() for dt in dates]
except:
	dates = [
		"2017-01-05 23:44", "2017-01-10 23:10",
		"2017-01-17 22:06", "2017-01-29 02:01",
		"2017-01-30 01:03",	"2017-02-03 00:49",
		"2017-02-03 21:27",	"2017-02-05 01:53",
		"2017-02-07 01:18",	"2017-02-09 22:04",
		"2017-02-11 22:36",	"2017-02-12 23:36",
		"2017-02-14 01:21",	"2017-02-18 22:40",
		"2017-02-23 22:28",	"2017-02-28 22:25",
		"2017-03-05 22:45",	"2017-03-13 23:20",
		"2017-03-18 22:30",	"2017-03-27 23:45",
		"2017-04-01 22:14",	"2017-04-12 22:43",
		"2017-04-15 23:12"
	]

dates = [datetime.strptime(dt,'%Y-%m-%d %H:%M') 
		 for dt in dates 
		 if dt.startswith('2')]
startdate = date(2018, 7, 1)
dates = [dt for dt in dates 
		 if dt.date() > startdate]
y = [1 + i * 0.1 for i, dt in enumerate(dates)]
# Calculate interval length, and disply result in days.
intervals = [(dates[i] - dates[i-1]).total_seconds()/86400 
			 for i, dt in enumerate(dates)]
intervals.pop(0)

# List and count occurances by day of week
days_list = [dt.strftime('%a') for dt in dates[1:]]
days_count = Counter(days_list)
day_names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
days_count_list = [days_count.get(day) for day in day_names]

plt.style.use('ggplot')
mpl.rc("savefig", dpi=600)
fig, ax = plt.subplots(figsize=(8, 12))

ax1 = plt.subplot(311)
plt.boxplot(intervals)
ax1.set_title('Interval Distribution')

ax2 = plt.subplot(312)
plt.plot(dates,y,'ro')
ax2.set_title('Dates')

ax3 = plt.subplot(313)
plt.bar(range(len(days_count_list)), days_count_list, align='center')
plt.xticks(range(len(day_names)), day_names)
ax3.set_title('Frequency by Day')

plt.show()

print('Total events: ', len(dates))
if round((datetime.now() - dates[-1]).total_seconds()/86400) != 0:
	print('Days since last event:', round((datetime.now() - dates[-1]).total_seconds()/86400))
else:
	print('Days between previous events:', round((dates[-1] - dates[-2]).total_seconds()/86400))
