// ## Sliding window

// 1. creating a window which can either be an array or number from one position to another
// 2. Depending on conditions, the window either increases or closes, and a new window is created

// Good for:
// keeping track of a subset of data in an array/string

function maxSubArraySum(arr, num) {
  let maxSum = 0;
  let tempSum = 0;
  if (arr.length < num) return null;

  for (let i = 0; i < num; i++) {
    maxSum += arr[i];
  }
  //   we get the initial window
  // 1, 2, 3 => 6
  // tempSum will start as 6

  tempSum = maxSum;

  for (let i = num; i < arr.length; i++) {
    // for each new number, subtract the old number
    // [1,2,3] => [2,3,4]
    // tempSum = 6 - 1 + 4
    // tempSum = maxSum starting point - arr[3 - 3] + arr[3]
    tempSum = tempSum - arr[i - num] + arr[i];

    // reassign the maxSum with the larger of the two
    maxSum = Math.max(maxSum, tempSum);
  }
  return maxSum;
}

console.log(maxSubArraySum([1, 2, 3, 4, 5, 6, 7], 3));
