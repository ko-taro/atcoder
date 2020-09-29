import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        
        // Nを取得
		int n = sc.nextInt();
		
		//Aの各要素が（（奇数である）または（6の倍数または10の倍数））ではないとき、DENIEDを設定
		int a;
        String result = "APPROVED";
		for(int i=0;i<n;i++){
		    a = sc.nextInt();
            if(! (a % 2 == 1 || (a % 6 == 0 || a % 10 == 0))){
		        result = "DENIED";
                break;
		    }
		}
		
		//結果を出力
		System.out.println(result);
    }
}
