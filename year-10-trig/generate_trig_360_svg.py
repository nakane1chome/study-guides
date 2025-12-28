#!/usr/bin/env python3
"""
Generate sine and cosine functions SVG from 0° to 360°
Shows full wave patterns for both sin(x) and cos(x)
"""

import math

def generate_trig_360_svg():
    # SVG dimensions
    width = 800
    height = 520
    margin_left = 60
    margin_bottom = 80
    margin_top = 80
    margin_right = 40

    # Graph dimensions
    graph_width = width - margin_left - margin_right
    graph_height = height - margin_top - margin_bottom

    # Start SVG
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    # Add background
    svg += f'  <rect width="{width}" height="{height}" fill="white"/>\n\n'

    # Calculate axis positions
    # Y-axis should be in the middle vertically (since values go from -1 to 1)
    x_axis_y = height - margin_bottom - graph_height / 2
    y_axis_x = margin_left

    # Grid lines
    svg += '  <!-- Grid lines -->\n'

    # Horizontal gridlines at special y-values
    import math as m
    grid_y_values = [1, m.sqrt(3)/2, 1/m.sqrt(2), 1/2, 0, -1/2, -1/m.sqrt(2), -m.sqrt(3)/2, -1]
    for y_val in grid_y_values:
        y_pos = x_axis_y - (y_val * graph_height / 2)
        stroke_width = "1.5" if y_val == 0 else "0.8"
        color = "#aaaaaa" if y_val == 0 else "#cccccc"
        svg += f'  <line x1="{margin_left}" y1="{y_pos}" x2="{width - margin_right}" y2="{y_pos}" stroke="{color}" stroke-width="{stroke_width}" stroke-dasharray="3,3"/>\n'

    # Vertical gridlines at special angles
    grid_angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]
    for angle in grid_angles:
        x_pos = margin_left + (angle / 360) * graph_width
        stroke_width = "1.2" if angle % 90 == 0 else "0.8"
        color = "#aaaaaa" if angle % 90 == 0 else "#cccccc"
        svg += f'  <line x1="{x_pos}" y1="{margin_top}" x2="{x_pos}" y2="{height - margin_bottom}" stroke="{color}" stroke-width="{stroke_width}" stroke-dasharray="3,3"/>\n'

    svg += '\n'

    # Axes
    svg += '  <!-- Axes -->\n'
    # X-axis (at y=0)
    svg += f'  <line x1="{margin_left}" y1="{x_axis_y}" x2="{width - margin_right}" y2="{x_axis_y}" stroke="black" stroke-width="2"/>\n'
    # Y-axis
    svg += f'  <line x1="{y_axis_x}" y1="{margin_top}" x2="{y_axis_x}" y2="{height - margin_bottom}" stroke="black" stroke-width="2"/>\n\n'

    # Arrow heads
    svg += '  <!-- Arrow heads -->\n'
    svg += f'  <polygon points="{width - margin_right},{x_axis_y} {width - margin_right - 5},{x_axis_y - 5} {width - margin_right - 5},{x_axis_y + 5}" fill="black"/>\n'
    svg += f'  <polygon points="{y_axis_x},{margin_top} {y_axis_x - 5},{margin_top + 5} {y_axis_x + 5},{margin_top + 5}" fill="black"/>\n\n'

    # Axis labels
    svg += '  <!-- Axis labels -->\n'
    svg += f'  <text x="{width - margin_right + 10}" y="{x_axis_y + 5}" font-family="Arial" font-size="16" font-weight="bold">θ</text>\n'
    svg += f'  <text x="{y_axis_x - 15}" y="{margin_top - 10}" font-family="Arial" font-size="14" font-weight="bold">y</text>\n\n'

    # X-axis tick marks and labels
    svg += '  <!-- X-axis ticks and labels -->\n'
    # Include special angles: 0, 30, 45, 60, 90, 120, 135, 150, 180, etc.
    major_angles = [0, 90, 180, 270, 360]
    minor_angles = [30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330]

    # Major angle marks
    for angle in major_angles:
        x_pos = margin_left + (angle / 360) * graph_width
        svg += f'  <line x1="{x_pos}" y1="{x_axis_y - 5}" x2="{x_pos}" y2="{x_axis_y + 5}" stroke="black" stroke-width="2"/>\n'
        svg += f'  <text x="{x_pos - 15}" y="{x_axis_y + 20}" font-family="Arial" font-size="13" font-weight="bold">{angle}°</text>\n'

    # Minor angle marks (special angles)
    for angle in minor_angles:
        x_pos = margin_left + (angle / 360) * graph_width
        svg += f'  <line x1="{x_pos}" y1="{x_axis_y - 3}" x2="{x_pos}" y2="{x_axis_y + 3}" stroke="black" stroke-width="1"/>\n'
        svg += f'  <text x="{x_pos - 12}" y="{x_axis_y + 38}" font-family="Arial" font-size="10">{angle}°</text>\n'

    svg += '\n'

    # Y-axis tick marks and labels with exact values
    svg += '  <!-- Y-axis ticks and labels -->\n'
    import math as m

    # Define special y-values with their decimal equivalents and labels
    y_values_data = [
        (1, "1"),
        (m.sqrt(3)/2, "√3/2"),
        (1/m.sqrt(2), "1/√2"),
        (1/2, "1/2"),
        (0, "0"),
        (-1/2, "-1/2"),
        (-1/m.sqrt(2), "-1/√2"),
        (-m.sqrt(3)/2, "-√3/2"),
        (-1, "-1"),
    ]

    for y_val, label in y_values_data:
        # Map y value (-1 to 1) to y position
        y_pos = x_axis_y - (y_val * graph_height / 2)

        # Tick mark
        svg += f'  <line x1="{y_axis_x - 5}" y1="{y_pos}" x2="{y_axis_x + 5}" y2="{y_pos}" stroke="black" stroke-width="1"/>\n'

        # Label
        label_offset = 50 if "√" in label else 35
        svg += f'  <text x="{y_axis_x - label_offset}" y="{y_pos + 4}" font-family="Arial" font-size="11">{label}</text>\n'

    svg += '\n'

    # Generate sine curve
    svg += '  <!-- Sine curve -->\n'
    svg += '  <path d="'

    num_points = 400
    for i in range(num_points + 1):
        angle_deg = (i / num_points) * 360
        angle_rad = math.radians(angle_deg)
        sin_val = math.sin(angle_rad)

        # Map to SVG coordinates
        x = margin_left + (angle_deg / 360) * graph_width
        y = x_axis_y - (sin_val * graph_height / 2)

        if i == 0:
            svg += f'M {x:.2f} {y:.2f}'
        else:
            svg += f' L {x:.2f} {y:.2f}'

    svg += '" fill="none" stroke="blue" stroke-width="2.5"/>\n\n'

    # Generate cosine curve
    svg += '  <!-- Cosine curve -->\n'
    svg += '  <path d="'

    for i in range(num_points + 1):
        angle_deg = (i / num_points) * 360
        angle_rad = math.radians(angle_deg)
        cos_val = math.cos(angle_rad)

        # Map to SVG coordinates
        x = margin_left + (angle_deg / 360) * graph_width
        y = x_axis_y - (cos_val * graph_height / 2)

        if i == 0:
            svg += f'M {x:.2f} {y:.2f}'
        else:
            svg += f' L {x:.2f} {y:.2f}'

    svg += '" fill="none" stroke="red" stroke-width="2.5"/>\n\n'

    # Add special points for sine at all special angles
    svg += '  <!-- Special points for sine -->\n'
    all_special_angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

    for angle in all_special_angles:
        angle_rad = math.radians(angle)
        sin_val = math.sin(angle_rad)
        x = margin_left + (angle / 360) * graph_width
        y = x_axis_y - (sin_val * graph_height / 2)
        svg += f'  <circle cx="{x}" cy="{y}" r="2.5" fill="blue"/>\n'

        # Add value labels for key points only
        if angle in [90, 270]:
            label_y_offset = -10 if sin_val > 0 else 15
            svg += f'  <text x="{x - 8}" y="{y + label_y_offset}" font-family="Arial" font-size="11" fill="blue" font-weight="bold">{int(sin_val)}</text>\n'

    svg += '\n'

    # Add special points for cosine at all special angles
    svg += '  <!-- Special points for cosine -->\n'

    for angle in all_special_angles:
        angle_rad = math.radians(angle)
        cos_val = math.cos(angle_rad)
        x = margin_left + (angle / 360) * graph_width
        y = x_axis_y - (cos_val * graph_height / 2)
        svg += f'  <circle cx="{x}" cy="{y}" r="2.5" fill="red"/>\n'

        # Add value labels for key points
        if angle == 0:
            svg += f'  <text x="{x - 25}" y="{y - 10}" font-family="Arial" font-size="11" fill="red" font-weight="bold">cos: 1</text>\n'
        elif angle == 180:
            label_y_offset = 15
            svg += f'  <text x="{x - 10}" y="{y + label_y_offset}" font-family="Arial" font-size="11" fill="red" font-weight="bold">-1</text>\n'
        elif angle == 360:
            svg += f'  <text x="{x + 10}" y="{y - 10}" font-family="Arial" font-size="11" fill="red" font-weight="bold">cos: 1</text>\n'

    svg += '\n'

    # Legend (positioned above the graph)
    svg += '  <!-- Legend -->\n'
    legend_x = width - margin_right - 160
    legend_y = 25

    # Background for legend
    svg += f'  <rect x="{legend_x - 10}" y="{legend_y - 18}" width="150" height="50" fill="white" stroke="black" stroke-width="1" rx="5"/>\n'

    # Sine line
    svg += f'  <line x1="{legend_x}" y1="{legend_y}" x2="{legend_x + 40}" y2="{legend_y}" stroke="blue" stroke-width="2.5"/>\n'
    svg += f'  <text x="{legend_x + 50}" y="{legend_y + 5}" font-family="Arial" font-size="14" font-weight="bold" fill="blue">sin θ</text>\n'

    # Cosine line
    svg += f'  <line x1="{legend_x}" y1="{legend_y + 20}" x2="{legend_x + 40}" y2="{legend_y + 20}" stroke="red" stroke-width="2.5"/>\n'
    svg += f'  <text x="{legend_x + 50}" y="{legend_y + 25}" font-family="Arial" font-size="14" font-weight="bold" fill="red">cos θ</text>\n'

    # Close SVG
    svg += '</svg>\n'

    return svg

if __name__ == '__main__':
    svg_content = generate_trig_360_svg()

    # Write to file
    with open('trig_360.svg', 'w') as f:
        f.write(svg_content)

    print('trig_360.svg generated successfully!')
    print('Full sine and cosine waves from 0° to 360°')
