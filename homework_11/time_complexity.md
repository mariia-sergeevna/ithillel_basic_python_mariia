1. Time complexity of list 'append()' operation.  
   **Answer:**  It depends on size of list. Average case - O(1), worst case - O(N) and amortized worst case - O(1).
2. Time complexity of list 'in' operation.  
   **Answer:**  Average case - O(N)
3. Time complexity of list 'pop' operation:  
     * general case  (**Answer:**  O(N), because if element is first > then all rest list will be shifted)
     * case without parameter (**Answer:** O(1) in all cases, because deleting the last element in the list is independent of the length of the list)
4. Time Complexity of add element to dict  
   **Answer:**  Average case - O(1), amortized worst case - O(N).
5. Time complexity of dict 'in' operation.  
   **Answer:**  Average case - O(1), amortized worst case - O(N).
6. Time complexity for the code described below, assume that list 'value' consists of N elements
    ```python
   if isinstance(value, list): # O(1)
       for i in range(0, 100, 3): # O(100/3) == O(1)
           if i in value: # O(N)
               value.remove(i) # O(100/3)
    ```
    **Answer:**  O(33 * N) = O(N)
7. Time complexity for the code described below, assume that list 'work_list' consists of N elements
    ```python
   work_list = [*a] # O(N)
   for i in range(len(work_list)): # O(N)
       for j in range(1, len(work_list)): # O(N - 1)
           if work_list[j-1] > work_list[j]: # O(1)
               buffer = work_list[j-1] # O(1)
               work_list[j-1] = work_list[j] # O(1)
               work_list[j] = buffer # O(1)
    ```
    **Answer:** O(N^2)
8. Time complexity for the code described below, assume that list 'some_list' consists of N elements
    ```python
   result = {} # O(1)
   for elem in some_list: # O(N)
       if elem not in result: # O(1)
           result[elem] = True  # O(1)
    ```
    **Answer:**  O(N)
