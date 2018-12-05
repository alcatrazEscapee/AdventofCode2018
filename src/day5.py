# Day 5: Alchemical Reduction


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
KEYWORDS = ['aA', 'Aa', 'bB', 'Bb', 'cC', 'Cc', 'dD', 'Dd', 'eE', 'Ee', 'fF', 'Ff', 'gG', 'Gg', 'hH', 'Hh', 'iI', 'Ii', 'jJ', 'Jj', 'kK', 'Kk', 'lL', 'Ll', 'mM', 'Mm', 'nN', 'Nn', 'oO', 'Oo', 'pP', 'Pp', 'qQ', 'Qq', 'rR', 'Rr', 'sS', 'Ss', 'tT', 'Tt', 'uU', 'Uu', 'vV', 'Vv', 'wW', 'Ww', 'xX', 'Xx', 'yY', 'Yy', 'zZ', 'Zz']


def reduce_polymer(poly):
    while True:
        start = poly
        for key in KEYWORDS:
            poly = poly.replace(key, '')
        if start == poly:
            break
    return poly


def find_best_polymer(poly):
    min_length = len(poly)
    for c in ALPHABET:
        poly_c = reduce_polymer(poly.replace(c, '').replace(c.upper(), ''))
        if len(poly_c) < min_length:
            min_length = len(poly_c)
    return min_length


if __name__ == '__main__':
    polymer = open('../assets/day5_input.txt').readline()
    print('The smallest is', reduce_polymer(len(polymer)))

    print('The best removal is', find_best_polymer(polymer))