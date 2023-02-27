import Pizza.*;

public class RostockPizzeria extends Pizzeria{
    @Override
    Pizza erstellePizza(String type) {
        if (type.equals("Rostock Calzone")) {
            return new RostockCalzone();
        } else {
            return null;
        }
    }
}
