package pull;

class ColorSignal implements Observer {
    private float temperature;
    private float humidity;
    private WeatherStation weatherStation;

    public ColorSignal(WeatherStation weatherStation) {
        this.weatherStation = weatherStation;
        weatherStation.registerObserver(this);
    }

    public void update(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        display();
    }

    public void display() {
        if (temperature > 30) {
            System.out.println("Red Signal");
        } else if (temperature > 15) {
            System.out.println("Yellow Signal");
        } else {
            System.out.println("Green Signal");
        }
    }
}