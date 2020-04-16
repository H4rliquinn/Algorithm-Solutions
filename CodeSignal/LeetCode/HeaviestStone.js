/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) { 
    // sorted array let sortedArray
    let sortedArray = stones.sort((a, b) => a-b)
    // Keep track of where the largest ones are
    // while loop so that length of array > 1
    while(sortedArray.length > 1) {
        let largest = sortedArray[sortedArray.length-1]
        let second = sortedArray[sortedArray.length-2]
    // Compare them
    // If they're the same, both are totally "destroyed" - pop() pop()
        if(largest === second) {
            sortedArray.pop()
            sortedArray.pop()
        } else {
            // pop and push the difference
            sortedArray.push(sortedArray.pop()- sortedArray.pop())
            //resort
            sortedArray.sort((a, b) => a-b)
        }
    }
    // edge case where length === 0 return 0
    if(sortedArray.length === 0) return 0
    // return sorted_array[0]
     return sortedArray[0]
};