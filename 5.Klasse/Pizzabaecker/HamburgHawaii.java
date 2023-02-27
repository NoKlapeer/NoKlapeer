import Pizza.*;

public class HamburgHawaii implements Pizza{
    @Override
    public void backen() {
        System.out.println("Hamburg Pizza Hawaii backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Hamburg Pizza Hawaii schneiden");
    }   
    @Override
    public void einpacken() {
        System.out.println("Hamburg Pizza Hawaii einpacken");
    }
}
