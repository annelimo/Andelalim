count = 0
while (count < 202):
    if (count % 10) == 0 and (count % 6) == 0:
        print "FizzBuzz"
        count = count +1
    elif (count % 6) == 0:
        print "Fizz"
        count = count + 1
    elif (count % 4) == 0:
        print "Buzz"
        count = count +1
    else:
        print count
        count = count + 1