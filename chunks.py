# Python Exercises By Kesav Sir

# 1. Write a list comprehension to chunk a given list into n number of sublits. Eg:
# data = list(range(1200))
# //create sublist chunks of 500 from this data list
# chunks = <code>
# assert len(chunks)==3
# assert len(chunks[0])==500
# assert len(chunks[-1])==200

from itertools import islice
data = list(range(1200))
# create sublist chunks of 500 from this data list
chunks = [data[idx:idx+500] for idx in range(0, len(data), 500)]
assert len(chunks) == 3
assert len(chunks[0]) == 500
assert len(chunks[-1]) == 200


# 2. Write a function which will chunk a given iterator/generator into n number of lists. Eg:
# def chunker(n, iterable):
#     pass
# data = map(str, list(range(1200))
# chunks = chunker(500, data)
# assert len(chunks)==3
# assert len(chunks[0])==500
# assert type(chunks[0])==list
# assert type(chunks[0][0])==str
# assert len(chunks[-1])==200


def chunker(n, iterable):
    result = []
    while(1):
        chunk = list(islice(iterable, n))
        if(not chunk):
            break
        result.append(chunk)
    return result


data = map(str, list(range(1200)))
chunks = chunker(500, data)
assert len(chunks) == 3
assert len(chunks[0]) == 500
assert type(chunks[0]) == list
assert type(chunks[0][0]) == str
assert len(chunks[-1]) == 200
