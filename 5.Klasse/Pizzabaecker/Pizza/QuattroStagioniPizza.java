package Pizza;
public class QuattroStagioniPizza implements Pizza {
    @Override
    public void backen() {
        System.out.println("Pizza QuattroStagioni Calzone backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Pizza QuattroStagioni Calzone schneiden");
    }
    @Override
    public void einpacken() {
        System.out.println("Pizza QuattroStagioni Calzone einpacken");
    }
}