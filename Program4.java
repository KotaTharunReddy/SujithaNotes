import java.util.*;
// public class Program4 {
//     void add(int n1, int n2 ) {System.out.println(n1+n2);}
//     void add(int n1, int n2, int n3) {System.out.println(n1+n2+n3);}
//     void add(float n1, float n2) {System.out.println(n1+n2);}
//     void add(int n1, float n2) {System.out.println(n1+n2);}
//     void add(float n1,int n2) {System.out.println(n1+n2);}

//     public static void main(String[] args) {
        
//     }
// }
// 3 rules:
// 1. count of parameters must be different
// 2. type of parameters must be different
// 3. sequence of parameters must be different

class Doctor {
    void treat() {
        System.out.println("I Treat Patients");
    }
}
class Physician extends Doctor {
    public void treat() {
        System.out.println("I Treat using Medicine");
    }
}
class Surgeon extends Doctor {
    public void treat() {
        System.out.println("I Treat using surgery");
    }
}
class Dentist extends Doctor {
    public void treat() {
        System.out.println("I treat Dental Issues");
    }
}
public class Program4 {
    public static void main(String[] args) {
        System.out.println("press 1 for physician, press 2 for surgean, press 3 for Dentist ");
        int choice = new java.util.Scanner(System.in).nextInt();
        Doctor doc=null;

        if(choice==1) { 
            doc = new Physician();
        }
        else if (choice == 2 ) {
            doc = new Surgeon();

        }
        else if (choice==3) {
            doc = new Dentist();
        }
        else {
            doc = new Doctor();
        }
        doc.treat();
    }
}