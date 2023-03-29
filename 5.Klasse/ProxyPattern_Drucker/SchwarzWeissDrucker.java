public class SchwarzWeissDrucker implements Drucker {
    @Override
    public void drucken(String dokument) {
        System.out.println("Schwarz-Weiß-Drucker: " + dokument);
    }
}