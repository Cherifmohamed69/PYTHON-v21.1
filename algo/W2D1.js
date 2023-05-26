// function removeDup
// Given an array of integers, remove duplicates
var arr = ["hello"]
function removeDup(arr) {
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (newArr.indexOf(arr[i]) === -1) {
      newArr.push(arr[i]);
    }
  }
  return newArr;
}

console.log(call(arr))

