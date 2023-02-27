package Pizza;
public class SalamiPizza implements Pizza {
    @Override
    public void backen() {
        System.out.println("Pizza Salami backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Pizza Salami schneiden");
    }   
    @Override
    public void einpacken() {
        System.out.println("Pizza Salami einpacken");
    }
}