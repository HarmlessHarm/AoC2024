import re

def puzzleA(data):
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    all = re.findall(regex, data)
    multiplications = [int(a) * int(b) for a, b in all]
    return sum(multiplications)

def puzzleB(data):
    data = ''.join(data.split('\n'))
    data = 'do()' + data + 'don\'t()'

    do_regex = r"do\(\)(.*?)don't\(\)"

    dos = re.findall(do_regex, data)
    print(dos)
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"

    summed = 0
    for do in dos:
        multiplications = [int(a) * int(b) for a, b in re.findall(regex, do)]
        summed += sum(multiplications)

    return summed

    mult_tupls = [re.findall(regex, do) for do in dos]
    flatten = [item for sublist in mult_tupls for item in sublist]
    multiplications = [int(a) * int(b) for a, b in flatten]
    return sum(multiplications)
