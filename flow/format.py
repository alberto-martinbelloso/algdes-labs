
def parse_input():
    start = False
    array = []
    with open('./data/rail.txt') as f:
        for line in f:
            if(start):
                array.append([ int(x) for x in line.split(' ')])
                
            if('119' in line):
                start = True
    
    return array