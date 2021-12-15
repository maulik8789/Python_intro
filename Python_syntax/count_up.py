def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    answer = 0
    for num in range(start, stop) :
        answer = answer + num
    answer = answer + stop
    return answer


count_up(5, 7)        
