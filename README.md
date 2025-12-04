# Binary Search Algorithm Visualizer

## Demo Video/GIF/Screenshot

**Demo GIF:**
![Binary Search Demo](demo/binary-search-demo.gif)

**Screenshots:**
![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png)

**Video Demo:** [Link to video recording]

---

## Problem Breakdown & Computational Thinking

### Algorithm Overview
Binary Search is an efficient searching algorithm that finds the position of a target value within a **sorted array**. It works by repeatedly dividing the search interval in half, comparing the middle element with the target value, and eliminating half of the remaining elements at each step.

### Computational Thinking Approach

#### 1. Decomposition
Breaking Binary Search into smaller steps:
- **Step 1:** Receive sorted array and target value as input
- **Step 2:** Initialize pointers: `low = 0`, `high = len(array) - 1`
- **Step 3:** While `low <= high`:
  - Calculate `mid = (low + high) // 2`
  - Compare `array[mid]` with target:
    - If equal: return `mid` (found)
    - If less: update `low = mid + 1` (search right half)
    - If greater: update `high = mid - 1` (search left half)
- **Step 4:** Return `-1` if not found

#### 2. Pattern Recognition
- Repeated halving of search space (divide-and-conquer)
- Systematic comparison at midpoint
- Progressive narrowing of search boundaries
- Logarithmic time complexity: O(log n)

#### 3. Abstraction
**What the user sees:**
- Current search boundaries (low, high pointers)
- Midpoint calculation and comparison
- Visual highlighting of compared elements
- Step-by-step progression through algorithm
- Final result (position or "not found")

**What is hidden:**
- Underlying array indexing details
- Mathematical floor division
- Loop control variables
- Memory allocation details

#### 4. Algorithm Design

**Input:**
- Sorted array of integers (1-20 elements)
- Target value to search for
- Input validation for correct data types

**Output:**
- Visual representation with color-coded elements:
  - Red: Current search boundaries (low and high)
  - Blue: Current midpoint being examined
  - Green: Found target element
  - Gray: Elements outside search range
- Search result message (found at index X or not found)
- Step-by-step execution trace
- Algorithm metrics (comparisons made, efficiency)

---

### Flowchart

```mermaid
flowchart TD
    Start([Start]) --> Input[/Input: Sorted Array & Target/]
    
    Input --> Validate{Valid Input?}
    Validate -->|No| Error[/Display Error/]
    Error --> End([End])
    
    Validate -->|Yes| Init[Initialize: low=0, high=n-1]
    Init --> Loop{low <= high?}
    
    Loop -->|No| NotFound[/Display: Not Found/]
    NotFound --> End
    
    Loop -->|Yes| CalcMid[Calculate: mid = low + high // 2]
    CalcMid --> Compare{arr[mid] vs target}
    
    Compare -->|Equal| Found[/Display: Found at mid/]
    Found --> End
    
    Compare -->|Less| UpdateLow[Update: low = mid + 1]
    UpdateLow --> Loop
    
    Compare -->|Greater| UpdateHigh[Update: high = mid - 1]
    UpdateHigh --> Loop
    
    classDef startEnd fill:#4CAF50,stroke:#2E7D32,color:#fff
    classDef process fill:#2196F3,stroke:#1976D2,color:#fff
    classDef decision fill:#FFC107,stroke:#F57C00,color:#000
    classDef io fill:#FF9800,stroke:#EF6C00,color:#000
    
    class Start,End startEnd
    class Init,CalcMid,UpdateLow,UpdateHigh process
    class Validate,Loop,Compare decision
    class Input,Error,NotFound,Found io
```

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/juswamacbook/CISC121_Final_Project.git
cd CISC121_Final_Project
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the application:**
```bash
python app.py
```

5. **Access the app:**
- Open your web browser
- Navigate to: http://localhost:7860
- Or click the link provided in the terminal

---

## Using the Application

### Input
1. Enter a comma-separated list of sorted numbers (e.g., `1, 3, 5, 7, 9, 11`)
2. Enter a target value to search for
3. Click "Run Binary Search" button

### Visualization
- Watch the step-by-step search process
- Color-coded elements show algorithm state:
  - **Red (L/H):** Current search boundaries
  - **Blue (M):** Current midpoint being compared
  - **Green (M):** Found target element

### Output
- Search result: Position index or "Not Found"
- Number of comparisons made
- Step-by-step execution trace
- Algorithm efficiency metrics

---

## Testing & Verification

### Test Cases Performed

| Test Case      | Input Array            | Target | Expected Result | Status |
|----------------|------------------------|--------|-----------------|--------|
| Normal Case    | [1, 3, 5, 7, 9, 11]    | 7      | Index 3         | ✓      |
| First Element  | [2, 4, 6, 8, 10]       | 2      | Index 0         | ✓      |
| Last Element   | [1, 2, 3, 4, 5]        | 5      | Index 4         | ✓      |
| Not Found      | [10, 20, 30, 40]       | 25     | -1              | ✓      |
| Single Element | [42]                   | 42     | Index 0         | ✓      |

### Edge Cases Handled
- Empty input arrays
- Single-element arrays
- Target not in array
- Non-numeric inputs (error handling)
- Unsorted arrays (error message)
- Array size limits (max 20 elements)

### Verification Methods
1. **Manual Testing:** Multiple test runs with varied inputs
2. **Visual Verification:** Step-by-step visualization confirms logic
3. **Complexity Analysis:** Confirms O(log n) behavior

---

## Algorithm Implementation

### Core Binary Search Function

```python
def binary_search(arr, target):
    """
    Implements binary search algorithm iteratively.
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    steps = []
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        steps.append({'low': low, 'high': high, 'mid': mid})
        
        if arr[mid] == target:
            return mid, steps  # Found
        elif arr[mid] < target:
            low = mid + 1      # Search right half
        else:
            high = mid - 1     # Search left half
    
    return -1, steps           # Not found
```

### Key Features
- **Input Validation:** Ensures sorted array requirement
- **Step-by-Step Visualization:** Real-time algorithm progression
- **Color Coding:** Visual distinction of algorithm states
- **Educational Output:** Clear explanations of each step
- **Responsive Design:** Works on different screen sizes

---

## Key Python Libraries Used

- **Gradio:** Web interface and user interaction
- **Matplotlib:** Bar chart visualization
- **NumPy:** Efficient array operations and calculations

---

## Deployment

### Hugging Face Spaces
Live Application: [Your Hugging Face Space Link]

### To Deploy:
1. Create a Hugging Face account at https://huggingface.co
2. Create a new Space and select "Gradio" as SDK
3. Upload `app.py` and `requirements.txt`
4. Your app will be live at: `https://huggingface.co/spaces/[username]/[space-name]`

---

## Project Structure

```
CISC121_Final_Project/
├── README.md              # Project documentation
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── demo/                  # Demo media files
│   └── binary-search-demo.gif
└── screenshots/           # Screenshot images
    ├── screenshot1.png
    └── screenshot2.png
```

---

## Author & Acknowledgments

**Author:** Joshua M. Ranin  
**Student ID:** 20457769  
**Course:** CISC-121  
**Institution:** Queen's University  
**Date:** December 2024

### Acknowledgments
- Course instructor and TAs for project guidance
- Gradio team for the excellent UI library
- Hugging Face for free app deployment

---

## References

1. [Binary Search Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
2. [Gradio Documentation](https://www.gradio.app/docs/)
3. [Hugging Face Spaces Guide](https://huggingface.co/docs/hub/spaces)
4. CISC-121 Course Materials

---

## License

This project is created for educational purposes as part of CISC-121 coursework at Queen's University.