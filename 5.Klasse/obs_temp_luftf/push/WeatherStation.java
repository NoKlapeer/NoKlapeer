package push;
import java.util.ArrayList;

public class WeatherStation {
    private float temperature;
    private float humidity;
    private ArrayList<Observer> observers;

    public WeatherStation() {
        this.temperature = 0;
        this.humidity = 0;
        this.observers = new ArrayList<>();
    }
    
    public void registerObserver(Observer observer) {
        this.observers.add(observer);
    }
    
    public void removeObserver(Observer observer) {
        this.observers.remove(observer);
    }
    
    public void notifyObservers() {
        for (Observer observer : this.observers) {
            observer.update(temperature, humidity);
        }
    }
    
    public void setMeasurements(float temperature, float humidity) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.notifyObservers();
    }
    
    public float getTemperature() {
        return temperature;
    }
    
    public float getHumidity() {
        return humidity;
    }
    
}

