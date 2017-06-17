/**
 * 
 */
/**
 * @author Hridoy Alam
 *
 */
package account;
public class Account{
	private int accountNumber;
	private double balance=0.0;
	double credit;
	
	public int getAccountNumber(){
		return accountNumber;
	}
	public void setAccountNumber(int accountNumber){
		this.accountNumber=accountNumber;
	}
	public double getBalance(){
		return balance;
	}
	public void setBalance(double balance){
		this.balance=balance;
	}
	public void setCredit(double amount){
		this.balance=this.balance+amount;
	}
	public double getCredit(){
		return credit;
	}
	public void debit(double amount){
		amount=amount-balance;
	}
}