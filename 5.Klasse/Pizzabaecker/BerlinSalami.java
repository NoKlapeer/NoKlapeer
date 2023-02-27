import Pizza.*;

public class BerlinSalami implements Pizza{
    @Override
    public void backen() {
        System.out.println("Berlin Pizza Salami backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Berlin Pizza Salami schneiden");
    }   
    @Override
    public void einpacken() {
        System.out.println("Berlin Pizza Salami einpacken");
    }
}
