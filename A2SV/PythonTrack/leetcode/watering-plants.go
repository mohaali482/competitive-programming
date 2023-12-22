func wateringPlants(plants []int, capacity int) int {
    ans := 0
    currentCapacity := capacity
    for i, v := range(plants){
        currentCapacity -= v
        if i + 1 < len(plants) && plants[i+1] > currentCapacity{
            currentCapacity = capacity
            ans += 2*(i+1)
        }
        ans++
    }

    return ans
}