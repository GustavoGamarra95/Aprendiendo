package aprendiendo;

import java.util.Scanner;

class VerificadorNumeroParImpar {

    public static void main(String[] args) {
        int numUsuario;
        System.out.print("Ingrese un número: ");
        Scanner scanner = new Scanner(System.in);
        numUsuario = scanner.nextInt();
        if (numUsuario % 2 == 0) {
            System.out.println(numUsuario + " es un número par.");
        } else {
            System.out.println(numUsuario + " es un número impar.");
        }
        scanner.close();
    }
}