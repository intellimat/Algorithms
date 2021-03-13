const readline = require('readline');


/* 
    We place:
    # s1 as the vertical string
    # s2 as the horizontal string
*/
function getInitialMatrix(s1,s2) {
    let D = []; // matrix
    let numberOfRows = s1.length + 1;
    let numberOfCols = s2.length + 1;

    let firstRow = [];
    for (let j=0; j < numberOfCols; j++) {
        firstRow.push(j);
    }
    D.push(firstRow)

    // Initialize empty matrix
    for (let i=1; i < numberOfRows; i++) { 
        row = [i];
        for(let k=1; k < numberOfCols; k++)
            row.push('');
        D.push(row);
    }
    
    return D;
}

// returns the minimum value between args
function getMin(...args){
    min = args[0];
    for (let value of args)
        if (value < min) 
            min = value;
    return min;
}

function getEditDistance(s1,s2) {
    // s1 vertical string, s2 horizontal string
    D = getInitialMatrix(s1,s2);
    
    numberOfRows = s1.length + 1;
    numberOfCols = s2.length + 1;

    for (j=1; j < numberOfCols; j++)
        for (i=1; i < numberOfRows; i++){
            insertion = D[i][j-1] + 1;
            deletion  = D[i-1][j] + 1;
            match     = D[i-1][j-1];
            mismatch  = D[i-1][j-1] + 1;
            if (s1[i-1] === s2[j-1]) 
                D[i][j] = getMin(insertion,deletion,match);
            else
                D[i][j] = getMin(insertion,deletion,mismatch);
        }
    return D[numberOfRows-1][numberOfCols-1];
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

    
var list = [];
rl.on('line', (input) => {
    list.push(input);
    if (list.length > 1){
        let s1 = list[0];
        let s2 = list[1];
        rl.close();
        let editDistance = getEditDistance(s1,s2);
        console.log(editDistance);
    }
});