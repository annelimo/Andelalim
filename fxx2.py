def fizzbuzz(n):

    if n % 5 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 5 == 0:
        return 'Fizz'
    elif n % 7 == 0:
        return 'Buzz'
    else:
        return str(n)

print "\n".join(fizzbuzz(n) for n in xrange(1, 11))
