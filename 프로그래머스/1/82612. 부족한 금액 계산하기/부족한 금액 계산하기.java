class Solution {
    public long solution(int price, int money, int count) {
        
        
        long total = 0;
        for(int i =0; i<count; i++){
            total += price*(i+1);
        }
        
        if(money-total >=0) {
            return 0;
        }

        return -(money-total);
    }
}