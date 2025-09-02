# 2D-array-operations-in-python 📚
This repository contains Python implementations of **matrix traversal algorithms** for 2D arrays.  
It includes different ways to iterate over matrices.  

**Note:** This is my independent work, developed based on practice exercises from CodeSignal.
## Algorithms Included

### Zig-Zag Column-wise Traversal  
**File:** `column-zigzag.py`  
Performs a zig-zag traversal of a matrix, moving **column by column** starting from the **bottom-right corner**. The direction alternates for each column: one upward, the next downward, and so on.  

### Vertical Column Traversal  
**File:** `vertical-traversal.py`  
Traverses a matrix **column by column** from **bottom to top**, starting at the **rightmost column** and moving left until all columns are covered.  

### Direction-based Traversal  
**File:** `direction-traverse.py`  
Traverses a matrix in a **predefined sequence of directions** (e.g., east, south, west, north), following the specified movement rules until all valid steps are completed.  

### Pattern Search  
**File:** `pattern-search.py`  
Searches a matrix for a **specific pattern** of values or characters, returning the locations of all matches.  

---

## How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/2D-array-operations-in-python.git
   cd 2D-array-operations-in-python

2. Run any of the scripts using Python:
```bash
python column-zigzag.py
python vertical-traversal.py
python direction-traverse.py
python pattern-search.py
```

3. Each script contains example matrices and outputs for demonstration.
Modify the matrix variable in the script to test with your own data.
