package Pizza;
public class CalzonePizza implements Pizza {
    @Override
    public void backen() {
        System.out.println("Pizza Calzone backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Pizza Calzone schneiden");
    }
    @Override
    public void einpacken() {
        System.out.println("Pizza Calzone einpacken");
    }
}