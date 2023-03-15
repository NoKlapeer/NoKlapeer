package pull;

class Display implements Observer {
    private WeatherStation weatherStation;
    private float temperature;
    private float humidity;

    public Display(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
        this.temperature = 0;
        this.humidity = 0;
        weatherStation.registerObserver(this);
    }

    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    public void display() {
        System.out.println("Temperature: " + temperature);
        System.out.println("Humidity: " + humidity);
    }
}