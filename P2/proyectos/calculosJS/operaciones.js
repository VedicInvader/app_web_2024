function operacion(){
    let n1, n2, tipo_op, resultado;
    n1 = parseFloat(document.getElementById("n1").value);
    n2 = parseFloat(document.getElementById("n2").value);
    tipo_op = document.getElementById("tipo-op").value;

    if (isNumber(n1) && isNumber(n2)){
        switch(tipo_op){
            case "sum":
                oper = n1 + n2;
                tipo = "+";
                break;
            case "res":
                oper = n1 - n2;
                tipo = "-";
                break;
            case "mult":
                oper = n1 * n2;
                tipo = "*"
                break;
            case "div":
                oper = n1 / n2;
                tipo = "/"
                break;
        }
    
        resultado = document.getElementById("resultado");
        resultado.innerHTML = `
        <hr>
        <h2>${n1} ${tipo} ${n2} = ${oper}</h2>`;
    }
    else
        alert("Ingresa sólo números.");
}

function isNumber(n){
    return ! isNaN(parseFloat(n) && isFinite(n));
}

