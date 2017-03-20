def levDist( s1, s2 ):
    """
    *This algorithm is taken from https://rosettacode.org/wiki/Levenshtein_distance
    """
    if len( s1 ) > len( s2 ):
        s1,s2 = s2,s1
    distances = range( len(s1) + 1 )
    for index2,char2 in enumerate( s2 ):
        newDistances = [ index2 + 1 ]
        for index1,char1 in enumerate( s1 ):
            if char1 == char2:
                newDistances.append( distances[index1] )
            else:
                newDistances.append( 1 + min((distances[index1], distances[index1+1], newDistances[-1])) )
        distances = newDistances
    return distances[ -1 ]


strArr = [ "b2", "a1", "b1", "4", "2", "a3", "a2", "3", "1" ]
n = 6 #Has to be less than the size of the array

#sort the given array in lexographical order
i = 0
while i < len( strArr ):
    small = strArr[ i ]
    j = i + 1
    while j < len( strArr ):
        if strArr[ j ] < small:
            small = strArr[ j ]
            temp = strArr[ i ]
            strArr[ i ] = strArr[ j ]
            strArr[ j ] = temp
        j = j + 1
    i = i + 1

print "Sorted array is:" + str( strArr )

for index, ele in enumerate( strArr ):
    left = index - 1
    right = index + 1
    count = 1

    print "Closest " + str(n) + " elements of " + ele + " are:"

    try:
        while count <= n:
            if levDist( ele, strArr[ left ] ) <= levDist( ele, strArr[ right ] ):
                if left < 0:
                    raise IndexError
                print strArr[ left ]
                left = left - 1
            else:
                print strArr[ right ]
                right = right + 1
            count = count + 1
    except IndexError:
        if left < 0:
            while count <= n:
                print strArr[ right ]
                right = right + 1
                count  = count + 1
        elif right == len( strArr ):
            while count <= n:
                print strArr[ left ]
                left = left - 1
                count  = count + 1
