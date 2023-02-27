import Pizza.*;

public class RostockCalzone implements Pizza{
    @Override
    public void backen() {
        System.out.println("Rostock Pizza Calzone backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Rostock Pizza Calzone schneiden");
    }   
    @Override
    public void einpacken() {
        System.out.println("Rostock Pizza Calzone einpacken");
    }
}
