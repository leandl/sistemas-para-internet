package Entities;

public abstract class Veiculo {

  String nome;
  int qtdRodas;

  public Veiculo(String nome, int qtdRodas) {
    this.nome = nome;
    this.qtdRodas = qtdRodas;
  }

  public abstract void acelerar();
}
