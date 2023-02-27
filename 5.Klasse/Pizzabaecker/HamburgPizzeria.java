import Pizza.*;

public class HamburgPizzeria extends Pizzeria{
    @Override
    Pizza erstellePizza(String type) {
        if (type.equals("Hamburg Hawaii")) {
            return new HamburgHawaii();
        } else {
            return null;
        }
    }
}
