public class Test {
    public static void main(String[] args) {
        ProxyDrucker druckerProxy = new ProxyDrucker();

        // Dokumente drucken
        druckerProxy.drucken("Hallo Welt!"); // Schwarz-Weiß-Drucker: Hallo wie gehts?
        druckerProxy.switchTo(new FarbDrucker());
        druckerProxy.drucken("Guten Tag!"); // Farbdrucker: Mir gehts gut!
    }
}
