function factorial(number){
    return  number < 2 ? 1 : number * factorial(number - 1)
}

console.log(factorial(1))