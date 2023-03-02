import Pizza.*;

public class HamburgPizzeria extends Pizzeria{
    @Override
    protected Pizza erstellePizza(String type) {
        if (type.equals("Hamburg Hawaii")) {
            return new HamburgHawaii();
        } else {
            return null;
        }
    }
}
