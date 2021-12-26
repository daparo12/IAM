const login = document.querySelector('.button');
var formulario = document.getElementById("formularioI");

login.addEventListener('click',()=>{
    alert('click')

    var url = 'https://iam-managment-server.herokuapp.com/controller/authUser/'

    var envio= {
        method: "POST",
        email: datos.get('email'),
        password: datos.get('pass'),
        headers :{
            'Access-Control-Allow-Origin': "http://127.0.0.1:5500",
            'Access-Control-Allow-Credentials': true
        }
    }

    fetch (url, envio).then(
        function(response) {
            console.log(response)
        }
    )
})


