"""
Binary Search Algorithm Visualizer
CISC-121 Final Project
Author: Joshua M.Ranin
Student ID: 20457769
"""

import gradio as gr
import time
import random
from typing import List, Tuple, Optional, Dict
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import colors
import numpy as np

# Color scheme for visualization
COLORS = {
    'default': '#E0E0E0',
    'boundary': '#FF6B6B',      # Red for low/high boundaries
    'midpoint': '#4D96FF',      # Blue for current midpoint
    'found': '#6BCF7F',         # Green for found element
    'searched': '#FFD93D',      # Yellow for already searched
    'text': '#2C3E50',
    'background': '#FFFFFF',
    'grid': '#B0BEC5'
}

def validate_and_parse_input(array_str: str, target_str: str) -> Tuple[Optional[List[int]], Optional[int], Optional[str]]:
    """
    Validate and parse user input.
    
    Args:
        array_str: Comma-separated string of numbers
        target_str: String representation of target number
    
    Returns:
        Tuple of (array, target, error_message)
    """
    # Check for empty inputs
    if not array_str.strip():
        return None, None, "Please enter an array of numbers."
    
    if not target_str.strip():
        return None, None, "Please enter a target value."
    
    try:
        # Parse array
        array = []
        for item in array_str.split(','):
            item = item.strip()
            if item:
                array.append(int(item))
        
        # Check array size
        if len(array) == 0:
            return None, None, "Array cannot be empty."
        if len(array) > 20:
            return None, None, "Array size limited to 20 elements for better visualization."
        
        # Parse target
        target = int(target_str.strip())
        
        # Check if array is sorted
        if array != sorted(array):
            return array, target, "Warning: Array is not sorted. Binary search requires sorted input."
        
        return array, target, None
        
    except ValueError:
        return None, None, "Please enter valid integers only."

def binary_search_with_steps(arr: List[int], target: int) -> Tuple[Optional[int], List[Dict], int]:
    """
    Perform binary search and record each step for visualization.
    
    Args:
        arr: Sorted list of integers
        target: Integer to search for
    
    Returns:
        Tuple of (found_index, steps_list, comparisons_made)
    """
    steps = []
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        # Record current state
        step_info = {
            'low': low,
            'high': high,
            'mid': mid,
            'low_value': arr[low],
            'high_value': arr[high],
            'mid_value': arr[mid],
            'target': target,
            'comparison': None,
            'action': None,
            'found': False
        }
        
        # Compare and decide next action
        if arr[mid] == target:
            step_info['comparison'] = f"arr[{mid}] = {arr[mid]} == {target}"
            step_info['action'] = "Target found!"
            step_info['found'] = True
            steps.append(step_info)
            return mid, steps, comparisons
            
        elif arr[mid] < target:
            step_info['comparison'] = f"arr[{mid}] = {arr[mid]} < {target}"
            step_info['action'] = f"Search right half: low = {mid} + 1 = {mid + 1}"
            low = mid + 1
            
        else:
            step_info['comparison'] = f"arr[{mid}] = {arr[mid]} > {target}"
            step_info['action'] = f"Search left half: high = {mid} - 1 = {mid - 1}"
            high = mid - 1
        
        steps.append(step_info)
    
    # Target not found
    return -1, steps, comparisons

def create_visualization(arr: List[int], current_step: Dict, step_number: int, total_steps: int) -> plt.Figure:
    """
    Create a visualization of the current search state.
    
    Args:
        arr: The array being searched
        current_step: Dictionary with current step information
        step_number: Current step number (1-indexed)
        total_steps: Total number of steps
    
    Returns:
        Matplotlib figure object
    """
    n = len(arr)
    fig, ax = plt.subplots(figsize=(max(10, n * 1.5), 6))
    
    # Set background color
    fig.patch.set_facecolor(COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    # Create bars for array elements
    x_positions = np.arange(n)
    bar_colors = [COLORS['default']] * n
    bar_heights = arr
    
    # Color code elements based on current state
    low = current_step['low']
    high = current_step['high']
    mid = current_step['mid']
    
    # Color the search boundaries
    bar_colors[low] = COLORS['boundary']
    bar_colors[high] = COLORS['boundary']
    
    # Color the midpoint
    bar_colors[mid] = COLORS['midpoint']
    
    # If found, highlight the found element
    if current_step.get('found', False):
        bar_colors[mid] = COLORS['found']
    
    # Create bars
    bars = ax.bar(x_positions, bar_heights, color=bar_colors, edgecolor='black', linewidth=2)
    
    # Add value labels on top of bars
    for i, (bar, value) in enumerate(zip(bars, bar_heights)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                str(value), ha='center', va='bottom', fontsize=14, fontweight='bold')
    
    # Add index labels below bars
    ax.set_xticks(x_positions)
    ax.set_xticklabels([str(i) for i in range(n)], fontsize=12)
    
    # Add pointers
    pointer_offset = max(arr) * 0.1
    
    # Low pointer
    ax.annotate('low', xy=(low, 0), xytext=(low, -pointer_offset),
                ha='center', va='top', fontsize=12, fontweight='bold',
                color=COLORS['boundary'],
                arrowprops=dict(arrowstyle='->', color=COLORS['boundary'], lw=2))
    
    # High pointer
    ax.annotate('high', xy=(high, 0), xytext=(high, -pointer_offset),
                ha='center', va='top', fontsize=12, fontweight='bold',
                color=COLORS['boundary'],
                arrowprops=dict(arrowstyle='->', color=COLORS['boundary'], lw=2))
    
    # Mid pointer
    ax.annotate('mid', xy=(mid, arr[mid]), xytext=(mid, arr[mid] + pointer_offset),
                ha='center', va='bottom', fontsize=12, fontweight='bold',
                color=COLORS['midpoint'],
                arrowprops=dict(arrowstyle='->', color=COLORS['midpoint'], lw=2))
    
    # Add title and labels
    ax.set_title(f'Binary Search Visualization - Step {step_number}/{total_steps}', 
                fontsize=16, fontweight='bold', pad=20, color=COLORS['text'])
    ax.set_xlabel('Array Index', fontsize=14, color=COLORS['text'])
    ax.set_ylabel('Value', fontsize=14, color=COLORS['text'])
    
    # Add grid for better readability
    ax.grid(True, alpha=0.3, linestyle='--', color=COLORS['grid'])
    
    # Set y-limit for better visualization
    ax.set_ylim(0, max(arr) * 1.2)
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    return fig

def generate_example_array() -> str:
    """Generate a random sorted array for example."""
    n = random.randint(5, 12)
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    arr = [start + i * step for i in range(n)]
    return ', '.join(map(str, arr))

def format_step_info(step: Dict, step_num: int, total_steps: int) -> str:
    """Format step information for display."""
    info = f"**Step {step_num}/{total_steps}:**\n\n"
    info += f"• low = {step['low']} (value: {step['low_value']})\n"
    info += f"• high = {step['high']} (value: {step['high_value']})\n"
    info += f"• mid = ({step['low']} + {step['high']}) // 2 = {step['mid']} (value: {step['mid_value']})\n\n"
    
    if 'comparison' in step:
        info += f"**Comparison:** {step['comparison']}\n\n"
    
    if 'action' in step:
        info += f"**Action:** {step['action']}\n"
    
    if step.get('found', False):
        info += "\n🎯 **TARGET FOUND!** 🎯\n"
    
    return info

def run_binary_search(array_input: str, target_input: str) -> Tuple[plt.Figure, str, str, str]:
    """
    Main function to run binary search and generate output.
    
    Args:
        array_input: Comma-separated string of numbers
        target_input: String representation of target number
    
    Returns:
        Tuple of (visualization_figure, result_text, steps_text, metrics_text)
    """
    # Validate input
    arr, target, error = validate_and_parse_input(array_input, target_input)
    
    if error:
        # Create error visualization
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.text(0.5, 0.5, error, ha='center', va='center', fontsize=14, 
                color='red', transform=ax.transAxes, wrap=True)
        ax.axis('off')
        plt.tight_layout()
        
        return fig, f"❌ {error}", "", ""
    
    # Check if array is sorted (warning case)
    if arr != sorted(arr):
        warning = "⚠️ Array is not sorted. Results may be incorrect."
    else:
        warning = ""
    
    # Perform binary search
    result_index, steps, comparisons = binary_search_with_steps(arr, target)
    
    # Create visualization for the final step
    if steps:
        final_step = steps[-1]
        fig = create_visualization(arr, final_step, len(steps), len(steps))
    else:
        # Edge case: empty steps (shouldn't happen with valid input)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        plt.tight_layout()
    
    # Generate result text
    if result_index != -1:
        result_text = f"✅ **Found at index {result_index}** (value: {arr[result_index]})"
    else:
        result_text = "❌ **Target not found** in the array"
    
    # Generate steps text
    steps_text = ""
    for i, step in enumerate(steps, 1):
        steps_text += format_step_info(step, i, len(steps))
        if i < len(steps):
            steps_text += "---\n\n"
    
    # Generate metrics text
    n = len(arr)
    max_comparisons = int(np.floor(np.log2(n))) + 1 if n > 0 else 0
    
    metrics_text = f"""
    ## 📊 Algorithm Metrics
    
    **Array Statistics:**
    • Array size: {n} elements
    • Minimum value: {min(arr)}
    • Maximum value: {max(arr)}
    
    **Search Results:**
    • Target value: {target}
    • Comparisons made: {comparisons}
    • Maximum possible comparisons: {max_comparisons}
    
    **Complexity Analysis:**
    • Time Complexity: O(log n) = O(log₂{len(arr)}) ≈ O({np.log2(len(arr)):.2f})
    • Space Complexity: O(1) - constant extra space
    • Efficiency: {comparisons}/{n} = {comparisons/len(arr)*100:.1f}% of linear search comparisons
    """
    
    if warning:
        result_text = warning + "\n\n" + result_text
    
    return fig, result_text, steps_text, metrics_text

def create_interface():
    """Create the Gradio interface."""
    # CSS for styling
    css = """
    .gradio-container {
        max-width: 1200px !important;
        margin: auto !important;
    }
    .input-section {
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 2px solid #e9ecef;
    }
    .output-section {
        background: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #e9ecef;
    }
    .title {
        text-align: center;
        color: #2c3e50;
        margin-bottom: 30px;
    }
    .example-btn {
        background: #3498db !important;
        color: white !important;
        border: none !important;
    }
    .example-btn:hover {
        background: #2980b9 !important;
    }
    """
    
    with gr.Blocks(css=css, theme=gr.themes.Soft()) as app:
        # Title
        gr.Markdown("""
        # 🔍 Binary Search Algorithm Visualizer
        
        **CISC-121 Final Project** | *Visualize the binary search algorithm step by step*
        
        ---
        """, elem_classes="title")
        
        with gr.Row():
            with gr.Column(scale=2):
                # Input Section
                with gr.Group(elem_classes="input-section"):
                    gr.Markdown("## 📥 Input Parameters")
                    
                    with gr.Row():
                        array_input = gr.Textbox(
                            label="Sorted Array (comma-separated integers)",
                            placeholder="e.g., 1, 3, 5, 7, 9, 11",
                            value="1, 3, 5, 7, 9, 11",
                            elem_id="array_input"
                        )
                        
                        target_input = gr.Textbox(
                            label="Target Value",
                            placeholder="e.g., 7",
                            value="7",
                            elem_id="target_input"
                        )
                    
                    with gr.Row():
                        generate_btn = gr.Button(
                            "🎲 Generate Random Example", 
                            variant="secondary",
                            elem_classes="example-btn"
                        )
                        search_btn = gr.Button(
                            "🔍 Start Binary Search", 
                            variant="primary",
                            scale=2
                        )
                
                # How to Use Section
                with gr.Accordion("📖 How to Use", open=False):
                    gr.Markdown("""
                    **Instructions:**
                    1. Enter a **sorted array** of integers (comma-separated)
                    2. Enter a **target value** to search for
                    3. Click **"Start Binary Search"** to visualize the algorithm
                    
                    **Requirements:**
                    - Array must be sorted in ascending order
                    - Only integers are accepted
                    - Maximum 20 elements recommended for best visualization
                    
                    **Example:** Try searching for 7 in the array: 1, 3, 5, 7, 9, 11
                    """)
            
            with gr.Column(scale=1):
                # Color Legend
                with gr.Group(elem_classes="input-section"):
                    gr.Markdown("## 🎨 Visualization Legend")
                    
                    legend_html = f"""
                    <div style="background: white; padding: 15px; border-radius: 8px;">
                        <div style="display: flex; align-items: center; margin: 5px 0;">
                            <div style="width: 20px; height: 20px; background: {COLORS['boundary']}; margin-right: 10px; border: 1px solid black;"></div>
                            <span>Search Boundaries (low/high)</span>
                        </div>
                        <div style="display: flex; align-items: center; margin: 5px 0;">
                            <div style="width: 20px; height: 20px; background: {COLORS['midpoint']}; margin-right: 10px; border: 1px solid black;"></div>
                            <span>Current Midpoint</span>
                        </div>
                        <div style="display: flex; align-items: center; margin: 5px 0;">
                            <div style="width: 20px; height: 20px; background: {COLORS['found']}; margin-right: 10px; border: 1px solid black;"></div>
                            <span>Found Element</span>
                        </div>
                        <div style="display: flex; align-items: center; margin: 5px 0;">
                            <div style="width: 20px; height: 20px; background: {COLORS['default']}; margin-right: 10px; border: 1px solid black;"></div>
                            <span>Other Elements</span>
                        </div>
                    </div>
                    """
                    gr.HTML(legend_html)
        
        # Output Section
        with gr.Group(elem_classes="output-section"):
            gr.Markdown("## 📊 Search Results")
            
            with gr.Row():
                with gr.Column(scale=2):
                    # Visualization
                    visualization = gr.Plot(
                        label="Binary Search Visualization",
                        elem_id="visualization"
                    )
                    
                    # Result
                    result_output = gr.Markdown(
                        label="Search Result",
                        elem_id="result_output"
                    )
                
                with gr.Column(scale=1):
                    # Step-by-step details
                    steps_output = gr.Markdown(
                        label="Step-by-Step Execution",
                        elem_id="steps_output"
                    )
            
            # Metrics
            metrics_output = gr.Markdown(
                label="Algorithm Metrics",
                elem_id="metrics_output"
            )
        
        # Button Actions
        search_btn.click(
            fn=run_binary_search,
            inputs=[array_input, target_input],
            outputs=[visualization, result_output, steps_output, metrics_output]
        )
        
        generate_btn.click(
            fn=generate_example_array,
            inputs=[],
            outputs=[array_input]
        )
        
        # Footer
        gr.Markdown("""
        ---
        
        **About Binary Search:**
        - **Time Complexity:** O(log n) - extremely efficient for large datasets
        - **Requirements:** Array must be sorted
        - **How it works:** Repeatedly divides search interval in half
        
        **Project Info:** CISC-121 Final Project | Queen's University
        """)
    
    return app

# Main execution
if __name__ == "__main__":
    # Create requirements.txt content reminder
    print("=" * 60)
    print("Binary Search Visualizer - CISC-121 Final Project")
    print("=" * 60)
    print("\nTo run this application:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Run the app: python app.py")
    print("3. Open browser to: http://localhost:7860")
    print("\nRequired packages (save to requirements.txt):")
    print("gradio>=4.0.0")
    print("matplotlib>=3.5.0")
    print("numpy>=1.21.0")
    print("=" * 60)
    
    # Launch the app
    app = create_interface()
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True,
        debug=True
    )