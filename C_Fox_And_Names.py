n = int(input())
records = []
heap = []

for _ in range(n):
    record = input().split()
    operation = record[0]
    
    if operation == 'insert':
        value = int(record[1])
        heap.append(value)
        records.append('insert ' + str(value))
    elif operation == 'getMin':
        value = int(record[1])
        if len(heap) == 0:
            heap.append(1e9)
            records.append('insert ' + str(1e9))
        records.append('getMin ' + str(value))
    elif operation == 'removeMin':
        if len(heap) == 0:
            heap.append(1e9)
            records.append('insert ' + str(1e9))
        heap.remove(min(heap))
        records.append('removeMin')

print(len(records))
for record in records:
    print(record)