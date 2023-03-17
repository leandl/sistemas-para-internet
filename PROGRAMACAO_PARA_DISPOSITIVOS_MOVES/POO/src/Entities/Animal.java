package Entities;

public abstract class Animal {
	public String cor;
	public int patas;
	public String raca;
	public double peso;

	public Animal(String type) {
		System.out.println("Novo " + type);
	}

	public void correr() {
		System.out.println("Correndo...");
	}

	public abstract void nadar();
}
