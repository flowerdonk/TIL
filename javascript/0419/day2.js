// 매개변수보다 인자의 개수가 적을 경우(매개변수와 인자의 불일치 허용)
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

threeArgs()

// Spread syntac (Rest parameters)
const restArgs = function(arg1, arg2, ...restArgs){
  return [arg1, arg2, restArgs]
}

restArgs(1, 2, 3, 4, 5)

const arrow = (a, b) => {
  let ans = 0
  for (let i = 0; i < a; i++){
    ans += i
  }
  return ans + b
}

const colors = ['red', 'blue', 'green']

printFunc = function (color){
  console.log(color)
}

colors.forEach(printFunc)

const nums = [1, 2, 3, 4]

const sq = function (num){
  return num * num
}

const sqnums = nums.map(sq)
console.log(sqnums)

for (let i = 0; i < 5; i++){
  for (let blank = 1; blank < 5 - i; blank++){
    console.log(' ')
  }
  for (let star = 1; star < 2 * i + 2; star++){
    console.log('*')
  }
}

for (let blank = 1; blank < 5; blank++){
  console.log(' ')
}
for (let star = 1; star < 2; star++){
  console.log('*')
}