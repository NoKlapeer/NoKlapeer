import java.util.Scanner;

public class test {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Geben sie die Zahl ein: ");
		int zahl = sc.nextInt();
		System.out.println("Ergebnis: " + sum(zahl));
	}

	// rekursive Summe

//	public static int sum(int zahl) {
//		if (zahl <= 1) {
//      	return 1;
//		}
//    	return zahl + sum(zahl - 1);
//	}

	// iterative Summe

	public static int sum(int zahl) {
		int ergebnis = 0;

		while (zahl > 0) {
			ergebnis += zahl;
			zahl -= 1;
		}

		return ergebnis;
	}
}
