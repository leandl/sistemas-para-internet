import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();

        System.out.print("Digite o tempo de serviço: ");
        int tempo = scanner.nextInt();

        System.out.print("Digite seu sexo (m/f): ");

        scanner = new Scanner(System.in);
        String sexo = scanner.nextLine();       

        if (sexo.equalsIgnoreCase("m")) {
            if (idade >= 65 && tempo >= 30) {
                System.out.println("Já pode se aposentar");
            } else {
                System.out.println("Ainda não pode se aposentar");
            }
        } else if (sexo.equalsIgnoreCase("f")) {
            if (idade >= 60 && tempo >= 25) {
                System.out.println("Já pode se aposentar");
            } else {
                System.out.println("Ainda não pode se aposentar");
            }
        } else {
            System.out.println("Dados inválidos");
        }


        scanner.close();

    }
}