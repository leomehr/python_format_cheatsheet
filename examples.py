def numbers():
    n = 1234567.8910
    print(f'add commas: {n:,}')
    print(f'add _s: {n:_}')
    print(f'1 decimal: {n:.1f}')
    print(f'percent: {0.34:.0%}')
    print()
    bases = 'dxb'
    print(' |'.join(f'{b:>6}' for b in bases))
    print('-*'.join('-'*6 for _ in bases))
    for i in range(6, 12, 1):
        s = ' |'.join('{i:>6{base}}'.format(i=i, base=b) for b in bases)
        print(s)

def alignment():
    for align, text in zip('<^>', ['left', 'center', 'right']):
        print(f'{text:_{align}12}')

def triangles():
    height = 8
    col_width = 4
    num_cols = 4

    tot_width = (col_width+1) * num_cols + 2
    print(' ' * 5 + ''.join(f'{i:^{col_width + 1}}' for i in range(num_cols)))
    print(('   /{x:-^{tot_width}}\\').format(x='', tot_width=tot_width))

    for i in range(height):
        inner = ''
        for _ in range(num_cols):
            vals = [' ' for _ in range(col_width + 1)]
            j = i % (col_width + 1)
            vals[j] = '\\'
            vals[col_width - j] = '/'
            inner += ''.join(vals)
        print(f'{i:<3}| ' + inner + ' |')

    print(('   \\{x:-^{tot_width}}/').format(x='', tot_width=tot_width))

for ex in [
    numbers,
    alignment,
    triangles,
]:
    print('{:-^25}'.format(' ' + ex.__name__ + ' '))
    ex()
    print()
