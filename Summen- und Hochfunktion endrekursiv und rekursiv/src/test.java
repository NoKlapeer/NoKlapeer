
public class test {
	
	
	
	

	public static void main(String[] args) {
		
		long time;
		
		time  = System.nanoTime();
		long SummeR = sumRekursiv(20);
		time = System.nanoTime() - time;
		System.out.println("Summe Rekursiv Ergebnis:" + SummeR + " Zeit: " + time + " ns");
		
		time  = System.nanoTime();
		long SummeE = sumEndRekursiv(20);
		time = System.nanoTime() - time;
		System.out.println("Summe Endrekursiv Ergebnis:" + SummeE + " Zeit: " + time + " ns");
		
		
		time  = System.nanoTime();
		long PotenzR = potenzRekursiv(6, 3);
		time = System.nanoTime() - time;
		System.out.println("Potenz Rekursiv Ergebnis: " + PotenzR + " Zeit: " + time + " ns");
		
		time  = System.nanoTime();
		long PotenzE = potEndRekursiv(6, 3);
		time = System.nanoTime() - time;
		System.out.println("Potenz Endrekursiv Ergebnis: " + PotenzE + " Zeit: " + time + " ns");

	}
	
	 public static long sumEndRekursiv(int n) {
	   return addsum (0, n);
	 }
	 public static long addsum(int m, int n) {
	   if (n==0) {
	     return m;
	   }
	     return addsum (m+n, n-1); 	
	 }
	 
	 public static long potEndRekursiv(int basis, int exponent) {
		   return addpot(basis, exponent, 1);
	 }
		 public static long addpot(int basis, int exponent, int m) {
		   if (exponent==0) {
		     return m;
		   }  
		     return addpot(basis, exponent-1, basis * m); 	
		 }
		 
		 public static long potenzRekursiv(long zahl, long pot) {
				if (pot == 1) {
					return zahl;
				} else {
					return zahl * potenzRekursiv(zahl, pot - 1);
				}
			}
		 
			public static int sumRekursiv(int zahl) {
				if (zahl <= 1) {
		      	return 1;
				}
		    	return zahl + sumRekursiv(zahl - 1);
			}

}
