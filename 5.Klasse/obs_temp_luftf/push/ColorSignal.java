package push;
public class ColorSignal implements Observer {
    private final WeatherStation weatherStation;
    private double temperature;

    public ColorSignal(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
        this.temperature = 0.0;
        this.weatherStation.registerObserver(this);
    }
    
    @Override
    public void update(float temperature, float humidity) {
        this.temperature = this.weatherStation.getTemperature();
        this.display();
    }
    
    public void display() {
        if (this.temperature > 30) {
            System.out.println("Red Signal");
        } else if (this.temperature > 15) {
            System.out.println("Yellow Signal");
        } else {
            System.out.println("Green Signal");
        }
    }
    
}