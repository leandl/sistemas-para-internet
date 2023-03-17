package Entities;

public class Carro extends Veiculo {
  
  public Carro(String nome) {
    super(nome, 4);
  }

  @Override
  public void acelerar() {
    System.out.println("Acelerar " + this.nome + " com " + this.qtdRodas + " rodas");
  }

  public void acelerar(int intensidade) {
    System.out.println("intensidade da aceleração: " + intensidade);
  }

}
