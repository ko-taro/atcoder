import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        // Nを取得
		int n = sc.nextInt();
		
		//Aの各要素を取得
		int[] a = new int[n];
		for(int i=0;i<n;i++){
		    a[i] = sc.nextInt();
		}
		
		//Aの要素が（（奇数である）または（6の倍数または10の倍数））ではないとき、DENIEDを設定
		String result = "APPROVED";
		for(int i=0;i<n;i++){
		    if(! (a[i] % 2 == 1 || (a[i] % 6 == 0 || a[i] % 10 == 0))){
		        result = "DENIED";
		    }
		}
		
		//結果を出力
		System.out.println(result);
    }
}
