1. Time Complexity of operation 'append()' for list
    Answer: 
2. Time Complexity of operation 'in' for list
    Answer: 
3. Time Complexity of operation 'pop()' for list. a) in general b) with parameter '-1'
    Answer: 
4. Time Complexity of add element to dict
    Answer: 
5. Time Complexity of operation 'in' for dict
    Answer:
6. Time complexity for this code, assume that list 'value' consist of N elements
    ```python
   if isinstance(value, list):
       for i in range(0, 100, 3):
           if i in value:
               value.remove(i)
    ```
    Answer:
7. Time complexity for this code, assume that list 'work_list' consist of N elements
    ```python
   work_list = [*a]
   for i in range(len(work_list)):
       for j in range(1, len(work_list)):
           if work_list[j-1] > work_list[j]:
               buffer = work_list[j-1]
               work_list[j-1] = work_list[j]
               work_list[j] = buffer
    ```
    Answer:
8. Time complexity for this code, assume that list 'some_list' consist of N elements
    ```python
   result = {}
   for elem in some_list:
       if elem not in result:
           result[elem] = True
    ```
    Answer:
