import Pizza.*;

public class TestPizza{
    public static void main(String[] args){
        
        Pizzeria pizzeria = new PizzaFactory();
        Pizza pizzaquat = pizzeria.bestellePizza("QuattroStagioni");

        Pizzeria pizzeriaberlin = new BerlinPizzeria();
        Pizza pizzab = pizzeriaberlin.bestellePizza("Berlin Salami");

        Pizzeria pizzeriahamburg = new HamburgPizzeria();
        Pizza pizzah = pizzeriahamburg.bestellePizza("Hamburg Hawaii");

        Pizzeria pizzeriarostock = new RostockPizzeria();
        Pizza pizzar = pizzeriarostock.bestellePizza("Rostock Calzone");
    }
}