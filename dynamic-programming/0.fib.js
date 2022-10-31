const classicFib = (n) => {
  if (n <= 2) return 1;
  return classicFib(n - 1) + classicFib(n - 2);
};

// console.log(classicFib(50));

// 1, 2, 3, 4, 5, 6,
// 1, 1, 2, 3, 5, 8

// exponential time complexity
// Time O(2 ^ n)
// Space O(n)

// meaning we are splitting each number n level of times
// and each level has exponentially growing splitting of values of 2
// 1, 2, 4, 8, 16 <= 5 levels, this is a problem if we are doing fib(50)
//                      5
//                     / \
//                    4   4
//                   / \ / \
//                  3  3 3  3
//                 ...

// Also one of the major problem with this recursive function is that it's stateless
// However many of the calculations actions were once done
// therefore we can implement a memo

const memoFib = (n, memo = {}) => {
  console.log(memo);
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  // we are passing the OG memo obj into the recursive fn
  memo[n] = memoFib(n - 1, memo) + memoFib(n - 2, memo);
  return memo[n];
};
// for memoFib(6) we can get a memo of up to:
// { '3': 2, '4': 3, '5': 5 }
console.log(memoFib(50));

// by using a memoized object we effectively brought the time complexity down to linear
// time: O(n)
// Space: O(n)
