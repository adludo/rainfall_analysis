data = numpy.random.random(100)
bins = numpy.linspace(0, 1, 10)
digitized = numpy.digitize(data, bins)
bin_means = [data[digitized == i].mean() for i in range(1, len(bins))]

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