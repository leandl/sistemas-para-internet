package Entities;

public class Cachorro extends Animal {
	public Cachorro() {
		super("Cachorro");
	}

	@Override
	public void nadar() {
		System.out.println("nadando...");
	}
}
