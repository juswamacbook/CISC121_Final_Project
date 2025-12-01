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

| Symbol | Name | Used For |
|--------|------|----------|
| `[START]/[END]` | Terminator | Beginning and end of the algorithm |
| `┃ ?? ┃` | Manual Input | User provides sorted array and target |
| `██████` | Process | Algorithm steps and calculations |
| `◇◇◇◇◇◇` | Decision | Branching points and comparisons |
| `▓▓▓▓▓▓` | Display | Showing results/output to user |
| `▒▒▒▒▒▒` | Manual Operation | Special operations or validations |
| `[||]` | Data Storage | Storing variables (low, high, mid) |
| `○──○` | Connector | Looping back to repeat process |

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
    
    %% Simplified styling that Mermaid actually supports
    classDef startEnd fill:#e1f5e1,stroke:#2e7d32,stroke-width:2px
    classDef manualInput fill:#fff3e0,stroke:#f57c00
    classDef preparation fill:#f3e5f5,stroke:#7b1fa2
    classDef process fill:#e3f2fd,stroke:#1976d2
    classDef decision fill:#fff3e0,stroke:#ff9800
    classDef display fill:#e8f5e8,stroke:#388e3c
    classDef connector fill:#ffffff,stroke:#666666,stroke-width:1px
    
    class Start,End startEnd
    class ManualInput,Display1,Display2,Display3 manualInput
    class Preparation preparation
    class Process1,Process2,Process3,Process4,ProcessReturn1,ProcessReturn2 process
    class Decision1,Decision2 decision
    class Connector connector
```
