import java.util.Scanner;

public class test {
	
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		System.out.print("Geben sie die Basiszahl ein: ");
		double basis = sc.nextDouble();
		System.out.print("Geben sie die Potenz ein: ");
		int pot = sc.nextInt();
		double npotenz = potenz(basis, pot);
		System.out.println("Ergebnis: " + npotenz);
	}



public static double potenz(double zahl, int pot) {
	  if (pot==1) {
	    return zahl;
	  } else {
	    return zahl*potenz(zahl,pot-1);
	  }
	}
}
