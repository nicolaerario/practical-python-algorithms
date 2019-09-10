from random import sample


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":

    to_sort = sample(range(100), 5)
    print(to_sort)
    print(quicksort(to_sort))
