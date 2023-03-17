import Entities.Carro;
import Entities.Moto;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("=================================");
        Moto moto = new Moto("bob fat");
        moto.acelerar();
        moto.acelerar(120);
        
        System.out.println("-------------------------------");
        Carro carro = new Carro("Gol");
        carro.acelerar();
        carro.acelerar(100);
    }
}
