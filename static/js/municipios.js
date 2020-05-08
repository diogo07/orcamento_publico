
function buscarMunicipios() {
    console.log('teste');
    let filtro = document.getElementById('campo_buscar').value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText);
      }
    };
    xhttp.open("GET", "http://127.0.0.1/api/municipio/"+filtro, true);
    xhttp.send();
}