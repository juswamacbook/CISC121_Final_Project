"""
Binary Search Algorithm Visualizer
This program implements the binary search algorithm with interactive visualization
using Gradio. It demonstrates how binary search efficiently finds elements in a
sorted array by repeatedly dividing the search space in half.
Author: Joshua M. Ranin
Student ID: 20457769
Date: December 2025
Course: CISC-121
"""

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np
import random


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
            'comparison': comparisons,
            'eliminated': low + (len(arr) - high - 1)  # Track eliminated elements
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


def visualize(arr, step, is_found=False, step_number=1, total_steps=1):
    """
    Creates a clean bar chart visualization showing the search process.
    
    Uses a horizontal bar layout with clear color coding to show which elements
    are being examined and which have been eliminated.
    
    Args:
        arr: The array being searched
        step: Dictionary with current low, high, mid pointers and values
        is_found: Boolean indicating whether target was found
        step_number: Current step number
        total_steps: Total number of steps
    
    Returns:
        Matplotlib figure object ready to display
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    n = len(arr)
    low_idx = step['low']
    high_idx = step['high']
    mid_idx = step['mid']
    
    # Determine colors for each bar
    colors = []
    for i in range(n):
        if i < low_idx or i > high_idx:
            # Eliminated - gray and faded
            colors.append('#d3d3d3')
        elif i == mid_idx:
            # Current midpoint - cyan for checking, green if found
            colors.append('#00ff88' if is_found else '#00bfff')
        elif i == low_idx or i == high_idx:
            # Boundaries - orange
            colors.append('#ff8c42')
        else:
            # Active search space - yellow
            colors.append('#ffd93d')
    
    # Create horizontal bars
    y_positions = np.arange(n)
    bars = ax.barh(y_positions, arr, color=colors, edgecolor='black', linewidth=2, height=0.7)
    
    # Add value labels at the end of bars
    for i, (bar, value) in enumerate(zip(bars, arr)):
        ax.text(bar.get_width() + max(arr) * 0.02, bar.get_y() + bar.get_height()/2,
                f'{value}', va='center', fontsize=12, fontweight='bold')
    
    # Add index labels on the left
    ax.set_yticks(y_positions)
    ax.set_yticklabels([f'[{i}]' for i in range(n)], fontsize=11)
    
    # Add pointer annotations
    pointer_offset = max(arr) * 0.15
    
    # Low pointer
    if low_idx <= high_idx:
        ax.annotate('LOW', xy=(0, low_idx), xytext=(-pointer_offset, low_idx),
                   ha='right', va='center', fontsize=11, fontweight='bold',
                   color='#ff8c42',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#ff8c42', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', color='#ff8c42', lw=2))
    
    # High pointer
    if low_idx <= high_idx:
        ax.annotate('HIGH', xy=(0, high_idx), xytext=(-pointer_offset, high_idx),
                   ha='right', va='center', fontsize=11, fontweight='bold',
                   color='#ff8c42',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='#ff8c42', alpha=0.3),
                   arrowprops=dict(arrowstyle='->', color='#ff8c42', lw=2))
    
    # Mid pointer
    mid_color = '#00ff88' if is_found else '#00bfff'
    mid_label = 'FOUND!' if is_found else 'MID'
    ax.annotate(mid_label, xy=(arr[mid_idx], mid_idx), 
               xytext=(arr[mid_idx] + pointer_offset * 2, mid_idx),
               ha='left', va='center', fontsize=12, fontweight='bold',
               color=mid_color,
               bbox=dict(boxstyle='round,pad=0.5', facecolor=mid_color, alpha=0.3),
               arrowprops=dict(arrowstyle='->', color=mid_color, lw=3))
    
    # Configure axes
    ax.set_xlabel('Value', fontsize=13, fontweight='bold')
    ax.set_ylabel('Index', fontsize=13, fontweight='bold')
    
    # Title with status
    if is_found:
        title_color = '#00aa00'
        title_text = f'FOUND! Target at index {mid_idx} (value = {step["value"]})'
    else:
        title_color = '#333333'
        title_text = f'Step {step_number}/{total_steps}: Checking index {mid_idx} (value = {step["value"]})'
    
    ax.set_title(title_text, fontsize=14, fontweight='bold', pad=20, color=title_color)
    
    ax.grid(axis='x', alpha=0.3, linestyle='--')
    ax.set_xlim(0, max(arr) * 1.3)
    
    # Add legend
    legend_elements = [
        plt.Rectangle((0,0),1,1, fc='#00bfff', ec='black', lw=2, label='Current Check (MID)'),
        plt.Rectangle((0,0),1,1, fc='#ff8c42', ec='black', lw=2, label='Search Boundaries (LOW/HIGH)'),
        plt.Rectangle((0,0),1,1, fc='#ffd93d', ec='black', lw=2, label='Active Search Space'),
        plt.Rectangle((0,0),1,1, fc='#d3d3d3', ec='black', lw=2, label='Eliminated'),
    ]
    if is_found:
        legend_elements[0] = plt.Rectangle((0,0),1,1, fc='#00ff88', ec='black', lw=2, label='FOUND!')
    
    ax.legend(handles=legend_elements, loc='upper right', fontsize=10, framealpha=0.9)
    
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


def generate_random_array():
    """Generate a random sorted array for demonstration."""
    size = random.randint(6, 12)
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    arr = [start + i * step for i in range(size)]
    return ', '.join(map(str, arr))


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
    
    # For "not found" cases, create a special visualization
    if not is_found:
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Show the final state with clear "NOT FOUND" message
        n = len(arr)
        y_positions = np.arange(n)
        colors = ['#ffcccc'] * n  # Light red for all elements
        
        bars = ax.barh(y_positions, arr, color=colors, edgecolor='#cc0000', linewidth=2, height=0.7)
        
        # Add value labels
        for i, (bar, value) in enumerate(zip(bars, arr)):
            ax.text(bar.get_width() + max(arr) * 0.02, bar.get_y() + bar.get_height()/2,
                    f'{value}', va='center', fontsize=12, fontweight='bold')
        
        # Add index labels
        ax.set_yticks(y_positions)
        ax.set_yticklabels([f'[{i}]' for i in range(n)], fontsize=11)
        
        # Big "NOT FOUND" overlay
        ax.text(max(arr) * 0.5, n/2, 'TARGET NOT FOUND', 
            ha='center', va='center', fontsize=32, fontweight='bold',
            color='#cc0000', alpha=0.7,
            bbox=dict(boxstyle='round,pad=1', facecolor='white', 
                        edgecolor='#cc0000', linewidth=4, alpha=0.9))
        
        ax.set_xlabel('Value', fontsize=13, fontweight='bold')
        ax.set_ylabel('Index', fontsize=13, fontweight='bold')
        ax.set_title(f'Search Complete: Target {target} not found after {len(steps)} comparisons', 
                    fontsize=14, fontweight='bold', pad=20, color='#cc0000')
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        ax.set_xlim(0, max(arr) * 1.3)
        
        plt.tight_layout()
    else:
        fig = visualize(arr, steps[-1], is_found, len(steps), len(steps))
    
    # Step 4: Format result message
    result_msg = "## Search Complete\n\n"
    
    if result != -1:
        result_msg += f"**Status:** Target found\n\n"
        result_msg += f"**Location:** Index {result} (value = {arr[result]})\n\n"
        result_msg += f"**Efficiency:** Found in {len(steps)} comparison(s)\n\n"
    else:
        result_msg += f"**Status:** Target not found\n\n"
        result_msg += f"**Comparisons:** {len(steps)} check(s) performed\n\n"
        result_msg += f"**Conclusion:** {target} is not present in this array\n\n"
    
    # Add efficiency metrics
    max_comparisons = int(np.log2(len(arr))) + 1 if len(arr) > 0 else 0
    efficiency = ((len(arr) - len(steps)) / len(arr) * 100) if len(arr) > 0 else 0
    
    result_msg += "### Algorithm Performance\n\n"
    result_msg += f"- Array size: {len(arr)} elements\n"
    result_msg += f"- Comparisons made: {len(steps)}\n"
    result_msg += f"- Maximum possible: {max_comparisons}\n"
    result_msg += f"- Efficiency gain: {efficiency:.1f}% fewer checks than linear search\n"
    
    # Step 5: Format detailed step-by-step execution
    steps_text = "## Step-by-Step Execution\n\n"
    
    for i, step in enumerate(steps, 1):
        steps_text += f"### Step {i}\n\n"
        steps_text += f"**Search Range:** indices {step['low']} to {step['high']} "
        steps_text += f"({step['high'] - step['low'] + 1} elements)\n\n"
        steps_text += f"**Midpoint:** index {step['mid']}\n\n"
        steps_text += f"**Value checked:** {step['value']}\n\n"
        
        # Explain what happens next
        if i == len(steps) and is_found:
            steps_text += f"**Result:** {step['value']} = {target} → **Target found!**\n\n"
        elif i < len(steps):
            next_step = steps[i]
            if step['value'] < target:
                steps_text += f"**Decision:** {step['value']} < {target}\n\n"
                steps_text += f"→ Search RIGHT half (indices {next_step['low']} to {next_step['high']})\n\n"
            else:
                steps_text += f"**Decision:** {step['value']} > {target}\n\n"
                steps_text += f"→ Search LEFT half (indices {next_step['low']} to {next_step['high']})\n\n"
        elif not is_found:
            steps_text += f"**Decision:** Search space exhausted → **Target not found**\n\n"
        
        steps_text += "---\n\n"
    
    return fig, result_msg, steps_text



with gr.Blocks(title="Binary Search Visualizer") as app:
    # Create the Gradio interface with custom CSS
    css = """
    .gradio-container {
        font-family: 'Inter', sans-serif;
    }
    .header {
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    """
    # Custom header
    gr.HTML("""
    <div class="header">
        <h1 style="margin:0; font-size: 2.5rem;">Binary Search Visualizer</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">
            Watch how binary search finds elements with logarithmic efficiency
        </p>
    </div>
    """)
    
    # Instructions in colored box
    gr.HTML("""
    <div class="info-box">
        <h3 style="margin-top:0;">How to Use</h3>
        <ol style="margin-bottom:0;">
            <li>Enter a <strong>sorted array</strong> of numbers (comma-separated)</li>
            <li>Enter the <strong>target value</strong> you want to find</li>
            <li>Click <strong>"Search"</strong> or try <strong>"Random Example"</strong></li>
            <li>Watch the unique circular visualization show the algorithm in action!</li>
        </ol>
    </div>
    """)
    
    # Input section with two columns
    with gr.Row():
        with gr.Column(scale=3):
            array_input = gr.Textbox(
                label="Sorted Array",
                placeholder="Example: 2, 5, 8, 12, 16, 23, 38, 45, 56, 67",
                value="2, 5, 8, 12, 16, 23, 38, 45, 56, 67",
                info="Enter numbers in ascending order, separated by commas"
            )
        with gr.Column(scale=1):
            target_input = gr.Textbox(
                label="Target Value",
                placeholder="23",
                value="23",
                info="Number to search for"
            )
    
    # Buttons
    with gr.Row():
        random_btn = gr.Button("Generate Random Example", variant="secondary", size="lg")
        search_btn = gr.Button("Search", variant="primary", size="lg")
    
    # Output section
    plot_output = gr.Plot(label="Algorithm Visualization")
    
    with gr.Row():
        result_output = gr.Markdown(label="Results")
        steps_output = gr.Markdown(label="Execution Details")
    
    # Educational footer
    gr.HTML("""
    <div class="info-box" style="margin-top: 2rem;">
        <h3>Why Binary Search is Powerful</h3>
        <p>
            Binary search eliminates <strong>half</strong> of the remaining elements with each step.
            This exponential reduction means:
        </p>
        <ul>
            <li>10 elements → max 4 comparisons</li>
            <li>100 elements → max 7 comparisons</li>
            <li>1,000,000 elements → max 20 comparisons!</li>
        </ul>
        <p style="margin-bottom:0;">
            <strong>Time Complexity:</strong> O(log n) | 
            <strong>Space Complexity:</strong> O(1) | 
            <strong>Requirement:</strong> Sorted array
        </p>
    </div>
    """)
    
    gr.Markdown("*CISC-121 Final Project | Joshua M. Ranin (20457769) | Queen's University*")
    
    # Connect buttons
    search_btn.click(
        fn=search,
        inputs=[array_input, target_input],
        outputs=[plot_output, result_output, steps_output]
    )
    
    random_btn.click(
        fn=generate_random_array,
        inputs=[],
        outputs=[array_input]
    )


# Launch the application
if __name__ == "__main__":
    app.launch()