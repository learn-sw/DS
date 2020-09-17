List<Interval> intervals = new ArrayList<>();
for (int i=0; i<A.length; i++){
    intervals.add(new Interval(A[i], B[i]));
}
Collections.sort(intervals);
List<Interval> result = new ArrayList<>();
Interval prev = intervals.get(0);
for(int i=1; i<intervals.size(); i++){
    Interval temp = intervals.get(i);
    if(temp.st <= prev.end ) {
        prev.st = Math.min(temp.st, prev.st);
        prev.end = Math.max(temp.end, prev.end);
    } else {
        result.add(prev);
        prev = temp;
    }
}
result.add(prev);
return result.size();
}

class Interval implements Comparable<Interval> {
int st;
int end;
public Interval(int a, int b){
    this.st=a;
    this.end=b;
}

@Override
public int compareTo(Interval o) {
    return this.st - o.st;
}
}