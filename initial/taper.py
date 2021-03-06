from collections import defaultdict


def get_sizes(dose):
    tots = []
    for mg in [50, 20, 10, 5, 2.5, 1]:
        n = dose//mg
        for _ in range(int(n)):
            tots += (str(mg),)
        dose -= mg * n
        if dose == 0.5:
            del tots[-1]
            dose = int(round(mg * n))
            
    return tots


def rx(dose, days):
    sizes = get_sizes(dose)
    return dict((i, (sizes.count(i)) * days) for i in sizes)
    
    
def main():
    
    phases = []
    
    args = { '1': {'dose': 60, 'time': 20}, '2': {'dose': 30, 'time': 15} }
    
#    phases = { {'dose': 20, 'quantity': 30}, {'dose': 10, 'quantity': 50} }
#    args = {'1': {'dose':60, 'time':60}}
    
    
    # --------------------------------------------
    # Iterate Phases
    
    for k in args:
        dose = args[k].get('dose')
        time = args[k].get('time')
        phases.append(rx(dose, time))
    
        
    result = dict.fromkeys(set().union(*phases), 0)
    

    
    for d in phases:
        for k in d.keys():
            result[k] += d[k]
    

    yield_ = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
    
    for k, v in yield_.items():
        print k
    


if __name__ == "__main__":
    main()