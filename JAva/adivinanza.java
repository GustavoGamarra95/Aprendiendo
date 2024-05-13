package aprendiendo;

import java.util.Random;
import java.util.Scanner;

public class adivinanza {

    public static void main(String[] args) {
        Random random = new Random();
        int numeroSecreto = random.nextInt(100) + 1;
        int guess;

        Scanner scanner = new Scanner(System.in);

        do {
            System.out.print("Digita tu expectativa (1 a 100): ");
            guess = scanner.nextInt();

            if (guess == numeroSecreto) {
                System.out.println("¡Felicidades! Acertaste el número secreto");
                break;
            } else if (guess < numeroSecreto) {
                System.out.println("Tu expectativa fue menor que el número secreto");
            } else {
                System.out.println("Tu expectativa fue mayor que el número secreto");
            }
        } while (guess != numeroSecreto);

        scanner.close();
    }
}
