interface Customer {
    void bookRide();
    void addWalletMoney();
    void checkRideHistory();
    void cancelRide();
    void makePayment();
}
interface Owner {
    void activateDriver();
    void removeDriver();
    void getFinanceReport();
    void addDriver();
    void setCommericalRate();
}
interface Driver {
    void confirmBooking();
    void validateOTP();
    void completeRide();
    void checkCommision();
    void setDrivingStatus();
}

    
public class Program3 implements Customer, Driver, Owner {
    public static void main(String[] args) {
        //Program3 god = new Program3(); // showing all the functionalities and hiding nothing which is bad
        // an object show not have access of all the features
        // we should learn coding with principles
        
        // so making relevant functions are only accessible is called abstraction
        // to implement abstraction we use interfaces in java
        // each interface defines a role

        //Customer ravi = new Program3();
        //Driver.prakash = new Program3();
        
    }
    // this is not advisable as main program has access all the methods
    public void activateDriver() {

    }
    public void removeDriver() {

    }
    public void getFinanceReport() {

    }
    public void addDriver() {

    }
    public void setCommericalRate() {

    }
    public void bookRide() {

    }
    public void addWalletMoney() {

    }
    public void checkRideHistory() {

    }
    public void cancelRide() {

    }
    public void makePayment() {

    }
    public void confirmBooking() {

    }
    public void validateOTP() {

    }
    public void completeRide() {

    }
    public void checkCommision() {

    }
    public void setDrivingStatus() {

    }
}
