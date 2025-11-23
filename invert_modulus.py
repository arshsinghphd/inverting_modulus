'''INVERSE MODULES AND PRINT WORKS
-------------------------------
Functions and Their Description
-------------------------------
euclid
    This function takes two positive integers A and B.
    If A mod B have a positive integer as a multiplicative inverse,
        the function finds and returns it in a tuple where the first value is
        the mutliplicative inverse of A mod B.
    Else the first value of the tuple is None.

    If verbose is True and A mod B has a multiplicative inverse,
        the index 1 of returned tuple holds all the works to find it
        as a tuple of strings.
    If verbose is True and A mod B does not have a multiplicative inverse,
        the index 1 of returned tuple is a tuple with a single line
        that says so.
    Else if verbose is False, the index 1 of the tuple returned is always None.

reverse_euclid
    This function takes two integers A and B.
    If GCD(A, B) 1,
        it returns a 5-tuple of three lists of ints, an integer, and
        a list of strings.
    Else,
        returns None
'''

def reverse_euclid(A: int, B: int, verbose: bool = True) -> tuple:
    '''
    This function takes two positive integers A and B.
    If A mod B have a positive integer as a multiplicative inverse,
        the function finds and returns it in a tuple where the first value is
        the mutliplicative inverse of A mod B.
    Else the first value of the tuple is None.

    If verbose is True and A mod B has a multiplicative inverse,
        the index 1 of returned tuple holds all the works to find it
        as a tuple of strings.
    If verbose is True and A mod B does not have a multiplicative inverse,
        the index 1 of returned tuple is a tuple with a single line
        that says so.
    Else if verbose is False, the index 1 of the tuple returned is always None.

    Params:
    A (int)
    B (int)

    Returns:
    int     x such that Ax = 1 mod B, if it exists, Else None.

    Calls:
    euclidean
    '''

    t = euclidean(A, B, True)
    if not t:
        return (None,
                (f"The multiplicative inverse for {A} mod {B} does not exist.",))
    else:
        quotients, first_vars, second_vars, counter, works = t
        n = counter

    # Reverse
    if verbose:
        #print("\nSecond Part: Reversing\n")
        works.append('')
        works.append('-'*80)
        works.append('Second Part: Reversing')
        works.append('-'*80)
    # initiate variables
    c1 = 0
    c2 = 1
    v2 = 1
    # reassigning
    q = quotients.pop()
    temp = c2
    c2 = c1 - c2 * q
    c1 = temp
    counter += 1
    if verbose:
        # printing
        works.append(f'Isolating {v2} from ({n})')
        v1 = first_vars.pop()
        v2 = second_vars.pop()
        n -= 1
        equation_str = f'1 = {v1} * {c1} + {v2} * {c2}'
        counter_str = f'... ({counter})'
        works.append(f'{equation_str:<70}{counter_str:>10}')
    while quotients:
        # reassigning
        q = quotients.pop()
        temp = c2
        c2 = c1 - c2 * q
        c1 = temp
        counter += 1
        if verbose:
            works.append(f'Isolating {v2} from ({n}) and putting in \
({counter - 1}).')
            v1 = first_vars.pop()
            v2 = second_vars.pop()
            works.append(f'Rearrange to keep as a linear combination of \
{v1} and {v2}:')
            n -= 1
            equation_str = f'1 = {v1} * {c1} + {v2} * {c2}'
            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
            works.append('')
    if c2 < 0:
        old_c2 = c2
        old_c1 = c1
        k = 0
        while c2 < 0:
            k += 1
            c2 += B
        assert (1 - c2*v2) % v1 == 0
        c1 = (1 - c2*v2)//v1
        if verbose:
            counter += 1
            works.append('Because we want a positive multiplicative inverse')
            works.append(f"    replace {old_c2} with {old_c2} + k * {B}")
            works.append(f"    such that {old_c2} + k * {B} > 0.")
            works.append(f"In this case, k = {k} and we replace {old_c2} \
with {c2}.")
            works.append(f"    Also find new coefficient of {B} as")
            works.append(f"    {old_c1} - k * {A} = {c1}, since k = {k}.")
            works.append('')
            works.append(f"Finally:")
            equation_str = f'1 = {B} * {c1} + {A} * {c2}'
            
            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
            works.append('')

    if verbose:
        works.append(f'Bézout\'s coefficients are {c1} and {c2}.')
        works.append('')
        works.append(f'The multiplicative inverse of {A} mod {B} is {c2}.')
        works.append('-'*80)

    multiplicative_inverse = c2
    return multiplicative_inverse, tuple(works)

def euclidean(A: int, B: int, verbose: bool = False) -> tuple:
    '''
    This function takes two integers A and B.
    If GCD(A, B) 1,
        it returns a 5-tuple of three lists of ints, an integer, and
        a list of strings.
    Else,
        returns None
    '''
    # initiate stacks
    first_vars = list()
    second_vars = list()
    quotients = list()
    works = list()
    # initiate variables
    greater = B
    smaller = A
    q = greater // smaller
    mod = greater % smaller
    counter = 1
    # fill stacks
    first_vars.append(greater)
    second_vars.append(smaller)
    quotients.append(q)
    if verbose:
        works.append('-'*80)
        works.append('First Part: Euclidean Algorithm')
        works.append('-'*80)
        works.append('Euclidean algorithm gives us the following equations.')
        works.append('')
        equation_str = f'{greater} = {smaller} * {quotients[-1]} + {mod}'
        counter_str = f'... ({counter})'
        works.append(f'{equation_str:<70}{counter_str:>10}')
    while mod > 0:
        # reassign variables
        greater = smaller
        smaller = mod
        q = greater // smaller
        mod = greater % smaller
        # fill stacks
        first_vars.append(greater)
        second_vars.append(smaller)
        quotients.append(q)
        counter += 1
        if verbose:
            # print
            equation_str = f'{greater} = {smaller} * {quotients[-1]} + {mod}'
            counter_str = f'... ({counter})'
            works.append(f'{equation_str:<70}{counter_str:>10}')
        if mod == 1:    # early stop if we know GCD(A, B) is 1
            return quotients, first_vars, second_vars, counter, works
    return None

#x, printing_block = reverse_euclid(197, 2001, True)
# large primes < 10**6: 999979, 999983
# large primes < 10**9: 961748941, 982451653
# https://t5k.org/lists/small/millions/
x, printing_block = reverse_euclid(961748941, 982451653, True)
print(x)

for line in printing_block:
    print(line)
