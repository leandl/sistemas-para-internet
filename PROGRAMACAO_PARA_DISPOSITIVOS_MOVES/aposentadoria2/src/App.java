import java.util.Scanner;

import Entities.Aposentadoria;
import Entities.Person;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("--------------------------------");

        Scanner scanner = new Scanner(System.in);
        Person p1 = new Person("Leandro");

       
        while (true) {
            try {
                scanner = new Scanner(System.in);
                System.out.print("Digite a idade: ");
                p1.setIdade(scanner.nextInt());
                break;
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }

        while (true) {
            try {
                scanner = new Scanner(System.in);
                System.out.print("Digite o tempo de trabalho: ");
                p1.setTempo(scanner.nextInt());
                break;
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }

        while (true) {
            try {
                scanner = new Scanner(System.in);
                System.out.print("Digite o sexo: ");
                p1.setSexo(scanner.nextLine());
                break;
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }

        scanner.close();

        if (Aposentadoria.verificar(p1)) {
            System.out.println("Já pode aposentar!");
        } else {
            System.out.println("Ainda não pode aposentar!");
        }
    }

    public static void performAction(Runnable runnable) {
        while (true) {
            try {
                runnable.run();
                break;
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
            }
        }
    }
}
