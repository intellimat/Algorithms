const swap = require('../utils').swap;
// Optimized quickSort! The pivot is randomized we partition each time the array into three sets!
function quickSort(array) {
    if (Array.isArray(array))
        quickSort_recursive(array, 0, array.length-1)
}

function quickSort_recursive(array, left, right) {
    if ( left < right ) {
        randomizePivot(array, left, right)

        indeces = partition(array, left, right)
        m1 = indeces.m1
        m2 = indeces.m2

        quickSort_recursive(array, left, m1)
        quickSort_recursive(array, m2, right)
    }
}

function partition(array, left, right) {
    pivot = array[right]

    i = left
    k = right
    j = left

    while (j <= k) {
        if (array[j] < pivot){
            swap(array, i, j)
            i++
            j++
        } else if (array[j] > pivot) {
            swap(array, j, k)
            k--
        } else j++
    }

    indeces = {
        m1: i-1,
        m2: k+1
    }

    return indeces
}

function randomizePivot(array, left, right) {
    mid = Math.floor((left + right) / 2)

    first = array[left]
    last = array[right]
    median = array[mid]

    let swapping_index = mid

    if ((first > median && first < last) || (first < median && first > last))
        swapping_index = left
    else if ((last < median && last > first) || (last > median && last < first))
        swapping_index = right
    else if ((median < first && median > last) || (median > first && median < last))
        swapping_index = mid
    else if (median == first)
        swapping_index = right
    else if (median == last)
        swapping_index = left
    
    swap(array, swapping_index, right)

}

module.exports.quickSort = quickSort;