/**
 * @param {number[]} stones
 * @return {number}
 */

//Using Splice to try to make it sorting faster than re-sorting the whole array
//Faster than 91.5% of other solutions
var lastStoneWeight = function(stones) { 
    let sortedArray = stones.sort((a, b) => a-b)
    while(sortedArray.length > 1) {
        if(sortedArray[sortedArray.length-1] === sortedArray[sortedArray.length-2]) {
            sortedArray=sortedArray.slice(0,sortedArray.length-2)
        } else {
            let val=sortedArray.pop() - sortedArray.pop()
            let i=0;
            while (sortedArray[i]<val){
                i++;    
            }
            sortedArray.splice(i,0,val);
        }
    }
    if(sortedArray.length === 0) return 0;
    return sortedArray[0];  
};


//My Version
// var lastStoneWeight = function(stones) { 
//     let sortedArray = stones.sort((a, b) => a-b)
//     while(sortedArray.length > 1) {
//         if(sortedArray[sortedArray.length-1] === sortedArray[sortedArray.length-2]) {
//             sortedArray=sortedArray.slice(0,sortedArray.length-2)
//         } else {
//             sortedArray.push(sortedArray.pop()- sortedArray.pop())
//             sortedArray.sort((a, b) => a-b)
//         }
//     }
//     if(sortedArray.length === 0) return 0;
//     return sortedArray[0];  
// };


// Class version

// var lastStoneWeight = function(stones) { 
//     // sorted array let sortedArray
//     let sortedArray = stones.sort((a, b) => a-b)
//     // Keep track of where the largest ones are
//     // while loop so that length of array > 1
//     while(sortedArray.length > 1) {
//         let largest = sortedArray[sortedArray.length-1]
//         let second = sortedArray[sortedArray.length-2]
//     // Compare them
//     // If they're the same, both are totally "destroyed" - pop() pop()
//         if(largest === second) {
//             sortedArray.pop()
//             sortedArray.pop()
//         } else {
//             // pop and push the difference
//             sortedArray.push(sortedArray.pop()- sortedArray.pop())
//             //resort
//             sortedArray.sort((a, b) => a-b)
//         }
//     }
//     // edge case where length === 0 return 0
//     if(sortedArray.length === 0) return 0
//     // return sorted_array[0]
//      return sortedArray[0]
// };