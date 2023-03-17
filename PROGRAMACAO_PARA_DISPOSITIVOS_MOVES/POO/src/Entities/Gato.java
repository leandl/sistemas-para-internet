package Entities;

public class Gato extends Animal {
	public Gato() {
		super("Gato");
	}

	@Override
	public void nadar() {
		System.out.println("odeio agua");
	}
}
