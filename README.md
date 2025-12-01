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

## Flowchart Symbol Key

## Flowchart Symbol Key

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
    
    %% Fixed styling with proper contrast
    classDef startEnd fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef manualInput fill:#FF9800,stroke:#EF6C00,stroke-width:2px,color:#000000,font-weight:bold
    classDef preparation fill:#7B1FA2,stroke:#6A1B9A,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef process fill:#1976D2,stroke:#1565C0,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef decision fill:#FF9800,stroke:#EF6C00,stroke-width:2px,color:#000000,font-weight:bold
    classDef display fill:#388E3C,stroke:#2E7D32,stroke-width:2px,color:#FFFFFF,font-weight:bold
    classDef connector fill:#FFFFFF,stroke:#757575,stroke-width:2px,color:#000000,font-weight:bold
    
    class Start,End startEnd
    class ManualInput,Display1,Display2,Display3 manualInput
    class Preparation preparation
    class Process1,Process2,Process3,Process4,ProcessReturn1,ProcessReturn2 process
    class Decision1,Decision2 decision
    class Connector connector
```
