a1 = [3, 2, 1, 2, 3, 4, 6, 8, 7, 4, 5, 10, 11, 12, 15, 16, 17, 18, 22]
a = [1, 2, 3, 2, 1, 4, 3, 2, 4, 5, 1]


def increasing(a):
    b = []
    count = 0
    for i in range(0, len(a)-1):
        if a[i] < a[i+1]:
            b.append(a[i])
            '''try:
                if a[i+1] > a[i+2]:
                    b.append(a[i+1])
            except ValueError:
                break'''
            print(b)


#increasing(a1)

def demir(l: list):
    x = [l[0]] #set x to a LIST that contains the first element of l
    for i in range(1, len(l)): # go from second element to the last one
        #print("i is",i)
        if l[i] > x[-1]: # if the next element is greater than the highest
            # ele in x (means increasing value in that period) and append the elemt to the current sequence
            x.append(l[i])
        else: # if revenue is not increasing
            print(x, "How many periods in a row increasing:", len(x)) # print old list containing the current seqeuence
            # of increasing revenues
            x = [l[i]] # create a new list that will represent the new sequence of increasing revenues
        if i == len(l)-1: # print out the sequence in the last round of the iterations
            print(x, "How many periods in a row increasing:", len(x))

#print(a1, "length", len(a1))
demir(a1)