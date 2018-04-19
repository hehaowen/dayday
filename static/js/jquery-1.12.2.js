var price = document.getElementsByClassName('show_pirze')[0].getElementsByTagName('em')[0];
var allPrice = document.getElementsByClassName('total')[0].getElementsByTagName('em')[0];
var getNum = document.getElementsByClassName("num_show")[0];
var allNum = document.getElementsByClassName("num_name")[0].getElementsByTagName('span')[0];

function getInputNum() {
    if (getNum.value < allNum.innerHTML) {
        getNum = document.getElementsByClassName("num_show")[0];
        allPrice.innerHTML = (Number(getNum.value) * Number(price.innerHTML)).toFixed(2);
    } else {
        alert("")
    }

}

function addNum() {
    if (getNum.value < allNum.innerHTML) {
        getNum.value = Number(getNum.value) + 1;
        allPrice.innerHTML = (Number(getNum.value) * Number(price.innerHTML)).toFixed(2);
    } else {
        alert("")
    }
}

function minusNum() {
    if (getNum.value < 1) {
        getNum.value = 0;
    } else {
        getNum.value = Number(getNum.value) - 1;
    }
    allPrice.innerHTML = (Number(getNum.value) * Number(price.innerHTML)).toFixed(2);
}