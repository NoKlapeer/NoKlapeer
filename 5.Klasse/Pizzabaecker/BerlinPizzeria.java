import Pizza.*;

public class BerlinPizzeria extends Pizzeria{
    @Override
    Pizza erstellePizza(String type) {
        if (type.equals("Berlin Salami")) {
            return new BerlinSalami();
        } else {
            return null;
        }
    }
}
