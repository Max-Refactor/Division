from pprint import pprint
import os

def division(a: int, b: int):
    os.system('cls||clear')
    try:
        dvars = {
            'a': {
                'lenght': len(str(a)),
                'list': []
            },
            'b': {
                'lenght': len(str(b))
            },

            'division_ints': [],
            'result': f'{a}|{b}\n'
        }

        for i in range(0, dvars['a']['lenght']):
            dvars['a']['list'].append(str(a)[i])

        while True:
            lenght = dvars['a']['lenght'] = len(dvars['a']['list'])
            if lenght > 1:
                var = dvars['a']['list'].pop(1)
                dvars['a']['list'][0] += var
                dvars['division_ints'].append(dvars['a']['list'][0])
                dvars['a']['list'].remove(dvars['a']['list'][0])
                print('Next')
            elif lenght == 1:
                dvars['division_ints'].append(dvars['a']['list'][0])
                dvars['a']['list'].remove(dvars['a']['list'][0])
            else:
                print('OK!')
                break

        pprint(dvars, width=3)
    except Exception as Error:
        print(Error)

if __name__ == '__main__': 
    division(input("A: "), input("B: "))
