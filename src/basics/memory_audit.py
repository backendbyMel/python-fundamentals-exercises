"""
"""

def run_audit():
    #create lists with the exact same content
    l1 = ['1','hello',3,5,'hi']
    l2 = ['1','hello',3,5,'hi']

    #confirm two lists have the same value
    print(l1==l2)

    #confirm that these objects are distinct at different memory addresses
    print(l1 is l2)

    #inspect the memory addresses
    print(id(l1))
    print(id(l2))

    #confirm that assignment does not copy the list
    #it copies the pointer
    l3 = l1

    #print the memory addrss to verify that it is the same with l1
    print(l3)
    print(l3==l1)
    print(l3 is l1)
    print(id(l3))


    #ghost update
    l3.append(999)
    print(l1)

    #small integer caching where python caches and reuses
    #small integers and short strings as an optimization
    x=42
    y=42
    print(x is y)

    #To avoid shared reference bugs,
    #create a true copy using slicing or list constructor
    l4 = l1[:]
    print(l4 is l1)
    print(l4==l1)

if __name__ == "__main__":
    run_audit()