function map(f, a){
    const result = new Array(a.length);
    for(let i = 0; i < a.length; i++ ){

        result[i] = f(a[i]);
    }
    return result;
}

const cube = function(x){
    return x * x * x;
};

const number = [2,4,5,6];

const y = function(a){
    return a;
}
console.log(map(y,number))