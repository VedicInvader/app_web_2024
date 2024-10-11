//Esto es un comentario de una linea

/*
Comentario multilinea
en
JavaScript
*/


//alerta
//alert("Hola, ¿qué tal? Soy una alerta")

//variables
var nombre = "Marco Antonio González Espino";
let nombre2 = "Cinthia Stephany Castro Salazar";
let edad = 22;
let estatura = 1.85;
let booleano = true;


//Mostrar en consola
console.log("Hola, estoy en la consola.");
console.log("Hola, tengo "+edad+" años.");

//Mostrar en pantalla 
document.write("Hola, estoy en la pantalla. <br>");
document.write("<h2>Hola, tengo "+edad+" años.</h2>");

//Mostrar en pantalla getElementById

let datos = document.getElementById("informacion");
datos.innerHTML = "Hola, este es el contenido de innerHTML";
datos.innerHTML += "<hr><h3>Hola, soy otro contenido de innerHTML</h3>";
datos.innerHTML += "<hr><h3>Mido: "+estatura+" metros</h3>";
datos.innerHTML += `
        <br>
        <hr>
        <h1>
            Hola, soy un contenido de HTML, mi nombre es: ${nombre} <br>
            Y mi estatura es de ${estatura} metros.
        </h1>`;

//Condicionales

if (edad >= 18)
    datos.innerHTML = `
        <hr>
        Soy mayor de edad
        <hr>
`;
else
    datos.innerHTML = `
        <hr>
        Soy menor de edad
        <hr>
    `;
//Ciclos
// for (let i = 1; i <= 200; i++){
//     datos.innerHTML += `<hr><h3>El numero es ${i}</h3>`;
// }

// let i = 1;

// while (i <= 5){
//     datos.innerHTML += `<hr><h3>El numero es ${i}</h3>`;
//     i++;
// };

// i = 1;
// do{
//     datos.innerHTML += `<hr><h3>El numero es ${i}</h3>`
// }
// while (i <= 5);

/* Funciones

1. Funcion que no recibe parametros y no regresa valor

2. Funcion que no recibe parametros y regresa valor

3. Funcion que recibe parametros y no regresa valor

4. Funcion que recibe parametros y regresa valor
*/

// //1
// function suma1(){
//     let n1 = 2;
//     let n2 = 3;
//     let suma = n1 + n2;
//     datos.innerHTML += `<hr><h3>El resultado es ${suma}</h3>`;
// }

// suma1();

// //2
// function suma2(){
//     let n1 = 2;
//     let n2 = 3;
//     let suma = n1 + n2;
//     return suma;
// }

// let suma = suma2();
// datos.innerHTML += `<hr><h3>El resultado de la suma es ${suma}</h3>`;

//3
function suma3(numero1, numero2){
    let n1 = numero1;
    let n2 = numero2;
    let suma = n1 +n2;
    datos.innerHTML += `<hr><h3>El resultado de la suma es ${suma}</h3>`;
}

suma3(3, 4);

//4
function suma4(numero3, numero4){
    let n1 = numero3;
    let n2 = numero4;
    let suma = n1 +n2;
    return suma;
}
let suma2 = suma4(4, 4);
datos.innerHTML += `<hr><h3>El resultado de la suma es ${suma2}</h3>`;

//Arreglos

let animales = []
animales[0] = "Perro"
animales[1] = "Serpiente"
animales[2] = "Gato"

let animales2 = ["Tiburon", "Elefante", "Puma"]

for(i = 0; i < animales.length; i++){
    datos.innerHTML += `<hr><h3>${animales[i]}</h3>`;
}

animales2.forEach(element =>{
    datos.innerHTML += `<hr><h3>El animal es ${element}</h3>`;
});