package push;
public class Display implements Observer {
    private WeatherStation weatherStation;
    private float temperature;
    private float humidity;

    public Display(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
        this.temperature = 0;
        this.humidity = 0;
        this.weatherStation.registerObserver(this);
    }
    
    @Override
    public void update(float temperature, float humidity) {
        this.temperature = this.weatherStation.getTemperature();
        this.humidity = this.weatherStation.getHumidity();
        this.display();
    }
    
    public void display() {
        System.out.println("Temperature: " + this.temperature);
        System.out.println("Humidity: " + this.humidity);
    }
    

}