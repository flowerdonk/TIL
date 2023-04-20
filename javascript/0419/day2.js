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

// forEach 연습
const colors = ['red', 'blue', 'green']

printFunc = function (color){
  console.log(color)
}

colors.forEach(printFunc)


// 3제곱 구하기
const nums = [1, 2, 3, 4]

const sq = function (num){
  return num * num
}

const sqnums = nums.map(sq)
console.log(sqnums)


// 피라미드 별 찍기
for (let i = 0; i < 5; i++){
  for (let blank = 1; blank < 5 - i; blank++){
    console.log(' ')
  }
  for (let star = 1; star < 2 * i + 2; star++){
    console.log('*')
  }
}

const inputs = [
  [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
  [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
  [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
]

function solution(K, N, M, chargers) {
  // solution 함수 완성
  let start = 0
  let idx = 0
  while (start < N){
    if (start + K == chargers[idx]){
      start += K
      idx += 1
    }
    else if(){
      
    }
  }
}

for (const input of inputs) {
  solution(input[0], input[1], input[2], input[3])
}