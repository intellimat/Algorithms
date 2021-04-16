function mergeSort(array) {
    if (Array.isArray(array))
        mergeSort_recursive(array, 0, array.length-1)
}

function mergeSort_recursive(array, left, right) {
    if (left < right){
        let mid = Math.floor((left + right) / 2) 

        mergeSort_recursive(array, left, mid)
        mergeSort_recursive(array, mid + 1, right)

        merge(array, left, mid, right)
    }
}


function merge(array, l, mid, r) {
    let A = []
    let B = []

    for ( let i=l; i <= mid; i++ )
        A.push(array[i])

    for ( let j=mid+1; j <= r; j++ )
        B.push(array[j])

    let i = 0     // i points to the first element of the left side array
    let j = 0     // j points to the first element of the right side array

    for ( k=l; i < A.length && j < B.length; k++ ) {
        if (A[i] <= B[j]){
            array[k] = A[i]
            i++
        } else {
            array[k] = B[j]
            j++
        }
    }

    // writing the remaining elements if the two arrays have different size
    while (k <= r && i < A.length) {
        array[k] = A[i]
        i++
        k++
    }

    // writing the remaining elements if the two arrays have different size
    while (k <= r && j < B.length) {
        array[k] = B[j]
        j++
        k++
    }


}

module.exports.mergeSort = mergeSort;