# pandas df manipulation
# When we roll a die 6000 times, we expect to get each value around 1000 times. But when we roll two dice and sum the result, the distribution is going to be quite different. A histogram illustrates those distributions.
df = pd.DataFrame(np.random.randint(1, 7, 6000), columns = ['one'])
df['two'] = df['one'] + np.random.randint(1, 7, 6000)
ax = df.plot.hist(bins=12, alpha=0.5)


# takes means of bins
data = numpy.random.random(100)
bins = numpy.linspace(0, 1, 10)
digitized = numpy.digitize(data, bins)
bin_means = [data[digitized == i].mean() for i in range(1, len(bins))]
bin_means = (numpy.histogram(data, bins, weights=data)[0] /
             numpy.histogram(data, bins)[0]) # maybe faster?

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# arr = np.array([])
# new_arr = np.append(arr, 10)

# print('New Array: ', new_arr)

# data_len = len(rows)
# cnt = 0
# for i in range(data_len):
#     # print(rows[i][0])
#     if rows[i][0] == 'No':
#         # print('test')
#         cnt = cnt + 1 

# print(cnt)