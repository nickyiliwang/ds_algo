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
// var createCounter = function (init) {
//   let count = init;

//   function increment() {
//     return count++;
//   }

//   return {
//     increment: increment,
//   };
// };

// createCounter().increment();

// function counter(n) {
//   return n;
// }

// for (const i = 0; i <= 10; i++) {
//   counter(10);
// }
