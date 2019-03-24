# Part 2 Code

from csv import reader
from numpy import unique, empty, arange, mean
import matplotlib.pyplot as plt

def open_a_file(filename):
    try:
        with open(filename, 'r') as f:
            d1 = reader(f)
            da1 = list(d1)
    except IOError as ioe:
        print("I/O Error in openning file: %s" % ioe)
    
    return da1

def get_time_and_values(d):
    time = [e[0] for e in d]
    value = [e[1] for e in d]
    return time, value

def remove_missing_values(dat):
    dat_copy = list(dat)
    number_of_missing_values = 0
    a = 0
    for each in dat_copy:
        if len(each[0]) == 0:
            dat.pop(a)
            a -= 1
            number_of_missing_values += 1
        if len(each[1]) == 0:
            dat.pop(a)
            a -= 1
            number_of_missing_values += 1
        a += 1
    
    return dat, number_of_missing_values

def create_array_of_data(the_data):
    da = empty((len(the_data), len(the_data[0])))
    for e1 in arange(0, len(the_data)):
        for e2 in arange(0, len(the_data[0])):
            da[e1,e2] = the_data[e1][e2]
    
    return da

def find_outliers(d, sym, threshold):
    outliers = []
    for each in d:
        if sym == 'lt':
            if each[1] < threshold:
                outliers.append(each)
        elif sym == 'gt':
            if each[1] > threshold:
                outliers.append(each)
    o = create_array_of_data(outliers)
    
    return o

def find_averages(dat):
    averages = {}

    for each in dat:
        if each[0] in averages.keys():
            averages[each[0]].append(each[1])
        else:
            averages[each[0]] = [each[1]]
    
    for each in averages:
        averages[each] = mean(averages[each])
    
    avg = []
    for each in averages:
        avg.append([each, averages[each]])
    a = create_array_of_data(avg)
    
    return a

def scatter_plot(d, col):
    plt.scatter(d[:,0], d[:,1], c = col)

def create_scatter(title, labels, data_array, col):
    plt.title(title)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    scatter_plot(data_array, col)
    
labs = ['Time', 'Value']

data = open_a_file('flow_1.csv')

print(data[:5])
# Stores the headers
flow1_headers = data[0]

# Stores the data
flow1 = data[1:]

flow1_time, flow1_value = get_time_and_values(flow1)

#print(unique(flow1_time))
#print(unique(flow1_value))

f1, flow1_missing = remove_missing_values(flow1)
        
print('The total number of missing values was: %s' % flow1_missing)

data_flow1 = create_array_of_data(f1)

flow1_time, flow1_value = get_time_and_values(data_flow1)

print(unique(flow1_value))

flow1_avg = find_averages(data_flow1)

plt.figure(figsize = (22,12))
create_scatter('Average Flow_1 times vs measured values', labs, flow1_avg, 'blue')
plt.show()

flow1_outliers = find_outliers(data_flow1, 'gt', 400)

plt.figure(figsize = (22,12))
create_scatter('All Flow_1 times vs measured values', labs, data_flow1, 'blue')
scatter_plot(flow1_outliers, 'red')
plt.show()

data = open_a_file('flow_2.csv')

#print(data[:5])
flow2_headers = data[0]

flow2 = data[1:]

flow2_time_test, flow2_value_test = get_time_and_values(flow2)

#print(unique(flow2_time_test))
#print(unique(flow2_value_test))

f2, flow2_missing = remove_missing_values(flow2)

print('the number of missing values was %s' % flow2_missing)

data_flow2 = create_array_of_data(f2)

flow2_time, flow2_value = get_time_and_values(data_flow2)

print(unique(flow2_value))

flow2_avg = find_averages(data_flow2)

plt.figure(figsize = (22,12))
create_scatter('Average Flow_2 times vs measured values', labs, flow2_avg, 'blue')
plt.show()

plt.figure(figsize = (22,12))
scatter_plot(data_flow2, 'blue')
plt.show()

data = open_a_file('flow_3.csv')

#print(data[:5])
flow3_headers = data[0]

flow3 = data[1:]

flow3_time, flow3_value = get_time_and_values(flow3)

#print(unique(flow3_time))
#print(unique(flow3_value))

f3, flow3_missing = remove_missing_values(flow3)

print('the number of missing values was %s' % flow3_missing)

data_flow3 = create_array_of_data(f3)

flow3_time, flow3_value = get_time_and_values(data_flow3)

print(unique(flow3_value))

flow3_avg = find_averages(data_flow3)

plt.figure(figsize = (22,12))
create_scatter('Average Flow_3 times vs measured values', labs, flow3_avg, 'blue')
plt.show()

flow3_outliers = find_outliers(data_flow3, 'lt', 50)

plt.figure(figsize = (22,12))
create_scatter('All Flow_3 times vs measured values', labs, data_flow3, 'blue')
scatter_plot(flow3_outliers, 'red')
plt.show()

data = open_a_file('flow_4.csv')

#print(data[:5])
flow4_headers = data[0]

flow4 = data[1:]

flow4_time, flow4_value = get_time_and_values(flow4)

#print(unique(flow4_time))
#print(unique(flow4_value))

f4, flow4_missing = remove_missing_values(flow4)

print('the number of missing values was %s' % flow4_missing)

data_flow4 = create_array_of_data(f4)

flow4_time, flow4_value = get_time_and_values(data_flow4)

print(unique(flow4_value))

flow4_avg = find_averages(data_flow4)

plt.figure(figsize = (22,12))
create_scatter('Average Flow_4 times vs measured values', labs, flow4_avg, 'blue')
plt.show()

flow4_outliers = find_outliers(data_flow4, 'lt', 60)

#print(flow4_outliers)

for each in arange(0, len(flow4_outliers)):
    if flow4_outliers[each,0] > 1535000000:
        flow4_outliers[each] = flow4_outliers[0]
    elif flow4_outliers[each,0] > 1531000000 and flow4_outliers[each,0] < 1532000000:
        flow4_outliers[each] = flow4_outliers[0]
    elif flow4_outliers[each,0] > 1531000000 and flow4_outliers[each,1] > 30:
        flow4_outliers[each] = flow4_outliers[0]
        
        
plt.figure(figsize = (22,12))
create_scatter('All Flow_4 times vs measured values', labs, data_flow4, 'blue')
scatter_plot(flow4_outliers, 'red')
plt.show()

data = open_a_file('rain_1.csv')

#print(data[:5])

rain1_headers = data[0]

rain1 = data[1:]

rain1_time, rain1_value = get_time_and_values(rain1)

#print(unique(rain1_time))
print(unique(rain1_value))

data_rain1 = create_array_of_data(rain1)

rain1_avg = find_averages(data_rain1)

plt.figure(figsize = (22,12))
create_scatter('Average Rain_1 times vs measured values', labs, rain1_avg, 'blue')
plt.show()

rain1_outliers = find_outliers(data_rain1, 'lt', 0)

plt.figure(figsize = (22,12))
create_scatter('All Rain_1 times vs measured values', labs, data_rain1, 'blue')
scatter_plot(rain1_outliers, 'red')
plt.show()

data = open_a_file('rain_2.csv')

#print(data[:5])

rain2_headers = data[0]

rain2 = data[1:]

rain2_time, rain2_value = get_time_and_values(rain2)

#print(unique(rain2_time))
print(unique(rain2_value))

data_rain2 = create_array_of_data(rain2)

rain2_avg = find_averages(data_rain2)

rain2_avg = rain2_avg[rain2_avg[:,0].argsort()]

plt.figure(figsize = (22,12))
create_scatter('Average Rain_2 times vs measured values', labs, rain2_avg, 'blue')
#plt.axis([1526000000, 1535000000,-0.6,2])
plt.show()

rain2_outliers = find_outliers(data_rain2, 'gt', 2)
#print(rain2_outliers)

plt.figure(figsize = (22,12))
create_scatter('All Rain_2 times vs measured values', labs, data_rain2, 'blue')
scatter_plot(rain2_outliers, 'red')
#plt.axis([1526000000, 1535000000,-0.6,2])
plt.show()

#print(len(rain1), len(rain2))
#print(unique(rain1_time)) # 1519951000 to 1526254000
#print(unique(rain2_time)) # 1526255000 to 1543574000

#print(unique(flow1_time)) # 1519906000 to 1527819000
#print(unique(flow2_time)) # 1543554000 to 1543579000
#print(unique(flow3_time)) # 1535686000 to 1543546000
#print(unique(flow4_time)) # 1527819000 to 1535685000
ra1 = rain1_avg[rain1_avg[:,0].argsort()]
ra2 = rain2_avg[rain2_avg[:,0].argsort()]
f1a = flow1_avg[flow1_avg[:,0].argsort()]
f4a = flow4_avg[flow4_avg[:,0].argsort()]
f3a = flow3_avg[flow3_avg[:,0].argsort()]
f2a = flow2_avg[flow2_avg[:,0].argsort()]

# plt.figure(figsize = (22,12))
# plt.scatter(rain1_avg[:,0], rain1_avg[:,1]*250, c = 'black')
# plt.scatter(data_f1_avg[:,0], data_f1_avg[:,1], c= 'red')
# plt.show()
# print(t[:5])
plt.figure(figsize = (22,12))
plt.plot(f1a[:,0], f1a[:,1], c= 'red')
plt.plot(f4a[:,0], f4a[:,1], c= 'red')
# plt.scatter(ra2[446:,0], ra2[446:,1]*250, c = 'black', s = 100)
plt.plot(f3a[:,0], f3a[:,1], c= 'red')
plt.plot(ra1[:,0], ra1[:,1]*250, c = 'black')
plt.plot(ra2[:446,0], ra2[:446,1]*250, c = 'black')
plt.show()
