let count = 0;
const simpleQsort = (arr) => {
  count++;
  if (arr.length <= 1) {
    return arr;
  }
  const pivot = arr[0];

  const arr1 = arr.filter((x) => x < pivot, arr);
  const arr2 = arr.filter((x) => x === pivot, arr);
  const arr3 = arr.filter((x) => x > pivot, arr);

  return simpleQsort(arr1).concat(arr2).concat(simpleQsort(arr3));
};

const arr = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10];
console.log(simpleQsort(arr));
console.log(count);
