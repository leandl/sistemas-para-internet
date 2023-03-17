package Entities;

public class Bemtevi extends Animal implements Passaro {
  
  public Bemtevi() {
    super("bem-te-vi");
  }

  @Override
  public void nadar() {
    System.out.println("bem-te-vi nadando");
  }

  @Override
  public void voar() {
    System.out.println("voando...");
  }
  
}
