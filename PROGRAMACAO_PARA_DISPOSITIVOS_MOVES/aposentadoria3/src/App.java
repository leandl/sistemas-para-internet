import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import Entities.Retirement;
import Entities.Person;

public class App {

	public static List<Person> people = new ArrayList<>();
	public static Scanner scanner = new Scanner(System.in);


	public static void main(String[] args) throws Exception {

		while (true) {
			System.out.print("Qual o nome da pessoa?: ");
			String personName = scanner.nextLine();
			Person person = new Person(personName);

			registerSex(person);
			registerAge(person);
			registerTime(person);

			people.add(person);
			
			System.out.print("Gostaria de cadastrar mais uma pessoa? (s/n): ");
			char option = scanner.next().toLowerCase().charAt(0);
			if (option != 's') {
				break;
			}

			scanner = new Scanner(System.in);
		}

		printOut();
	}

	static void registerAge(Person person) {
		scanner = new Scanner(System.in);

		System.out.print("Digite a idade: ");
		int age = scanner.nextInt();
		person.setAge(age);
	}

	static void registerTime(Person person) {
		scanner = new Scanner(System.in);

		System.out.print("Digite o tempo de trabalho: ");
		int time = scanner.nextInt();
		person.setWorkTime(time);
	}

	static void registerSex(Person person) {
		scanner = new Scanner(System.in);

		System.out.print("Digite o sexo: ");
		String sex = scanner.nextLine();
		person.setSex(sex);
	}

	static void printOut() {
		for (Person person : people) {
			System.out.println("-----------------------------");
			if (Retirement.check(person)) {
				System.out.println(person.getName() + " já pode se aposentar!");
			} else {
				System.out.println(person.getName() + " não pode se aposentar!");
			};
		}
	}
}
