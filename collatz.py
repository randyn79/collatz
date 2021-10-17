from sympy import isprime



def collatz_sequence(x: int) -> list:
    """Takes a positive integer and if even divides by 2,
if odd, multiplies by 3 and adds one.  Returns a list as
the result."""
    # Initialize sequence list
    sequence = [x]

    # Loops until the value of x equals 1
    while x > 1:

        # If even, divide by 2 and add to list
        if x % 2 == 0:
            x = x//2
            sequence.append(x)
            
        # If odd, multiply by 3 and add 1, and add to list
        elif x % 2 != 0:
            x = 3 * x + 1
            sequence.append(x)
            
    # Return the list for the Collatz sequence for the number x
    return sequence


def prime_sequence(sequence: list) -> list:
    """Takes a list of positive integers and if the integer is
prime it appends it to the primelist"""

    #Initialize primelist list
    primelist = []

    # Loop through each integer in the inputted list
    for i in sequence:

        # If the integer is prime, append to the primelist list
        if isprime(i) == True:
            primelist.append(i)

    # Return the list for the primelist
    return primelist


def evens_odds(sequence: list) -> tuple:
    """Takes a list of positive integers and if the integer is
even it appends it to the evens list, if it is odd it appends it
to the odds list"""

    # Initialize evens and odds lists
    evens = []
    odds = []

    # Loop through each integer in the inputted list
    for i in sequence:

        # If the integer is even, append it to the evens list
        if i % 2 == 0:
            evens.append(i)

        # If the integer is odd, append it to the odds list
        elif i % 2 != 0:
            odds.append(i)

    # Returns the evens and odds lists as a tuple of lists
    return evens, odds


def frequency_count(sequence: list) -> dict:
    """Counts the frequency of each number in the sequence list"""

    # Initialize a dictionary to store the frequency counts
    counts = {}

    #Loop through each integer in the sequence
    for i in sequence:
        # If the integer is not in the dictionary, add it to the dictionary
        # with a value of zero
        if i not in counts:
            counts[i] = 0
        # If the integer is in the dictionary, increment the value by 1
        counts[i] += 1
    # Sort the dictionary as descending
    sortedcounts = {k: v for k, v in sorted(counts.items(), key=lambda counts: counts[1], reverse = True)}
    # Return the sortedcounts dictionary
    return sortedcounts

def print_collatz(x, sequence, primelist, evens, odds, sortedcounts):
    """Prints the formatted output of the program"""

    # Set the length of formatting lines (___, ---, ===, etc)
    formatcount = 75
    
    print()
    print('=' * formatcount)
    print('For number {}...'.format(x))
    print('=' * formatcount)
    print()
    print("Collatz Sequence: {}".format(sequence))
    print("--Collatz sequence is {} numbers long.".format(len(sequence)))
    print()
    print("Primes in this sequence: {}".format(primelist))
    print("--Primes sequence is {} numbers long.".format(len(primelist)))
    print()
    print("Evens in this sequence: {}".format(evens))
    print("--Evens sequence is {} numbers long.".format(len(evens)))
    print()
    print("Odds in this sequence: {}".format(odds))
    print("--Odds sequence is {} numbers long".format(len(odds)))
    print()
    print("Frequency of each number: {}".format(sortedcounts))
    print()
    print('=' * formatcount)

  
    
    

def run_sequences(x):
    """Runs all functions that generate sequences and calls the print_collatz
function"""
    # Call the collatz_sequence function
    sequence = collatz_sequence(x)
    # Call the prime_sequence function
    primelist = prime_sequence(sequence)
    # Call the evens_odds function
    evens, odds = evens_odds(sequence)
    # Call the frequency_count function
    sortedcounts = frequency_count(sequence)

    # Call the print_collatz function
    print_collatz(x, sequence, primelist, evens, odds, sortedcounts)
    


# If program is being run independently and not as a function
if __name__ == "__main__":
    
    # Input choice of whether to run the program for one number or a range
    # of numbers
    choice = int(input("Enter 1 to run the sequence for one number or enter 2 to run the sequence for a range of numbers: "))

    # If the program is being ran for one number, enter the number
    if choice == 1:
        x = int(input("Enter the number to run the sequence on: "))
        # Call the run_sequences function
        run_sequences(x)

    # If the program is being ran for a range of numbers, enter the start
    # and end number
    elif choice == 2:
        start = int(input("Enter the starting number:  "))
        end = int(input("Enter the ending number:  "))

        for x in range(start, end + 1):
            
            run_sequences(x)

        
        
    


