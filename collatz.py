from sympy import isprime

def collatz_sequence(x: int) -> list:
    sequence = [x]
    while x > 1:

        if x % 2 == 0:
            x = x//2
            sequence.append(x)

        elif x % 2 != 0:
            x = 3 * x + 1
            sequence.append(x)
    
    return sequence


def prime_sequence(sequence: list) -> list:
    primelist = []

    for i in sequence:
        if isprime(i) == True:
            primelist.append(i)
    return primelist


def evens_odds(sequence: list) -> list:
    evens = []
    odds = []

    for i in sequence:
        if i % 2 == 0:
            evens.append(i)
        elif i % 2 != 0:
            odds.append(i)
    return evens, odds


def frequency_count(sequence: list) -> dict:
    counts = {}

    for i in sequence:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    sortedcounts = {k: v for k, v in sorted(counts.items(), key=lambda counts: counts[1], reverse = True)}
    return sortedcounts

def print_collatz(*args, **kwargs):
    formatcount = 75
    print()
    print('=' * formatcount)
    print('For number {}...'.format(x))
    print('=' * formatcount)
    print()
    print("Collatz Sequence: {}".format(sequence))
    print()
    print("Primes in this sequence: {}".format(primelist))
    print()
    print("Evens in this sequence: {}".format(evens))
    print()
    print("Odds in this sequence: {}".format(odds))
    print()
    print("Frequency of each number: {}".format(sortedcounts))
    print()
    print('=' * formatcount)

#def user_input(*args: int, **kwargs: int) -> None:
choice = int(input("Enter 1 to run the sequence for one number or enter 2 to run the sequence for a range of numbers: "))

if choice == 1:
    x = int(input("Enter the number to run the sequence on: "))
    # repeated code, move to main function
    sequence = collatz_sequence(x)
    primelist = prime_sequence(sequence)
    evens, odds = evens_odds(sequence)
    sortedcounts = frequency_count(sequence)

    print_collatz(x, sequence, primelist, evens, odds, sortedcounts)

   

elif choice == 2:
    start = int(input("Enter the starting number:  "))
    end = int(input("Enter the ending number:  "))

    for x in range(start, end + 1):
        #repeated code, move to main function
        sequence = collatz_sequence(x)
        primelist = prime_sequence(sequence)
        evens, odds = evens_odds(sequence)
        sortedcounts = frequency_count(sequence)

        print_collatz(x, sequence, primelist, evens, odds, sortedcounts)

        
        
    


