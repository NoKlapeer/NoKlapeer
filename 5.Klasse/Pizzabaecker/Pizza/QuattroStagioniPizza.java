package Pizza;
public class QuattroStagioniPizza implements Pizza {
    @Override
    public void backen() {
        System.out.println("Pizza QuattroStagioni backen");
    }
    @Override
    public void schneiden() {
        System.out.println("Pizza QuattroStagioni schneiden");
    }
    @Override
    public void einpacken() {
        System.out.println("Pizza QuattroStagioni einpacken");
    }
}