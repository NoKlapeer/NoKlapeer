import Pizza.*;

public class BerlinPizzeria extends Pizzeria{
    @Override
    protected Pizza erstellePizza(String type) {
        if (type.equals("Berlin Salami")) {
            return new BerlinSalami();
        } else {
            return null;
        }
    }
}
