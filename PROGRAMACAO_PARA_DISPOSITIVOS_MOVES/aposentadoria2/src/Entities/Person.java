package Entities;

public class Person {
    private String name;
    private int idade;
    private int tempo;
    private String sexo;

    public Person() {
        System.out.println("Nova pessoa Anônima!");
    }

    public Person(String name) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    /**
     * Define o nome da pessoa 
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    public int getIdade() {
        return idade;
    }

    /**
     * Define a idade da pessoa
     * @param idade
     */
    public void setIdade(int idade) {
        if (idade < 0 || idade > 150) {
            throw new IllegalArgumentException("Idade inválida!");
        }

        this.idade = idade;
    }

    public int getTempo() {
        return tempo;
    }

    /**
     * Define o tempo de trabalho da pessoa
     * @param tempo
     */
    public void setTempo(int tempo) {
        if (tempo < 0 || tempo > 100) {
            throw new IllegalArgumentException("Tempo de serviço inválida!");
        }

        this.tempo = tempo;
    }

    public String getSexo() {
        return sexo;
    }

    /**
     * Define o sexo da pessoa
     * @param sexo
     */
    public void setSexo(String sexo) {
        if (!sexo.equalsIgnoreCase("f") && !sexo.equalsIgnoreCase("m")) {
            throw new IllegalArgumentException("Sexo inválida! opções: f ou m");
        }

        this.sexo = sexo;
    }
}
