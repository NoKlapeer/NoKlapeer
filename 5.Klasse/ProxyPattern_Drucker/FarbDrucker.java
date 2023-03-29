public class FarbDrucker implements Drucker {
    @Override
    public void drucken(String dokument) {
        System.out.println("Farbdrucker: " + dokument);
    }
}