# Binary Search Algorithm Visualizer

## Demo Video/GIF/Screenshot

*(Replace this section with your actual visual materials)*

**Demo GIF:**
<!-- ![Binary Search Demo](demo/binary-search-demo.gif) -->

**Screenshots:**
<!-- ![Screenshot 1](screenshots/screenshot1.png)
![Screenshot 2](screenshots/screenshot2.png) -->

**Video Demo:** [Link to video recording if available]

## Problem Breakdown & Computational Thinking

### Algorithm Overview
Binary Search is an efficient searching algorithm that finds the position of a target value within a **sorted array**. It works by repeatedly dividing the search interval in half, comparing the middle element with the target value, and eliminating half of the remaining elements at each step.

### Computational Thinking Approach

#### 1. **Decomposition**
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

#### 2. **Pattern Recognition**
- Repeated halving of search space (divide-and-conquer)
- Systematic comparison at midpoint
- Progressive narrowing of search boundaries
- Logarithmic time complexity: O(log n)

#### 3. **Abstraction**
**Shown to user:**
- Current search boundaries (low, high pointers)
- Midpoint calculation and comparison
- Visual highlighting of compared elements
- Step-by-step progression through algorithm
- Final result (position or "not found")

**Hidden from user:**
- Underlying array indexing details
- Mathematical floor division
- Loop control variables
- Memory allocation details

#### 4. **Algorithm Design**
**Input → Processing → Output Flow:**

### Flowchart Symbol Key
The following symbols are used in the Binary Search algorithm flowchart:

```mermaid
flowchart TD
    subgraph A["Terminator (Start/End)"]
        A1([Start/End])
    end
    
    subgraph B["Manual Input"]
        B1[/User Input/]
    end
    
    subgraph C["Process/Operation"]
        C1[Process Step]
    end
    
    subgraph D["Decision/Branching"]
        D1{Condition?}
    end
    
    subgraph E["Display/Output"]
        E1[/Output Display/]
    end
    
    subgraph F["Connector/Loop"]
        F1((Connector))
    end
    
    A --> B --> C --> D --> E --> F
    
    %% Improved styling with better contrast
    classDef terminator fill:#4CAF50,stroke:#2E7D32,stroke-width:2px,color:#ffffff,font-weight:bold
    classDef input fill:#FF9800,stroke:#EF6C00,stroke-width:2px,color:#000000,font-weight:bold
    classDef process fill:#2196F3,stroke:#1976D2,stroke-width:2px,color:#ffffff,font-weight:bold
    classDef decision fill:#FFC107,stroke:#FF9800,stroke-width:2px,color:#000000,font-weight:bold
    classDef display fill:#8BC34A,stroke:#689F38,stroke-width:2px,color:#000000,font-weight:bold
    classDef connector fill:#FFFFFF,stroke:#757575,stroke-width:2px,color:#000000
    classDef keyBox fill:#f8f9fa,stroke:#dee2e6,stroke-width:1px,rx:8,ry:8
    
    class A1 terminator
    class B1 input
    class C1 process
    class D1 decision
    class E1 display
    class F1 connector
    class A,B,C,D,E,F keyBox
```

| Symbol | Name | Purpose | Used in Binary Search For |
|--------|------|---------|---------------------------|
| `([Start/End])`<br>![Green Circle](https://via.placeholder.com/15/4CAF50/000000?text=+) | **Terminator** | Beginning and end points | Starting the search and ending when complete |
| `[/.../]`<br>![Orange Parallelogram](https://via.placeholder.com/15/FF9800/000000?text=+) | **Manual Input/Display** | User input or output display | Receiving sorted array/target; displaying results |
| `[...]`<br>![Blue Rectangle](https://via.placeholder.com/15/2196F3/000000?text=+) | **Process/Operation** | Algorithm steps and calculations | Initializing pointers, calculating midpoint |
| `{...?}`<br>![Yellow Diamond](https://via.placeholder.com/15/FFC107/000000?text=+) | **Decision/Branching** | Conditional checks | Checking loop condition, comparing values |
| `((...))`<br>![White Circle](https://via.placeholder.com/15/FFFFFF/000000?text=+) | **Connector** | Connecting flow segments | Looping back to repeat search |

### Color & Contrast Guide:

| Color | Element Type | Text Color | Purpose |
|-------|--------------|------------|---------|
| ![#4CAF50](https://via.placeholder.com/15/4CAF50/000000?text=+) **Green** | Terminator | **White** | Start/End points - high visibility |
| ![#FF9800](https://via.placeholder.com/15/FF9800/000000?text=+) **Orange** | Input/Output | **Black** | User interaction points |
| ![#2196F3](https://via.placeholder.com/15/2196F3/000000?text=+) **Blue** | Process | **White** | Core algorithm operations |
| ![#FFC107](https://via.placeholder.com/15/FFC107/000000?text=+) **Yellow** | Decision | **Black** | Comparisons and branching |
| ![#8BC34A](https://via.placeholder.com/15/8BC34A/000000?text=+) **Light Green** | Display | **Black** | Results and output |
| ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) **White** | Connector | **Black** | Flow connections |

### Binary Search Specific Examples:

| Step | Symbol | Description |
|------|--------|-------------|
| 1 | `([Start])` | Algorithm begins |
| 2 | `[/Sorted Array: 1,3,5,7,9/]` | User inputs data |
| 3 | `[Initialize: low=0, high=4]` | Set up search boundaries |
| 4 | `{low ≤ high?}` | Check if search should continue |
| 5 | `[Calculate: mid = (0+4)//2 = 2]` | Find midpoint |
| 6 | `{arr[2] = target?}` | Compare middle element |
| 7 | `[/Found at index 2/]` | Display successful result |
| 8 | `((Loop))` | Return to step 4 |
| 9 | `([End])` | Algorithm completes |

**Note:** All symbols use high-contrast color combinations (light text on dark backgrounds, dark text on light backgrounds) for maximum readability.

### Flow Chart:

```mermaid
flowchart TD
    Start(["Start"]) --> ManualInput[/"Manual Input: Sorted Array & Target Value"/]
    
    ManualInput --> Preparation{"Preparation: Validate Input"}
    Preparation -->|Valid| Process1["Initialize: low = 0, high = n-1"]
    Preparation -->|Invalid| Display1["Display: Error Message"]
    Display1 --> End(["End"])
    
    Process1 --> Decision1{"low ≤ high?"}
    
    Decision1 -->|No| Display2[/"Display: Target Not Found"/]
    Display2 --> ProcessReturn2["Return: -1"]
    ProcessReturn2 --> End
    
    Decision1 -->|Yes| Process2["Calculate: mid = (low + high) // 2"]
    Process2 --> Decision2{"Compare arr[mid] with x"}
    
    Decision2 -->|Equal| Display3[/"Display: Found at index mid"/]
    Display3 --> ProcessReturn1["Return: mid"]
    ProcessReturn1 --> End
    
    Decision2 -->|Less Than| Process3["Update: low = mid + 1<br>Search Right Half"]
    Process3 --> Connector(( ))
    
    Decision2 -->|Greater Than| Process4["Update: high = mid - 1<br>Search Left Half"]
    Process4 --> Connector
    
    Connector --> Decision1
    
    %% Alternative styling with good contrast
    classDef startEnd fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef manualInput fill:#FFB74D,stroke:#FF9800,stroke-width:2px,color:#000000,font-weight:bold
    classDef preparation fill:#BA68C8,stroke:#9C27B0,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef process fill:#64B5F6,stroke:#2196F3,stroke-width:2px,color:#000000,font-weight:bold
    classDef decision fill:#FFD54F,stroke:#FFC107,stroke-width:2px,color:#000000,font-weight:bold
    classDef display fill:#81C784,stroke:#4CAF50,stroke-width:2px,color:#000000,font-weight:bold
    classDef connector fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#000000,font-weight:bold
    
    class Start,End startEnd
    class ManualInput,Display1,Display2,Display3 manualInput
    class Preparation preparation
    class Process1,Process2,Process3,Process4,ProcessReturn1,ProcessReturn2 process
    class Decision1,Decision2 decision
    class Connector connector
```

### Steps to Run:

## Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

## Installation Steps

# 1. Clone the repository:

```bash
git clone https://github.com/juswamacbook/CISC121-_Final-Project.git
cd CISC121-_Final-Project
```

# 2. Install required dependencies:
```
bash
pip install -r requirements.txt
```

# 3. Run the application:

```
bash
python app.py
```
# 4. Access the app:

- Open your web browser

- Navigate to: http://localhost:7860

- Or click the link provided in the terminal

## Using the Application

# Input Section:

- Enter a comma-separated list of numbers (e.g., 1, 3, 5, 7, 9, 11)

- Enter a target value to search for

- Click "Search" button

# Visualization:

- Watch the step-by-step search process

- See color-coded elements:

    - Red: Current search boundaries

    - Blue: Current midpoint being compared

    - Green: Found target element

- Follow the algorithm logic in real-time

# Output:

- Result displayed: Position index or "Not Found"

- Number of steps taken

- Time complexity explanation

## Testing & Verification

# Test Cases Performed
# Test Cases Performed

| Test Case      | Input Array            | Target | Expected Result | Status |
|----------------|------------------------|--------|-----------------|--------|
| Normal Case    | [1, 3, 5, 7, 9, 11]    | 7      | Index 3         | ✓      |
| First Element  | [2, 4, 6, 8, 10]       | 2      | Index 0         | ✓      |
| Last Element   | [1, 2, 3, 4, 5]        | 5      | Index 4         | ✓      |
| Not Found      | [10, 20, 30, 40]       | 25     | -1              | ✓      |
| Empty Array    | []                     | 5      | -1              | ✓      |
| Single Element | [42]                   | 42     | Index 0         | ✓      |
| Large Array    | 1-1000                 | 777    | Index 776       | ✓      |

# Edge Cases Handled
- ✅ Empty input arrays

- ✅ Single-element arrays

- ✅ Target not in array

- ✅ Non-numeric inputs (error handling)

- ✅ Unsorted arrays (with sorting reminder)

# Verification Methods
1. Manual Testing: Multiple test runs with varied inputs

2. Unit Tests: Basic test functions included in code

3. Visual Verification: Step-by-step visualization confirms logic

4. Complexity Analysis: Confirms O(log n) behavior

### Hugging Face Link
- Live Application: [Your Hugging Face Space Link Here]
(Once deployed, replace with your actual Hugging Face URL)

## To deploy on Hugging Face:

- Create a Hugging Face account

- Create a new Space

- Choose "Gradio" as SDK

- Upload your files: app.py, requirements.txt

Your app will be available at: https://huggingface.co/spaces/[your-username]/[app-name]

## Features & Implementation Details

# Algorithm Implementation
```
python
def binary_search(arr, target):
    """
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of numbers
        target: Number to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    low, high = 0, len(arr) - 1
    steps = []
    
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, mid, high, arr[mid]))  # Record step for visualization
        
        if arr[mid] == target:
            return mid, steps  # Found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    
    return -1, steps  # Not found
```
## Gradio Interface Features
- Input Validation: Ensures sorted array requirement

- Step-by-Step Visualization: Animated progression

- Color Coding: Visual distinction of algorithm states

- Educational Labels: Clear explanations of each step

- Responsive Design: Works on different screen sizes

## Key Python Libraries Used
- Gradio: For creating the web interface

- Matplotlib/Plotly: For visualization (if used)

- Time: For step delays in visualization

### Author & Acknowledgment

Author: Joshua M. Ranin

Student ID: [204567769]

Course: CISC-121

Institution: Queen's University

## Acknowledgments

- Course instructor and TAs for project guidance

- Gradio team for the excellent UI library

- Hugging Face for free app deployment

- Visualgo for algorithm visualization inspiration

## References

1. Binary Search Algorithm - GeeksforGeeks

2. Gradio Documentation: https://www.gradio.app/docs/

3. Hugging Face Spaces Guide

4. CISC-121 Course Materials

## **How to Use This:**

1. **Save as `README.md`** in your GitHub repository root

2. **Fill in the placeholder sections:**

   - Your name and student ID in "Author" section
     
   - Add actual demo media (GIFs/screenshots)
     
   - Add your Hugging Face link once deployed
     
4. **Add your actual `app.py` code** when ready
   
6. **Create `requirements.txt`** with: `gradio`

## Project Structure

CISC121-_Final-Project/
├── README.md # This documentation file
├── app.py # Main application file
├── requirements.txt # Python dependencies
├── demo/ # Optional: Demo media files
│ └── binary-search-demo.gif
└── screenshots/ # Optional: Screenshot images
├── screenshot1.png
└── screenshot2.png


