<!-- 2024-02-15 20:46:17 -->
Lookup/Search/Query with Restrictions
-------------------------------------
This note aims to summarize all questions that uses the idea of lookup/search/query with restrictions.
The main idea behind this type of question is for each lookup/search/query we have some restrictions that 
makes some answers in the answer space not qualified for the current lookup/search/query. However, as we 
progress these answers become qualified for lookup/search/query. 

One general approach for this type of question is to dynamically add qualified answers to a "queryable" set.
We maintain a set of answers that is queryable to the current restriction. Then, as the restriction updates,
we add more answers to the "queryable" set. Generally, we visit/traverse/iterate the query/lookup monotonically
either that monotonicity is associated with array's idex or with value order. 


Questions:
==========
- [1707. Maximum XOR With an Element From Array](https://leetcode.com/problems/maximum-xor-with-an-element-from-array/)

