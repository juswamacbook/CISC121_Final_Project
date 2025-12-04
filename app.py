"""
Binary Search Algorithm Visualizer

This program implements the binary search algorithm with interactive visualization
using Gradio. It demonstrates how binary search efficiently finds elements in a
sorted array by repeatedly dividing the search space in half.

Author: Joshua M. Ranin
Student ID: 20457769
Date: December 2024
Course: CISC-121
"""

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np


def binary_search(arr, target):
    """
    Implements the binary search algorithm iteratively.
    
    Algorithm steps:
    1. Initialize low pointer to start (0) and high pointer to end (len-1)
    2. While low <= high:
        a. Calculate midpoint: mid = (low + high) // 2
        b. If arr[mid] == target: return mid (found)
        c. If arr[mid] < target: search right half (low = mid + 1)
        d. If arr[mid] > target: search left half (high = mid - 1)
    3. If not found, return -1
    
    Time Complexity: O(log n) - each step eliminates half the remaining elements
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Args:
        arr: Sorted list of integers to search through
        target: Integer value to search for
    
    Returns:
        Tuple of (index, steps) where:
        - index is position of target (-1 if not found)
        - steps is a list of dictionaries tracking each iteration
    """
    steps = []
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    # Main search loop - continues while search space is valid
    while low <= high:
        # Calculate midpoint (avoiding integer overflow)
        mid = (low + high) // 2
        comparisons += 1
        
        # Record current state for visualization
        steps.append({
            'low': low,           # Current lower boundary
            'high': high,         # Current upper boundary
            'mid': mid,           # Current midpoint being checked
            'value': arr[mid],    # Value at midpoint
            'comparison': comparisons
        })
        
        # Check if we found the target
        if arr[mid] == target:
            return mid, steps
        
        # Target is in right half - eliminate left half
        elif arr[mid] < target:
            low = mid + 1
        
        # Target is in left half - eliminate right half
        else:
            high = mid - 1
    
    # Target not found in array
    return -1, steps


def visualize(arr, step, is_found=False):
    """
    Creates a bar chart visualization showing the current state of the search.
    
    The visualization uses color coding to help understand what the algorithm is doing:
    - Gray bars: Elements not currently being examined
    - Red bars: Current search boundaries (low and high pointers)
    - Blue bar: Current midpoint being compared
    - Green bar: Target element (when found)
    
    Args:
        arr: The array being searched
        step: Dictionary with current low, high, mid pointers and values
        is_found: Boolean indicating whether target was found
    
    Returns:
        Matplotlib figure object ready to display
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Set up bar colors - default to gray
    colors = ['#d3d3d3'] * len(arr)
    
    # Color the search boundaries red
    colors[step['low']] = '#ff4444'
    colors[step['high']] = '#ff4444'
    
    # Color the midpoint blue (or green if target found)
    if is_found:
        colors[step['mid']] = '#44ff44'  # Green = success!
    else:
        colors[step['mid']] = '#4444ff'  # Blue = checking this element
    
    # Create the bar chart
    ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', width=0.8)
    
    # Add value labels on top of each bar
    for i, val in enumerate(arr):
        ax.text(i, val + 0.3, str(val), ha='center', fontsize=11, fontweight='bold')
    
    # Add pointer labels below the chart
    ax.text(step['low'], -1.5, 'L', ha='center', fontsize=11, 
            color='#ff4444', fontweight='bold')
    ax.text(step['high'], -1.5, 'H', ha='center', fontsize=11, 
            color='#ff4444', fontweight='bold')
    ax.text(step['mid'], arr[step['mid']] + 1.2, 'M', ha='center', fontsize=11,
            color='#44ff44' if is_found else '#4444ff', fontweight='bold')
    
    # Configure chart appearance
    ax.set_ylim(-2, max(arr) + 2.5)
    ax.set_xlabel('Array Index', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title(f"Step {step['comparison']}: Checking index {step['mid']} (value = {step['value']})", 
                 fontsize=13, fontweight='bold')
    ax.grid(alpha=0.2, linestyle='--')
    
    plt.tight_layout()
    return fig


def validate_input(array_str, target_str):
    """
    Validates and parses user input to ensure it meets algorithm requirements.
    
    Checks performed:
    - Input is not empty
    - All values are valid integers
    - Array is sorted (required for binary search)
    - Array size is reasonable for visualization
    
    Args:
        array_str: Comma-separated string of integers
        target_str: String representation of target integer
    
    Returns:
        Tuple of (arr, target, error_message)
        If valid: (list, int, None)
        If invalid: (None, None, error_string)
    """
    # Check for empty inputs
    if not array_str.strip():
        return None, None, "Error: Please enter an array of numbers"
    
    if not target_str.strip():
        return None, None, "Error: Please enter a target value to search for"
    
    try:
        # Parse array from comma-separated string
        arr = [int(x.strip()) for x in array_str.split(',') if x.strip()]
        
        # Parse target value
        target = int(target_str.strip())
        
        # Validate array is not empty
        if not arr:
            return None, None, "Error: Array cannot be empty"
        
        # Validate array size (keep visualization readable)
        if len(arr) > 20:
            return None, None, "Error: Please limit array to 20 elements for clear visualization"
        
        # CRITICAL: Check if array is sorted
        # Binary search ONLY works on sorted arrays
        if arr != sorted(arr):
            return None, None, "Error: Array must be sorted in ascending order for binary search to work"
        
        # All validation passed
        return arr, target, None
        
    except ValueError:
        return None, None, "Error: Please enter valid integers only (no letters or symbols)"


def search(array_str, target_str):
    """
    Main search function that coordinates the entire process.
    
    This function:
    1. Validates user input
    2. Executes the binary search algorithm
    3. Generates the visualization
    4. Formats the output for display
    
    Args:
        array_str: Comma-separated string of integers from user
        target_str: Target value string from user
    
    Returns:
        Tuple of (figure, result_text, steps_text)
        - figure: Matplotlib visualization
        - result_text: Summary of search results
        - steps_text: Detailed step-by-step breakdown
    """
    # Step 1: Validate and parse input
    arr, target, error = validate_input(array_str, target_str)
    
    if error:
        # Create error visualization
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.text(0.5, 0.5, error, ha='center', va='center', 
                fontsize=14, color='red', transform=ax.transAxes, wrap=True)
        ax.axis('off')
        plt.tight_layout()
        return fig, error, ""
    
    # Step 2: Execute binary search
    result, steps = binary_search(arr, target)
    
    # Step 3: Generate visualization of the final step
    is_found = (result != -1)
    fig = visualize(arr, steps[-1], is_found)
    
    # Step 4: Format result message
    if result != -1:
        result_msg = f"Success! Target {target} found at index {result}"
        result_msg += f"\n\nThe algorithm made {len(steps)} comparison(s) to find the target."
    else:
        result_msg = f"Target {target} was not found in the array"
        result_msg += f"\n\nThe algorithm made {len(steps)} comparison(s) before determining the target is not present."
    
    # Add efficiency comparison
    max_comparisons = int(np.log2(len(arr))) + 1 if len(arr) > 0 else 0
    result_msg += f"\n\nFor an array of size {len(arr)}:"
    result_msg += f"\n- Binary Search: {len(steps)} comparisons (O(log n))"
    result_msg += f"\n- Linear Search would need: up to {len(arr)} comparisons (O(n))"
    result_msg += f"\n- Efficiency gain: {((len(arr) - len(steps)) / len(arr) * 100):.1f}% fewer comparisons"
    
    # Step 5: Format detailed step-by-step execution
    steps_text = "### How the Algorithm Works:\n\n"
    steps_text += "Each step shows the current search boundaries and which element is being checked.\n\n"
    
    for i, step in enumerate(steps, 1):
        steps_text += f"**Step {i}:**\n"
        steps_text += f"- Search range: index {step['low']} to {step['high']}\n"
        steps_text += f"- Midpoint: index {step['mid']}\n"
        steps_text += f"- Value at midpoint: {step['value']}\n"
        
        # Explain what happens next
        if i == len(steps) and is_found:
            steps_text += f"- Result: {step['value']} equals {target} - Found it!\n"
        elif i < len(steps):
            next_step = steps[i]
            if step['value'] < target:
                steps_text += f"- Decision: {step['value']} < {target}, so search the right half\n"
                steps_text += f"- Next search range: index {next_step['low']} to {next_step['high']}\n"
            else:
                steps_text += f"- Decision: {step['value']} > {target}, so search the left half\n"
                steps_text += f"- Next search range: index {next_step['low']} to {next_step['high']}\n"
        elif not is_found:
            steps_text += f"- Decision: Search space exhausted - target not in array\n"
        
        steps_text += "\n"
    
    return fig, result_msg, steps_text


# Create the Gradio interface
with gr.Blocks(title="Binary Search Visualizer", theme=gr.themes.Soft()) as app:
    
    # Header section
    gr.Markdown("""
    # Binary Search Algorithm Visualizer
    
    **Learn how binary search efficiently finds elements in sorted arrays**
    
    Binary search is one of the fastest searching algorithms, reducing search time from O(n) to O(log n).
    This means searching 1,000,000 elements takes only ~20 comparisons instead of up to 1,000,000!
    """)
    
    # Instructions section
    gr.Markdown("""
    ### How to Use This Tool:
    
    1. **Enter a sorted array** of numbers separated by commas (e.g., `1, 3, 5, 7, 9, 11, 13`)
    2. **Enter the target value** you want to search for (e.g., `7`)
    3. Click **"Run Binary Search"** to see the algorithm in action
    4. Watch how the algorithm narrows down the search space step by step
    
    **Important:** The array must be sorted in ascending order for binary search to work correctly!
    """)
    
    # Input section
    with gr.Row():
        array_input = gr.Textbox(
            label="Sorted Array (comma-separated integers)",
            placeholder="Enter sorted numbers like: 1, 3, 5, 7, 9, 11, 13",
            value="1, 3, 5, 7, 9, 11, 13",
            info="Enter up to 20 numbers in ascending order"
        )
        target_input = gr.Textbox(
            label="Target Value",
            placeholder="Enter the number to search for",
            value="7",
            info="This is the value the algorithm will try to find"
        )
    
    # Search button
    search_btn = gr.Button("Run Binary Search", variant="primary", size="lg")
    
    # Output section
    gr.Markdown("### Results:")
    
    plot_output = gr.Plot(label="Visual Representation")
    
    with gr.Row():
        with gr.Column():
            result_output = gr.Markdown(label="Search Summary")
        with gr.Column():
            gr.Markdown("""
            **Legend:**
            - **L** = Low pointer (red) - start of search range
            - **H** = High pointer (red) - end of search range  
            - **M** = Midpoint (blue) - currently checking this element
            - **Green** = Target found!
            - **Gray** = Not currently being examined
            """)
    
    steps_output = gr.Markdown(label="Step-by-Step Breakdown")
    
    # Educational footer
    gr.Markdown("""
    ---
    
    ### Why Binary Search is Powerful:
    
    Binary search eliminates half of the remaining elements with each comparison. This makes it extremely efficient:
    - Array of 10 elements: max 4 comparisons
    - Array of 100 elements: max 7 comparisons  
    - Array of 1,000 elements: max 10 comparisons
    - Array of 1,000,000 elements: max 20 comparisons
    
    **Time Complexity:** O(log n) - logarithmic growth  
    **Space Complexity:** O(1) - constant extra space  
    **Requirement:** Array must be sorted
    
    ---
    
    *Created for CISC-121 | Queen's University | Joshua M. Ranin (20457769)*
    """)
    
    # Connect button to search function
    search_btn.click(
        fn=search,
        inputs=[array_input, target_input],
        outputs=[plot_output, result_output, steps_output]
    )


# Launch the application
if __name__ == "__main__":
    app.launch()