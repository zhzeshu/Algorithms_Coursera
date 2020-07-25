from heapq import heappop, heappush, heapify


def get_data(file_name):
    heap_input = []
    with open(file_name, "r") as data:
        for line in data:
            heap_input.append(int(line))
        data.close()
    return heap_input


def calculation(heap_input_list):
    heap_low = []
    heap_high = []
    heap_medium = []

    heapify(heap_low)
    heapify(heap_high)
    size_low = 0
    size_high = 0

    # heap_input_list = get_data("data1.txt")
    input1 = heap_input_list[0]
    input2 = heap_input_list[1]
    heap_medium.append(input1)

    if input1 > input2:
        input1, input2 = input2, input1
    heap_medium.append(input1)

    heappush(heap_low, -1*input1)
    heappush(heap_high, input2)
    size_low += 1
    size_high += 1

    for i in range(2, len(heap_input_list)):
        element = heap_input_list[i]
        heap_high_min = heap_high[0]
        if element > heap_high_min:
            heappush(heap_high, element)
            size_high += 1
            if size_high - size_low == 2:
                heappush(heap_low, -1*heappop(heap_high))
                size_low += 1
                size_high -= 1

        else:
            heappush(heap_low, -1*element)
            size_low += 1
            if size_low - size_high == 2:
                heappush(heap_high, -1*heappop(heap_low))
                size_low -= 1
                size_high += 1

        if size_high > size_low:
            element = heap_high[0]
            heap_medium.append(element)

        else:
            element = -1*heap_low[0]
            heap_medium.append(element)

    return sum(heap_medium) % 10000


heap_input_list = get_data("Median.txt")
print(calculation(heap_input_list))


