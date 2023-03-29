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

    public void update() {
        this.temperature = this.weatherStation.getTemperature();
        this.humidity = this.weatherStation.getHumidity();
        display();
    }

    public void display() {
        System.out.println("Temperature: " + temperature);
        System.out.println("Humidity: " + humidity);
    }
}