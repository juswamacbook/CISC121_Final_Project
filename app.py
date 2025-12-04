"""
Binary Search Visualizer
"""

import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, target):
    steps = []
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        steps.append({'low': low, 'high': high, 'mid': mid, 'value': arr[mid]})
        
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, steps

def visualize(arr, step):
    fig, ax = plt.subplots(figsize=(10, 4))
    
    colors = ['#d3d3d3'] * len(arr)
    colors[step['low']] = '#ff4444'
    colors[step['high']] = '#ff4444'
    colors[step['mid']] = '#4444ff'
    
    ax.bar(range(len(arr)), arr, color=colors, edgecolor='black', width=0.8)
    
    for i, val in enumerate(arr):
        ax.text(i, val + 0.3, str(val), ha='center', fontsize=11)
    
    ax.text(step['low'], -1.5, 'L', ha='center', fontsize=10, color='#ff4444')
    ax.text(step['high'], -1.5, 'H', ha='center', fontsize=10, color='#ff4444')
    ax.text(step['mid'], arr[step['mid']] + 1, 'M', ha='center', fontsize=10, color='#4444ff')
    
    ax.set_ylim(-2, max(arr) + 2)
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title(f"mid = {step['mid']}, value = {step['value']}")
    ax.grid(alpha=0.2)
    
    plt.tight_layout()
    return fig

def search(array_str, target_str):
    try:
        arr = [int(x.strip()) for x in array_str.split(',')]
        target = int(target_str)
        
        if not arr:
            return None, "Array cannot be empty", ""
        
        if arr != sorted(arr):
            return None, "Array must be sorted", ""
        
        result, steps = binary_search(arr, target)
        fig = visualize(arr, steps[-1])
        
        if result != -1:
            msg = f"Found at index {result}"
        else:
            msg = "Not found"
        
        msg += f"\nSteps: {len(steps)}"
        
        details = ""
        for i, step in enumerate(steps, 1):
            details += f"Step {i}: mid={step['mid']}, value={step['value']}\n"
        
        return fig, msg, details
        
    except ValueError:
        return None, "Invalid input", ""

with gr.Blocks() as app:
    gr.Markdown("# Binary Search Visualizer")
    
    with gr.Row():
        array_input = gr.Textbox(
            label="Array (comma-separated)",
            placeholder="1, 3, 5, 7, 9",
            value="1, 3, 5, 7, 9, 11, 13"
        )
        target_input = gr.Textbox(
            label="Target",
            placeholder="7",
            value="7"
        )
    
    search_btn = gr.Button("Search")
    
    plot_output = gr.Plot(label="Visualization")
    result_output = gr.Markdown()
    steps_output = gr.Markdown()
    
    search_btn.click(
        fn=search,
        inputs=[array_input, target_input],
        outputs=[plot_output, result_output, steps_output]
    )

if __name__ == "__main__":
    app.launch()