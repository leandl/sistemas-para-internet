package Entities;

public class Retirement {

    static public boolean check(Person person) {
        if (
            person.isMasculine() &&
            person.getAge() >= 65 &&
            person.getWorkTime() >= 30
        ) {
            return true;
        }

        if (
            person.isFeminine() &&
            person.getAge() >= 60 &&
            person.getWorkTime() >= 25
        ) {
            return true;
        }


        return false;
    }
}
