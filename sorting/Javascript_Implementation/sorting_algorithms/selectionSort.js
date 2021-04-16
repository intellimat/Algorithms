const swap = require('../utils').swap;

function selectionSort(array) {
    for (i=0; i < array.length; i++){
        min_index = i
        for (j=i; j < array.length; j++)
            if (array[j] < array[min_index])
                min_index = j
        swap(array, i, min_index)
    }
}




module.exports.selectionSort = selectionSort;