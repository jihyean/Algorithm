class Solution {
    public String solution(String s, String skip, int index) {
        
        String answer = ""; // 최종 결과(암호)를 저장할 문자열
        
        // String s의 길이만큼 반복
        for(int i = 0; i<s.length(); i++){

            char asc = s.charAt(i);
                
            int ascii = (int)asc;
            
            for(int j = 0; j<index; j++){ // index만큼 뒤로
                ascii++;
                while(ascii > 122){
                    ascii = ascii - 26;
                }
                
                if (skip.contains(String.valueOf((char) ascii))) { // skip 문자열 포함 검사
                    j--;
                }
                
            }
                 
            answer += (char)ascii;
        }
        
    return answer;
    }
}