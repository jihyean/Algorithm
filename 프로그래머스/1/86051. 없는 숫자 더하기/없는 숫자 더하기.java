class Solution {
    public int solution(int[] numbers) {
    // 0 ~ 9 의 모든 수 합 : 45
        
        int answer = 0;
        for(int i = 0; i<numbers.length; i++){
            answer+=numbers[i];
        }
        answer = 45 - answer;
        
        return answer;
    }
}