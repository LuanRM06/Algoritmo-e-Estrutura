const participantes = [];
let contador =  0;


document.getElementById("registroform").addEventListener('submit', function(event){
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const cpf = document.getElementById('cpf').value;
    const email = document.getElementById('email').value;
    const codigo = document.getElementById('codigo').value;

if (nome && cpf && email &&  codigo) {
    participantes.push({ nome, cpf, email, codigo});
    document.getElementById('nome').value = '';
    document.getElementById('cpf').value = '';
    document.getElementById('email').value = '';
    document.getElementById('codigo').value = '';
    alert('Participante registrado.');
    contador++
    }   
});

document.getElementById('mostrarlista').addEventListener('click', function()
{
    const lista = document.getElementById('listaparticipantes');
    lista.innerHTML = '';
    participantes.forEach(participante => {
    const li = document.createElement('li');
    li.textContent = `Nome: ${participante.nome}, CPF: ${participante.cpf}, Email: ${participante.email}, Código ${participante.codigo}`;
    this.appendChild(li);
    });
    document.getElementById('quantidadeP').innerHTML= contador;
});
