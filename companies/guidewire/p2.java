public int highNum(int N) {
    final int MAX_NUM = 100000000;
    int[] map = new int[10];
    while(N>0){
        map[N%10]++;
        N=N/10;
    }
    StringBuilder sb = new StringBuilder();
    for(int i=map.length-1; i>=0;i--){
        while (map[i]>0){
            sb.append(i);
            map[i]--;
        }
    }
    if(sb.length()==0){
        sb.append(0);
    }
    try {
        int result =  Integer.parseInt(sb.toString());
        if(result>MAX_NUM) return -1;
        else return result;
    } catch (NumberFormatException exception){
        return -1;
    }
}