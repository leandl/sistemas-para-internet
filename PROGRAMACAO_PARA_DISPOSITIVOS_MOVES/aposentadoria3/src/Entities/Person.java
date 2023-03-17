package Entities;

public class Person {
    private String name;
    private int age;
    private int workTime;
    private String sex;

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

    public int getAge() {
        return age;
    }

    /**
     * Define a age da pessoa
     * @param age
     */
    public void setAge(int age) {
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("age inválida!");
        }

        this.age = age;
    }

    public int getWorkTime() {
        return workTime;
    }

    /**
     * Define o workTime de trabalho da pessoa
     * @param workTime
     */
    public void setWorkTime(int workTime) {
        if (workTime < 0 || workTime > 100) {
            throw new IllegalArgumentException("tempo de serviço inválida!");
        }

        this.workTime = workTime;
    }

    public String getSex() {
        return sex;
    }

    /**
     * Define o sex da pessoa
     * @param sex
     */
    public void setSex(String sex) {
        if (!sex.equalsIgnoreCase("f") && !sex.equalsIgnoreCase("m")) {
            throw new IllegalArgumentException("Sexo inválida! opções: f ou m");
        }

        this.sex = sex;
    }


    public boolean isMasculine() {
        return this.getSex().equalsIgnoreCase("m");
    }

    public boolean isFeminine() {
        return this.getSex().equalsIgnoreCase("f");
    }
}
