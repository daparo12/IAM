const contenedor1 = document.getElementById('contenedor1')
const contenedor2 = document.getElementById('contenedor2')
const btn = document.querySelector('.button2');


function agregarTareas(){
    
    contenedor1.innerHTML += `
            <div class="card">
                <div class="container">
                    <h4><b>John Doe</b></h4>
                    <p class="card__apply">
                    </div>
            </div>`;
}