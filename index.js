// Função para adicionar um item à lista não ordenada
function addItemNaoOrdenada() {
    const listaNaoOrdenada = document.getElementById("listaNaoOrdenada");
    const novoItem = document.createElement("li");
    novoItem.textContent = "Novo Item Não Ordenado";
    listaNaoOrdenada.appendChild(novoItem);
  }
  
  // Função para adicionar um item à lista ordenada
  function addItemOrdenada() {
    const listaOrdenada = document.getElementById("listaOrdenada");
    const novoItem = document.createElement("li");
    novoItem.textContent = "Novo Item Ordenado";
    listaOrdenada.appendChild(novoItem);
  }
  