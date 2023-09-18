var apple_price = 200;
var orange_price = 150;

var harry_money = 1000;

function total_khoroj(apple_kg, orange_kg){
    var total = apple_kg * apple_price + orange_kg * orange_price;
    return total;
}


var total_khoroj_amount = total_khoroj(1, 1);

function total_back_mony(person_mony){ 
    var back_money = person_mony - total_khoroj_amount ;
    return back_money

}

var result = total_back_mony(harry_money)

console.log(result)
