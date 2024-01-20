class Solution{
    public:
    int select(int arr[], int i)
    {
        // code here such that selectionSort() sorts arr[]
        return arr[i];
    }
     
    void selectionSort(int arr[], int n)
    {
       //code here
       for(int i=0; i< n; i++){
           int num = arr[i];
           for (int j=0; j < n; j++){
               if(num < arr[j]){
                   num = arr[j];
                   int c = arr[i];
                   arr[i] = arr[j];
                   arr[j] = c;
               }
           }
       }
    }
    
                
};