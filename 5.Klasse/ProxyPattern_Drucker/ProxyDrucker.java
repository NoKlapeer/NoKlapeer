public class ProxyDrucker implements Drucker {
    private Drucker drucker;

    public void switchTo(Drucker neuerDrucker) {
        this.drucker = neuerDrucker;
    }

    @Override
    public void drucken(String dokument) {
        if (drucker == null) {
            // Standard-Drucker (z.B. Schwarz-Weiß)
            drucker = new SchwarzWeissDrucker();
        }
        drucker.drucken(dokument);
    }
}