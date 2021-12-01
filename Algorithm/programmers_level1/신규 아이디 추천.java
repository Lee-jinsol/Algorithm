class Solution {
    public String solution(String new_id) {
        // 1단계
        String lower = new_id.toLowerCase();
        // 2단계
        char[] lowerchar = lower.toCharArray();
        StringBuilder step2 = new StringBuilder();
        for (char c : lowerchar) {
            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9') || (c == '-' || c == '_' || c == '.')) {
                step2.append(c);
            }
        }
        // 3단계
        String step3 = step2.toString().replace("..", ".");
        while (step3.contains("..")) {
            step3 = step2.replace("..", ".");
        }
        // 4단계

        return answer;
    }
}
