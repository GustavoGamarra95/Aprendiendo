package aprendiendo;

import java.util.Scanner;

public class calculadoraimc {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double peso, altura, imc;

        System.out.print("Ingrese su peso (en kg): ");
        peso = scanner.nextDouble();
        System.out.print("Ingrese su altura (en metros): ");
        altura = scanner.nextDouble();

        imc = peso / (altura * altura);

        System.out.println("Su IMC es: " + imc);

        if (imc < 18.5) {
            System.out.println("Clasificación: Bajo peso");
        } else if (imc >= 18.5 && imc < 25) {
            System.out.println("Clasificación: Peso normal");
        } else if (imc >= 25 && imc < 30) {
            System.out.println("Clasificación: Sobrepeso");
        } else {
            System.out.println("Clasificación: Obesidad");
        }

        scanner.close();
    }
}



