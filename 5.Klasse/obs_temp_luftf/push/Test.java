package push;
public class Test {
    public static void main(String[] args) {
        WeatherStation weatherStation = new WeatherStation();
        Display display = new Display(weatherStation);
        ColorSignal colorSignal = new ColorSignal(weatherStation);
    
        weatherStation.setMeasurements(20, 60);
    
    }
}
