class Untitled {
	public static void main(String[] args) {
		
	}
}

public class Solution {
	public int rob(int[] nums) {
		int odd = 0;
		int even = 0;
		for (int i = 0; i < nums.length; i++) {
			if (i%2 == 0) {
				even = Math.max(odd, even + numsp[i]);
			} else {
				odd = Math.max(even, odd + numsp[i]);
			}
			
		}
		
		return Math.max(even, odd);
		
	
	}
}
