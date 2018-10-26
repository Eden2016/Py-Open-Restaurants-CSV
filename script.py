# Run using Python3
# python3 script.py

import csv
from datetime import datetime, timedelta, time as Time

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def get_day_list(day_names):
	if "-" not in day_names:
		return [day_names]
	start_day, end_day = day_names.split('-')
	start_index = DAYS.index(start_day)
	days = DAYS[start_index:]
	end_index = days.index(end_day)
	days = days[:end_index+1]
	return days

def get_datetime_from_str(items):
	start_time = Time(*map(int, items[1].split(':'))).strftime("%I:%M")+items[2].upper()
	end_time = Time(*map(int, items[4].split(':'))).strftime("%I:%M")+items[5].upper()
	start_time = datetime.strptime(start_time, '%I:%M%p')
	end_time = datetime.strptime(end_time, '%I:%M%p')
	return start_time, end_time

def find_open_restaurants(filename, day, time):
	time = datetime.strptime(time, '%H:%M')

	open_restaurants_list = []
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			day_times = row[1].split("/")
			for day_time in day_times:
				days = []
				items = list(filter(None, day_time.split(" ")))
				if "," in items[0]:
					day_time = day_time.split(",")
					items = list(filter(None, day_time[-1].split(" ")))

					for daytime in day_time[:-1]:
						days = days + get_day_list(daytime)

				days = days + get_day_list(items[0])

				start_time, end_time = get_datetime_from_str(items)

				if day in days and start_time <= time and time <=end_time:
					open_restaurants_list.append(row[0])

	return  open_restaurants_list


if __name__ == '__main__':
	filename = "restaurant_hours.csv"
	day = "Tue"
	time = "11:30"
	print("Open Restaurants list ",find_open_restaurants(filename, day, time))