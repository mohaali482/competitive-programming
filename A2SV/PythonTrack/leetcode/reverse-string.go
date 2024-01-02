func reverseString(s []byte)  {
    var i, j int
    j = len(s) - 1
    for i < j{
        s[i], s[j] = s[j], s[i]
        i++
        j--
    }
}