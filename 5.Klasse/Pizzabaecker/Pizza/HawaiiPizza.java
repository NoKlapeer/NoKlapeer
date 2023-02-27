package Pizza;
public class HawaiiPizza implements Pizza {
    @Override
    public void backen() {
        System.out.println("Pizza Hawaii backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Pizza Hawaii schneiden");
    }
    @Override
    public void einpacken() {
        System.out.println("Pizza Hawaii einpacken");
    }
}