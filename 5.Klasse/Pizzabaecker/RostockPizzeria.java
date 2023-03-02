import Pizza.*;

public class RostockPizzeria extends Pizzeria{
    @Override
    protected Pizza erstellePizza(String type) {
        if (type.equals("Rostock Calzone")) {
            return new RostockCalzone();
        } else {
            return null;
        }
    }
}
