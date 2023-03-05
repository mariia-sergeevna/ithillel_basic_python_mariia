1. Time complexity of list 'append()' operation.  
   *Answer:* It depends on size of list. Average case - O(1), worst case - O(N) and amortized worst case - O(1).
2. Time complexity of list 'in' operation.  
   *Answer:* 
3. Time complexity of list 'pop' operation:  
     * general case  
     * case with parameter '-1'  
   *Answer:*  
4. Time Complexity of add element to dict  
   *Answer:* 
5. Time complexity of dict 'in' operation.  
   *Answer:*
6. Time complexity for the code described below, assume that list 'value' consists of N elements
    ```python
   if isinstance(value, list):
       for i in range(0, 100, 3):
           if i in value:
               value.remove(i)
    ```
    *Answer:*
7. Time complexity for the code described below, assume that list 'work_list' consists of N elements
    ```python
   work_list = [*a]
   for i in range(len(work_list)):
       for j in range(1, len(work_list)):
           if work_list[j-1] > work_list[j]:
               buffer = work_list[j-1]
               work_list[j-1] = work_list[j]
               work_list[j] = buffer
    ```
    *Answer:*
8. Time complexity for the code described below, assume that list 'some_list' consists of N elements
    ```python
   result = {}
   for elem in some_list:
       if elem not in result:
           result[elem] = True
    ```
    *Answer:*
