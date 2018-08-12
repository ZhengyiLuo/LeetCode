import java.util.*;

class Untitled {
	public static void main(String[] args) {
		
		
		Solution solu = new Solution();
		System.out.println(solu.minWindow("aa", "aa"));		
		
	}
}


class Solution {
	public String minWindow(String s, String t) {
		HashMap<Character,Integer> alphbet = new HashMap<Character,Integer>();
		HashMap<Character,Integer> counterMap = new HashMap<Character,Integer>();
		int[] result = new int[s.length()];
		int start = 0;
		for (int i = 0; i < t.length(); ++i){
			char c = t.charAt(i);
			if (alphbet.containsKey(c)) {
				alphbet.put(c, alphbet.get(c) + 1);
			} else {
				alphbet.put(c, 1);
			}
		}
		
		for (int i = 0; i < s.length(); ++ i) {
			char c = s.charAt(i);
			if (alphbet.containsKey(c)) {
				if (counterMap.containsKey(c)) {
					counterMap.put(c, counterMap.get(c)+1);
				} else {
					counterMap.put(c, 1);
				}
				
				
				while (isWindow(counterMap, alphbet)) {
					result[start] = i - start + 1;
					char startc = s.charAt(start);
					if (counterMap.containsKey(startc)) {
						int num = counterMap.get(startc);
						if (num >= 2 ) {
							counterMap.put(startc, --num);
						} else {
							counterMap.remove(startc);
						}
					}
					start++;
				}

			}
			
			

		}
		
		int min = 9999999;
		int minIndx = 0;
		for (int i = 0; i < result.length; ++i) {
			if (result[i] >= 1 && result[i] < min) {
				minIndx = i;
				min = result[i];
			}
		}
		
		return s.substring(minIndx, minIndx+result[minIndx]);
	
	
	
	
	}
	
	public boolean isWindow(HashMap<Character,Integer> counterMap, HashMap<Character,Integer> alphbet){
	 	for (char c : alphbet.keySet()) {
					if (!counterMap.containsKey(c)) {
						return false;
					}	else if (counterMap.get(c) < alphbet.get(c)) {
						return false;
					}
		}	
		return true;	
		
	}
}