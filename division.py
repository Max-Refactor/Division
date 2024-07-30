from pprint import pprint

def division(a: int, b: int):
    try:
        dvars = {
            'a': {
                'lenght': len(str(a)),
                'list': []
            },

            'division_ints': [],
            'result': f'{a}|{b}\n'
        }
        
        for i in range(0, dvars['a']['lenght']):
            dvars['a']['list'].append(str(a)[i])

        pprint(dvars, width=3)
    except Exception as Error:
        print(Error)

if __name__ == '__main__': division(15, 5)