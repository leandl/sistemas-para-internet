package Entities;

public class Moto extends Veiculo implements Eletrificado {
   
  public Moto(String nome) {
    super(nome, 2);
  }

  @Override
  public void acelerar() {
    System.out.println("Acelerar " + this.nome + " com " + this.qtdRodas + " rodas");
    this.motorEletrico();
  }

  public void acelerar(int intensidade) {
    System.out.println("intensidade da aceleração: " + intensidade);
  }

  @Override
  public void motorEletrico() {
    System.out.println("ARodando com motor elétrico");
  }
}
