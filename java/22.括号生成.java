/*
 * @lc app=leetcode.cn id=22 lang=java
 *
 * [22] 括号生成
 */

// @lc code=start
class Solution {
    public List<String> generateParenthesis(int n) {
        List<Parenthesis> res = new ArrayList<>();
        res.add(new Parenthesis("(", 1));
        List<String> ret = new ArrayList<>();
        for (Parenthesis i : recurGen(res, n)) {
            if (i.offset == 0) {
                ret.add(i.string);
            }
        }
        return ret;
    }

    public static List<Parenthesis> recurGen(List<Parenthesis> list, int n) {
        while (list.get(0).string.length() < n * 2) {
            List<Parenthesis> tmp = new ArrayList<>();
            for (Parenthesis i : list) {
                if (i.offset > 0) {
                    tmp.add(i.addRight());
                }
                i.addLeft();
            }
            list.addAll(tmp);
        }
        return list;
    }

    static class Parenthesis {
        String string;
        int offset;  // Left - Right

        public Parenthesis(String s, int i) {
            string = s;
            offset = i;
        }

        public void addLeft() {
            string += "(";
            offset += 1;
        }

        public Parenthesis addRight() {
            return new Parenthesis(string + ")", offset - 1);
        }
    }
}
// @lc code=end

