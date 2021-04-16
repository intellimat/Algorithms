const swap = require('../utils').swap;

function heapSort(array) {
    max_heap = buildMaxHeap(array)
    heap_size = array.length

    for ( i = 0; i < array.length-1; i++ ){
        swap(array, 0, heap_size - 1)
        heap_size--
        siftDown(array, heap_size, 0)
    }
}

function buildMaxHeap(array) {
    heapSize = array.length
    fromIndex = Math.floor((array.length - 1)/2) // last non-leaf node
    for (i=fromIndex; i>=0; i--) 
        siftDown(array, heapSize, i)
}

function siftDown(array, heapSize, i) {
    leftChildIndex = i*2 + 1
    leftChild = array[leftChildIndex]

    rightChildIndex = i*2 + 2
    rightChild = array[rightChildIndex]

    max = array[i]
    maxIndex = i

    if (leftChildIndex < heapSize && array[leftChildIndex] > max) {
        max = leftChild
        maxIndex = leftChildIndex
    } 

    if (rightChildIndex < heapSize && array[rightChildIndex] > max) {
        max = rightChild
        maxIndex = rightChildIndex
    }

    if (maxIndex != i) {
        swap(array, i, maxIndex)
        siftDown(array, heapSize, maxIndex)
    }


}

module.exports.heapSort = heapSort;