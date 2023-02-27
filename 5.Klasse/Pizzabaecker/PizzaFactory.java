import Pizza.*;

public class PizzaFactory {
    public Pizza erstellePizza(String type){
		Pizza pizza=null;
		if (type.equals("Salami"))
			pizza = new SalamiPizza();
		else if (type.equals("Hawaii"))
			pizza = new HawaiiPizza();
		else if (type.equals("Calzone"))
			pizza = new CalzonePizza();
        else if (type.equals("QuattroStagioni"))
			pizza = new QuattroStagioniPizza();
		
		return pizza;
	}

    }