function check() {
    console.log("check check");
}

let equation = '';

function appendToEquation(value) {
    equation += value;
    document.getElementById('equation').value = equation;
    console.log(equation);
}

function clearEquation() {
    equation = '';
    document.getElementById('equation').value = equation;
    console.log(equation)
}

function remove() {
    if (equation.length == 1) {
        clearEquation()
    } else {
        equation = equation.slice(0,-1);
    }
    document.getElementById('equation').value = equation;
    console.log(equation)
}

function calculate() {
    $.ajax({
        url: '/calculate',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ equation: equation }),
        success: function(response) {
            console.log('Response from server:', response);
            let result = response.result
            document.getElementById('equation').value = result;
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
        }
    });
}


