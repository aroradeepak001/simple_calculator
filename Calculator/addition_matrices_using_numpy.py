import numpy

def addition_using_numpy(listA,listB):
    numpyArrayA = numpy.array(listA)
    numpyArrayB = numpy.array(listB)
    return numpyArrayA + numpyArrayB


def addition_of_normal_lists(listA,listB):
    return [ x + y for x,y in zip(listA,listB)]


def addition_using_for_loops(listA,listB):
    C=[]
    for x,y in zip(listA,listB):
        C.append(x+y)

    return C
