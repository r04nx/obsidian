#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

# Define the benchmark data
algorithms = ['Huffman', 'RLE', 'LZW', 'DEFLATE']
compression_ratios = [1.17, 0.62, 0.85, 2.03]  # higher is better
compression_times = [2.83, 1.03, 4.6, 0.25]    # in seconds, lower is better
decompression_times = [7.04, 2.73, 2.88, 0.02] # in seconds, lower is better

# Set the style for the plots
sns.set_style("whitegrid")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 12,
    'figure.figsize': (10, 6),
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

# Colors for the algorithms
colors = sns.color_palette("viridis", len(algorithms))

# 1. Bar Chart for Compression Ratios (higher is better)
plt.figure(figsize=(12, 7))
bars = plt.bar(algorithms, compression_ratios, color=colors, alpha=0.8)
plt.title('Compression Ratio Comparison (Higher is Better)', fontsize=16, fontweight='bold')
plt.xlabel('Compression Algorithm', fontsize=14)
plt.ylabel('Compression Ratio', fontsize=14)
plt.ylim(0, max(compression_ratios) + 0.5)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{height:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add a horizontal line at ratio=1 (no compression)
plt.axhline(y=1, color='red', linestyle='--', alpha=0.7, label='No Compression (1:1)')
plt.legend()

# Annotate the best algorithm
best_ratio_idx = np.argmax(compression_ratios)
plt.annotate(f'Best: {algorithms[best_ratio_idx]}',
             xy=(best_ratio_idx, compression_ratios[best_ratio_idx]),
             xytext=(best_ratio_idx, compression_ratios[best_ratio_idx] + 0.4),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             ha='center', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('compression_ratio_comparison.png')

# 2. Bar Chart for Compression Times (lower is better)
plt.figure(figsize=(12, 7))
bars = plt.bar(algorithms, compression_times, color=colors, alpha=0.8)
plt.title('Compression Time Comparison (Lower is Better)', fontsize=16, fontweight='bold')
plt.xlabel('Compression Algorithm', fontsize=14)
plt.ylabel('Compression Time (seconds)', fontsize=14)
plt.ylim(0, max(compression_times) + 1)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
             f'{height:.2f}s', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Annotate the best algorithm
best_time_idx = np.argmin(compression_times)
plt.annotate(f'Best: {algorithms[best_time_idx]}',
             xy=(best_time_idx, compression_times[best_time_idx]),
             xytext=(best_time_idx, compression_times[best_time_idx] + 0.9),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             ha='center', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('compression_time_comparison.png')

# 3. Bar Chart for Decompression Times (lower is better)
plt.figure(figsize=(12, 7))
bars = plt.bar(algorithms, decompression_times, color=colors, alpha=0.8)
plt.title('Decompression Time Comparison (Lower is Better)', fontsize=16, fontweight='bold')
plt.xlabel('Compression Algorithm', fontsize=14)
plt.ylabel('Decompression Time (seconds)', fontsize=14)
plt.ylim(0, max(decompression_times) + 1)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.2,
             f'{height:.2f}s', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Annotate the best algorithm
best_decomp_idx = np.argmin(decompression_times)
plt.annotate(f'Best: {algorithms[best_decomp_idx]}',
             xy=(best_decomp_idx, decompression_times[best_decomp_idx]),
             xytext=(best_decomp_idx, decompression_times[best_decomp_idx] + 0.9),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
             ha='center', fontsize=12, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('decompression_time_comparison.png')

# 4. Scatter plot of compression time vs. ratio
plt.figure(figsize=(12, 7))
plt.scatter(compression_times, compression_ratios, s=200, c=colors, alpha=0.8)

# Label each point with algorithm name
for i, alg in enumerate(algorithms):
    plt.annotate(alg, (compression_times[i], compression_ratios[i]), 
                 xytext=(10, 5), textcoords='offset points',
                 fontsize=12, fontweight='bold')

plt.title('Compression Time vs. Ratio', fontsize=16, fontweight='bold')
plt.xlabel('Compression Time (seconds, lower is better)', fontsize=14)
plt.ylabel('Compression Ratio (higher is better)', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('compression_time_vs_ratio.png')

# 5. Radar Chart for Overall Comparison
def radar_factory(num_vars, frame='circle'):
    """Create a radar chart with `num_vars` axes."""
    # Calculate evenly-spaced axis angles
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    
    class RadarAxes(PolarAxes):
        name = 'radar'
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')
            
        def fill(self, *args, closed=True, **kwargs):
            """Override fill so that line is closed by default"""
            return super().fill(closed=closed, *args, **kwargs)
            
        def plot(self, *args, **kwargs):
            """Override plot so that line is closed by default"""
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)
                
        def _close_line(self, line):
            x, y = line.get_data()
            # FIXME: markers at x[0], y[0] get doubled-up
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)
                
        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)
            
        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars,
                                      radius=.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)
                
        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine_type = 'circle'
                verts = unit_poly_verts(num_vars)
                verts.append(verts[0])
                path = Path(verts)
                spine = Spine(self, spine_type, path)
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)
    
    register_projection(RadarAxes)
    return theta

def unit_poly_verts(num_vars):
    """Return vertices of polygon for radar chart"""
    theta = np.linspace(0, 2*np.pi, num_vars, endpoint=False)
    verts = list(zip(np.sin(theta), np.cos(theta)))
    return verts

# Prepare data for radar chart
categories = ['Compression\nRatio', 'Compression\nSpeed', 'Decompression\nSpeed']
theta = radar_factory(len(categories), frame='polygon')

# Normalize data for radar chart (scale between 0 and 1, with 1 being best)
# For compression ratio, higher is better
norm_ratios = np.array(compression_ratios) / max(compression_ratios)
# For times, lower is better, so we invert
norm_comp_times = 1 - (np.array(compression_times) / max(compression_times))
norm_decomp_times = 1 - (np.array(decompression_times) / max(decompression_times))

radar_data = []
for i, alg in enumerate(algorithms):
    radar_data.append([norm_ratios[i], norm_comp_times[i], norm_decomp_times[i]])

fig, ax = plt.subplots(figsize=(9, 9), subplot_kw=dict(projection='radar'))
for i, (alg, data) in enumerate(zip(algorithms, radar_data)):
    line = ax.plot(theta, data, label=alg)
    ax.fill(theta, data, alpha=0.25)

ax.set_varlabels(categories)
plt.title('Algorithm Performance Comparison', fontsize=16, fontweight='bold', y=1.1)
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.tight_layout()
plt.savefig('algorithm_performance_radar.png')

# 6. Combined plot with all three metrics
# Create a dataframe for easier plotting
df = pd.DataFrame({
    'Algorithm': algorithms * 3,
    'Metric': ['Compression Ratio'] * 4 + ['Compression Time (s)'] * 4 + ['Decompression Time (s)'] * 4,
    'Value': compression_ratios + compression_times + decompression_times
})

# Create a function to add value labels
def add_value_labels(ax, is_h=False):
    for p in ax.patches:
        width = p.get_width() if is_h else p.get_height()
        x = p.get_x() + p.get_width() / 2 if not is_h else p.get_width() + 0.05
        y = p.get_y() + p.get_height() / 2 if is_h else p.get_height() + 0.05
        ax.annotate(f'{width:.2f}', (x, y), ha='center' if not is_h else 'left', va='bottom')

plt.figure(figsize=(15, 10))
# Use hue to distinguish between algorithms, and col to separate metrics
g = sns.catplot(
    data=df, kind="bar",
    x="Algorithm", y="Value", hue="Metric",
    palette="viridis", alpha=.8, height=6, aspect=1.5
)

g.set_axis_labels("", "Value")
g.legend.set_title("")
plt.title('Combined Compression Algorithm Performance Metrics', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('combined_performance_metrics.png')

print("All visualization charts have been generated and saved as PNG files.")

#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from math import pi

# Set the aesthetic style of the plots
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Sample data from compression benchmark results
# Replace this with data extraction from your benchmark results if needed
algorithms = ['Huffman', 'RLE', 'LZW', 'DEFLATE']
compression_ratios = [0.75, 0.65, 0.55, 0.45]  # Lower is better
compression_times = [35, 15, 45, 25]  # ms
decompression_times = [25, 10, 30, 20]  # ms

# Normalize the values for radar chart (higher is better)
max_comp_ratio = max(compression_ratios)
max_comp_time = max(compression_times)
max_decomp_time = max(decompression_times)

# For radar chart - invert values for compression ratio (lower is better)
# and for times (lower is better)
norm_comp_ratio = [1 - (cr / max_comp_ratio) for cr in compression_ratios]
norm_comp_time = [1 - (ct / max_comp_time) for ct in compression_times]
norm_decomp_time = [1 - (dt / max_decomp_time) for dt in decompression_times]

# Function to create and save bar charts
def create_bar_chart(data, labels, title, ylabel, filename, color='skyblue'):
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=labels, y=data, palette='viridis')
    
    # Add value labels on top of each bar
    for i, v in enumerate(data):
        ax.text(i, v + 0.01, f"{v:.2f}", ha='center')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.ylabel(ylabel)
    plt.xlabel('Compression Algorithm')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")

# Create bar charts
create_bar_chart(
    compression_ratios, 
    algorithms, 
    'Compression Ratio Comparison', 
    'Compression Ratio (lower is better)', 
    'compression_ratio_chart.png'
)

create_bar_chart(
    compression_times, 
    algorithms, 
    'Compression Time Comparison', 
    'Compression Time (ms, lower is better)', 
    'compression_time_chart.png'
)

create_bar_chart(
    decompression_times, 
    algorithms, 
    'Decompression Time Comparison', 
    'Decompression Time (ms, lower is better)', 
    'decompression_time_chart.png'
)

# Create radar chart for comprehensive comparison
def create_radar_chart(categories, values_by_algorithm, title, filename):
    # Number of variables
    N = len(categories)
    
    # Compute angle for each axis
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Close the loop
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Add category labels
    plt.xticks(angles[:-1], categories, size=12)
    
    # Set y-ticks
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75], ["0.25", "0.50", "0.75"], color="grey", size=10)
    plt.ylim(0, 1)
    
    # Plot data
    for i, algorithm in enumerate(algorithms):
        values = values_by_algorithm[i]
        values += values[:1]  # Close the loop
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=algorithm)
        ax.fill(angles, values, alpha=0.1)
    
    # Add legend
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    plt.title(title, size=16, fontweight='bold', y=1.1)
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")

# Prepare data for radar chart
categories = ['Compression Ratio', 'Compression Speed', 'Decompression Speed']
values_by_algorithm = [
    [norm_comp_ratio[i], norm_comp_time[i], norm_decomp_time[i]] 
    for i in range(len(algorithms))
]

create_radar_chart(
    categories,
    values_by_algorithm,
    'Comprehensive Compression Algorithm Comparison',
    'compression_radar_chart.png'
)

# Create a combined comparison visualization
def create_combined_chart(algorithms, comp_ratios, comp_times, decomp_times, filename):
    # Prepare data for combined chart
    data = {
        'Algorithm': algorithms * 3,
        'Value': comp_ratios + comp_times + decomp_times,
        'Metric': ['Compression Ratio'] * len(algorithms) + 
                 ['Compression Time (ms)'] * len(algorithms) + 
                 ['Decompression Time (ms)'] * len(algorithms)
    }
    df = pd.DataFrame(data)
    
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(x='Algorithm', y='Value', hue='Metric', data=df)
    
    plt.title('Combined Compression Algorithm Performance', fontsize=16, fontweight='bold')
    plt.ylabel('Value (lower is better for all metrics)')
    plt.legend(title='Metric')
    plt.tight_layout()
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved {filename}")

create_combined_chart(
    algorithms,
    compression_ratios,
    compression_times,
    decompression_times,
    'compression_combined_chart.png'
)

print("All visualization plots have been generated successfully!")

