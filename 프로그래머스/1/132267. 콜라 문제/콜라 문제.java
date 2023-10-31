class Solution {
    public int solution(int a, int b, int n) { // 2 1 20
    // 빈병 a개를 주면 콜라 b개로 교환
    // 현재 가지고 있는 빈병 n
    int answer = 0;
    
        // 더 이상 교환할 빈병이 없을때까지 반복
        while(n >= a){ 
            answer += ( n / a ) * b;        // 새로 받을 콜라 수
            n = ( n / a ) * b + ( n % a );  // 새로 생긴 빈병 수 + 교환하지 못하고 남은 빈병 수
        }
        
        return answer;
    }
    
}