const mergeSort        = require('./sorting_algorithms/mergeSort').mergeSort;
const quickSort        = require('./sorting_algorithms/quickSort').quickSort;
const heapSort         = require('./sorting_algorithms/heapSort').heapSort;
const selectionSort    = require('./sorting_algorithms/selectionSort').selectionSort;
const getRandomInteger = require('./utils').getRandomInteger;
const ask              = require('./utils').ask;
const myArgs           = process.argv.slice(2);

function testSortingAlgorithm(sortingAlgorithm, numOfTests=1000, maxArrayLength=1000, maxElementValue=10000) {
    for (n = 1; n < numOfTests + 1; n++) {
        A = []
        B = []
        arrayLength = getRandomInteger(0, maxArrayLength)

        for (i = 0; i < arrayLength; i++) {
            value = getRandomInteger(0, maxElementValue)
            A.push(value)
            B.push(value)
        }
        
        A.sort( (a,b) => a-b)
        sortingAlgorithm(B)

        if (A.length != B.length) {
            console.log(`TEST ${n} FAILED \n`)
            console.log('Size is not equal. ')
            return 1
        } else
            for (j=0; j< A.length; j++)
                if (B[j] != A[j]){
                    console.log(`TEST ${n} FAILED \n`)
                    console.log(`modelSolution[${j}] = ${A[j]}`)
                    console.log(`${sortingAlgorithm.name}Solution[${j}] = ${B[j]}`)
                    return 1
                }
            console.log(`TEST ${n} PASSED \n`)
    }

    return 0
}

async function main() {
    algorithms = {
        quicksort: quickSort,
        mergesort: mergeSort,
        heapsort: heapSort,
        selectionsort: selectionSort
    }

    algorithmName =  myArgs[0].toLowerCase();

    if (!algorithms[algorithmName]) {
        console.log(`\nWrong algorithm name given. No algorithm with the name '${algorithmName}' has been implemented. \n`)
        return 
    }

    numOfTests         = parseInt(await ask(`How many tests do you want to run on ${algorithmName}()? `));
    maximumArrayLength = parseInt(await ask('Size of the largest array to test? '));
    maxElementValue    = parseInt(await ask('Largest value stored in the testing arrays? '));

    testOutcome = testSortingAlgorithm(algorithms[algorithmName], numOfTests, maximumArrayLength, maxElementValue);

    if (testOutcome === 0)
        console.log('\nALL TESTS PASSED!\n')
    else if (testOutcome === 1)
        console.log('\nOH NO! AT LEAST ONE TEST FAILED!\n')

}

main();

module.exports.testSortingAlgorithm = testSortingAlgorithm;