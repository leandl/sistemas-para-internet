package Entities;

public class Aposentadoria {
    static public boolean verificar(Person p) {
        if (
            p.getSexo().equalsIgnoreCase("m") &&
            p.getIdade() >= 65 &&
            p.getTempo() >= 30
        ) {
            return true;
        }

        if (
            p.getSexo().equalsIgnoreCase("f") &&
            p.getIdade() >= 60 &&
            p.getTempo() >= 25
        ) {
            return true;
        }


        return false;
    }
}
