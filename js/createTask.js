var formulario = document.getElementById("formu");

formulario.addEventListener('submit', function(e){
    e.preventDefault();
    var datos = new FormData(formulario);

    var url = 'https://iam-managment-server.herokuapp.com/controller/addTask/'

    var envio= {
        method: "POST",
        name: datos.get('name'),
        description: datos.get('descrip'),
        start_date: datos.get('fecha'),
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