from pprint import pprint
import os


def division(a: int, b: int):
    os.system('cls' if os.name == 'nt' else 'clear')
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
            'division_ints2': [],
            'remainder': 0,
            'result': f'{a}|{b}\n'  # Provide values for a and b here
        }

        for i in range(0, dvars['a']['lenght']):
            dvars['a']['list'].append(str(a)[i])

        lenght = len(dvars['a']['list'])
        while True:
            if lenght > 1:
                var = dvars['a']['list'].pop(1)
                dvars['a']['list'][0] += var
                dvars['division_ints'].append(dvars['a']['list'][0])
                dvars['a']['list'].remove(dvars['a']['list'][0])
                print('Next')
            elif lenght == 1:
                if dvars['a']['list'][0] % b == 0:
                    dvars['division_ints'].append(str(dvars['a']['list'][0]))
                    dvars['a']['list'].remove(dvars['a']['list'][0])
                else:
                    # dvars['division_ints2'][len(dvars['division_ints2'])] += dvars['a']['list'][0]
                    # dvars['remainder'] += 1
                    # dvars['division_ints2'][0] -= 1
                    print('Next')
            else:
                print('OK!')
                break

            lenght -= 1
            
        for i in dvars:
            print(i, dvars[i])
    except Exception as Error:
        print(f'Error: {Error}')


if __name__ == '__main__':
    division(155, 2)
