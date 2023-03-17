import Entities.Bemtevi;
import Entities.Cachorro;
import Entities.Gato;
import Entities.Passaro;

public class App {
	public static void main(String[] args) throws Exception {
		Cachorro cachorro = new Cachorro();
		cachorro.patas = 4;
		cachorro.correr();
		cachorro.nadar();

		Gato gato = new Gato(); 
		gato.peso = 5.5;
		gato.correr();
		gato.nadar();

		Bemtevi bemtevi = new Bemtevi();
		bemtevi.patas = 4;
		bemtevi.correr();
		bemtevi.nadar();
		bemtevi.voar();

		System.out.println(Passaro.asas);


	}
}
