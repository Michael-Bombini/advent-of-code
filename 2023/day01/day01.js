import fs from "fs";
const file = fs.readFileSync("input.txt", { encoding: "utf-8" });
const data = file.split("\n");

function findNumbers(row) {
  let firstNum = null;
  let lastNum;
  for (let char of row) {
    if (!isNaN(parseInt(char))) {
      if (firstNum === null) {
        firstNum = parseInt(char);
      }
      lastNum = parseInt(char);
    }
  }
  return "" + firstNum + lastNum
}
let sum = 0;
data.forEach((row) => {
  sum += parseInt(findNumbers(row));
});

console.log(sum);
