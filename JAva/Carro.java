package aprendiendo;

public class Carro {

    private String marca;
    private String modelo;
    private int ano;
    private double valor;

    // Getters
    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public int getAno() {
        return ano;
    }

    public double getValor() {
        return valor;
    }

    // Setters
    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }
}
public class CarroComArrayList {

    public static void main(String[] args) {

        // Criação de um ArrayList de Carros
        ArrayList<Carro> carros = new ArrayList<>();

        // Inserindo dados nos Carros (Tempo de Projeto)
        carros.add(new Carro("Fiat", "Mobi", 2020, 45000.00));
        carros.add(new Carro("Volkswagen", "Gol", 2021, 55000.00));
        carros.add(new Carro("Ford", "Ka", 2022, 60000.00));

        // Imprimindo informações dos Carros
        for (Carro carro : carros) {
            System.out.println("Marca: " + carro.getMarca());
            System.out.println("Modelo: " + carro.getModelo());
            System.out.println("Ano: " + carro.getAno());
            System.out.println("Valor: " + carro.getValor());
            System.out.println("-----------------------");
        }
    }
}
import java.util.Scanner;

public class CarroComArrayListTempoExecucao {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Criação de um ArrayList de Carros
        ArrayList<Carro> carros = new ArrayList<>();

        // Variável para controlar o número de carros
        int numeroCarros;

        System.out.println("Quantos carros deseja cadastrar?");
        numeroCarros = scanner.nextInt();

        // Cadastro dos Carros (Tempo de Execução)
        for (int i = 0; i < numeroCarros; i++) {
            System.out.println("Carro " + (i + 1) + ":");

            System.out.print("Marca: ");
            String marca = scanner.next();

            System.out.print("Modelo: ");
            String modelo = scanner.next();

            System.out.print("Ano: ");
            int ano = scanner.nextInt();

            System.out.print("Valor: ");
            double valor = scanner.nextDouble();

            carros.add(new Carro(marca, modelo, ano, valor));
        }

        // Imprimindo informações dos Carros
        for (Carro carro : carros) {
            System.out.println("Marca: " + carro.getMarca());
            System.out.println("Modelo: " + carro.getModelo());
            System.out.println("Ano: " + carro.getAno());
            System.out.println("Valor: " + carro.getValor());
            System.out.println("-----------------------");
        }
    }
}
