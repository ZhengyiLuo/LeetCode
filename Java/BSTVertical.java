import java.util.*;


class Untitled {
	public static void main(String[] args) {
		TreeNode node = new TreeNode(1);
		node.left = new TreeNode(1);
		node.left.left = new TreeNode(1);
		node.left.left.left = new TreeNode(1);
		node.right = new TreeNode(1);
		node.right.right = new TreeNode(1);
		
		Solution solu = new Solution();
		System.out.println(solu.verticalOrder(node));
	}
}


class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
  }
 
 class Solution {
	int leftR = 0;
	int rightR = 0;
	
	public List<List<Integer>> verticalOrder(TreeNode root) {
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		HashMap<Integer,List<Integer>> map = new HashMap<Integer, List<Integer>>();
		preOrderWalk(root, 0, map);
		int level = rightR - leftR - 1;
		for (int i = 0; i < level; i++) {
			result.add(map.get(i + leftR + 1));
		}
		
		return result;
	}
	
	void preOrderWalk(TreeNode root, int l, HashMap<Integer,List<Integer>> map){
		int left = 0;
		int right = 0;
		if (root == null) {
			if (l < leftR) {
				leftR = l;
			} else if (l > rightR) {
				rightR = l;
			}
			return;
		}
		
		if (map.containsKey(l)) {
				map.get(l).add(root.val);
			} else {
				ArrayList<Integer> list = new ArrayList<>();
				list.add(root.val);

				map.put(l, list);
			}
			
		preOrderWalk(root.left, l-1, map);		
		preOrderWalk(root.right, l+1, map);
		
		
		
	}	
	
	
}