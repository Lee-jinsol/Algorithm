class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int zeroCnt = 0;
        int sameCnt = 0;

        for (int i : lottos) {
            for (int j : win_nums) {
                if (i == j) {
                    sameCnt++;
                    break;
                }
            }
            if (i == 0) {
                zeroCnt++;
            }
        }

        int up = 7 - (zeroCnt + sameCnt) > 6 ? 6 : 7 - (zeroCnt + sameCnt);
        int down = 7 - (sameCnt) > 6 ? 6 : 7 - (sameCnt);
        int[] answer = { up, down };
        return answer;
    }
}