import fs from "fs";
const file = fs.readFileSync("input.txt", { encoding: "utf-8" });
const data = file.split("\n");

function main() {
  let idSum = 0;
  data.forEach((line, id) => {
    const games = line.split(": ")[1];
    const game = games.split(";");
    let maxRed = 0;
    let maxGreen = 0;
    let maxBlue = 0;
    game.forEach((turn) => {
      const cubes = turn.split(",");
      cubes.forEach((cube) => {
        const number = cube.replace(/[^0-9]/g, "");
        if (cube.includes("red")) maxRed = Math.max(maxRed, parseInt(number));
        if (cube.includes("green")) maxGreen = Math.max(maxGreen, parseInt(number));
        if (cube.includes("blue")) maxBlue = Math.max(maxBlue, parseInt(number));
      });
    });
    // here is the end of a single game
    if (maxRed <= 12 && maxGreen <= 13 && maxBlue <= 14) idSum += id + 1;
  });
  console.log(idSum);
}

main();
