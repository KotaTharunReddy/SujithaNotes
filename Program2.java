

class Paytm {
    // this variable is publically exposed which is wrong.
    // anybody can manipulate this
    // private is used to control access of variable
    // this action is called encapsulation
    private float transactionCharge=0.05f;

    // Indirect Access to Private variable is provided
    // using Getter and Setters

    public float getTxnCharge() {
        return transactionCharge;
    }

    public void setTxnCharge(float newCharge) {
        if (newCharge < 0.05) {
            System.out.println("Invalid TxnRate, cannot be less than 5%");
            return;
        }
        transactionCharge = newCharge;
    }
}

class Amazon {
    Paytm paytm = new Paytm();
    void makePayment(int payableAmount) {
        float ActualPayable = payableAmount + (paytm.getTxnCharge()*payableAmount);
        System.out.println(ActualPayable);
    }
}

public class Program2{
    public static void main(String[] args) {
        Amazon amzn = new Amazon();
        amzn.makePayment(200);
    }
}

// therefore encapsulation helps control or restrict access
// to variable or functions using access specifiers

// when the variable is marked as private
// the variable is encapsulated in its own class.

// when the variable is marked as protected 
// the variable is encapsulated in its own class
// and in derived class

//when the variable is marked as default(no acceess modifier)
// then variable is encapsulated in all classes of same package in java

//when the variable is mareked as public is variable
// isn't encapsulated its visible/accessible to all

// we define boundaries using access modifiers
// and that boundary is called as encapsulation