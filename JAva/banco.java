package aprendiendo;

import java.util.Scanner;
import Account.Account;

public class Main {
    public static void test(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Account account = null;

        boolean sair = false;
        while (!sair) {
            System.out.println("Escolha uma opção:");
            System.out.println("1. Criar nova conta");
            System.out.println("2. Ver saldo");
            System.out.println("3. Depositar");
            System.out.println("4. Sacar");
            System.out.println("5. Ver limite");
            System.out.println("6. Sair");

            int opcao = scanner.nextInt();
            switch (opcao) {
                case 1:
                    System.out.println("Digite o saldo inicial da conta:");
                    double saldoInicial = scanner.nextDouble();
                    System.out.println("Digite o limite da conta:");
                    double limite = scanner.nextDouble();
                    scanner.nextLine(); // Limpar o buffer
                    System.out.println("Digite a agência da conta:");
                    String agencia = scanner.nextLine();
                    account = new Account(saldoInicial, limite, agencia);
                    System.out.println("Conta criada com sucesso!");
                    break;
                case 2:
                    if (account != null) {
                        System.out.println("Saldo: " + account.getBalance());
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 3:
                    if (account != null) {
                        System.out.println("Digite o valor para depositar:");
                        double valorDeposito = scanner.nextDouble();
                        account.deposit(valorDeposito);
                        System.out.println("Depósito realizado com sucesso!");
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 4:
                    if (account != null) {
                        System.out.println("Digite o valor para sacar:");
                        double valorSaque = scanner.nextDouble();
                        account.withdraw(valorSaque);
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 5:
                    if (account != null) {
                        System.out.println("Limite: " + account.getLimit());
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 6:
                    sair = true;
                    break;
                default:
                    System.out.println("Opção inválida!");
                    break;
            }
        }

        scanner.close();
    }
}