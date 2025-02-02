public class Solution {
    public string Convert(string s, int numRows) {
        if (numRows == 1)
            return s;
        if (numRows >= s.Length)
            return s;
        
        var result = new char[s.Length]; 
        var m = numRows;
        var k = numRows - 2;
        var maxk = k;
        var sp = 0;
        var delta = 0;
        
        for (var i = 0; i < numRows; i++) {
            var p = i;
            result[sp++] = s[p];
            while (true) {
                delta = m + k;
                if (delta <= 0 || p + delta >= s.Length)
                    break;
                p += delta;
                result[sp++] = s[p];
                delta = (maxk - k) + (numRows - m);
                if (delta <= 0 || p + delta >= s.Length)
                    break;
                p += delta;
                result[sp++] = s[p];
            }
            k--;
            m--;
        }
        
        return new string(result, 0, sp);
    }
}
