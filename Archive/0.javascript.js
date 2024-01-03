var createCounter = function (init) {
  let count = init;

  function increment() {
    return count++;
  }

  return {
    increment: increment,
  };
};

createCounter().increment();

// function counter(n) {
//   return n;
// }

// for (const i = 0; i <= 10; i++) {
//   counter(10);
// }
