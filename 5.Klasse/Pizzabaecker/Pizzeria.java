import Pizza.*;

public abstract class Pizzeria {
    public Pizza bestellePizza(String type){
        Pizza pizza = erstellePizza(type);
        pizza.backen();
        pizza.schneiden();
        pizza.einpacken();
        return pizza;
    }

    abstract Pizza erstellePizza(String type);
}