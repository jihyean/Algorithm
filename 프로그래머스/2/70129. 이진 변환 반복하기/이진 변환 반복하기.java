class Solution {

    static int cnt = 0;
    static int allcount = 0;

    public int[] solution(String s) {
        int[] answer = new int [2];
        delete(s);
        answer[0] = allcount;
        answer[1] = cnt;
        return answer;
    }

    private static String delete(String binary) {

        // binary 값이 1이 되면 호출한 부분으로 돌아감
        if(binary.equals("1"))
            return "";

        int zerocount = 0;
        // 0의 개수 출력
        for(int i = 0; i < binary.length(); i++) {
            if(binary.charAt(i) == '0')
                zerocount++;
        }
        cnt += zerocount;                           // 제거된 전체 0의 갯수
        int length = binary.length() - zerocount;   // 0 제거 후의 길이
        allcount++;                                 // 전체 변환 수
        
        return delete(Integer.toString(length,2));
    }
}  