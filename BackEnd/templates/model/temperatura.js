class Temperatura {
      constructor(id, temperatura, umidade) {
      this.id = id;
      this.temperatura = temperatura;
      this.umidade = umidade;
    }
  
    exibirInformacoes() {
      console.log(`ID: ${this.id}, Temperatura: ${this.temperatura}°C, Umidade: ${this.umidade}%`);
    }
  }

  export default Temperatura;