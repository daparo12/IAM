var formulario = document.getElementById("form");

formulario.addEventListener('submit', function(e){
    e.preventDefault();
    var datos = new FormData(formulario);

    var url = 'https://iam-managment-server.herokuapp.com/controller/addUser/'

    var envio= {
        method: "POST",
        name: datos.get('name'),
        last_name: datos.get('last-name'),
        phone_num: datos.get('phone'),
        email: datos.get('email'),
        password: datos.get('pass'),
        headers :{
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
            "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"

        }
    }

    fetch (url, envio).then(
        function(response) {
            console.log(response)
        }
    )
})
 