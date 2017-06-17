package account;

public class Test {

	public static void main(String[] args) {
		Account account=new Account();
		
		account.setAccountNumber(145046);
		account.setBalance(15000);
		System.out.println("Your account number is:"+account.getAccountNumber());
		System.out.println("Your account balance is:"+account.getBalance());
		
		account.setCredit(1500);
		System.out.println("Your account balance is:"+account.getCredit());
	}

}
