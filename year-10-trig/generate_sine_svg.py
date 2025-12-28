#!/usr/bin/env python3
"""
Generate a smooth sine function SVG from 0° to 90°
Shows sin(x) increasing from 0 to 1
"""

import math

def generate_sine_svg():
    # SVG dimensions
    width = 500
    height = 400
    margin_left = 60
    margin_bottom = 60
    margin_top = 40
    margin_right = 40

    # Graph dimensions
    graph_width = width - margin_left - margin_right
    graph_height = height - margin_top - margin_bottom

    # Start SVG
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    # Add background
    svg += f'  <rect width="{width}" height="{height}" fill="white"/>\n\n'

    # Axes positions
    x_axis_y = height - margin_bottom
    y_axis_x = margin_left

    # Grid lines
    svg += '  <!-- Grid lines -->\n'

    # Horizontal gridlines at special y-values (0 to 1)
    grid_y_values = [
        (0, "0"),
        (1/2, "1/2"),
        (1/math.sqrt(2), "1/√2"),
        (math.sqrt(3)/2, "√3/2"),
        (1, "1")
    ]
    for y_val, label in grid_y_values:
        y_pos = x_axis_y - (y_val * graph_height)
        stroke_width = "1.5" if y_val == 0 else "0.8"
        color = "#aaaaaa" if y_val == 0 else "#cccccc"
        svg += f'  <line x1="{margin_left}" y1="{y_pos}" x2="{width - margin_right}" y2="{y_pos}" stroke="{color}" stroke-width="{stroke_width}" stroke-dasharray="3,3"/>\n'

    # Vertical gridlines at special angles
    grid_angles = [0, 30, 45, 60, 90]
    for angle in grid_angles:
        x_pos = margin_left + (angle / 90) * graph_width
        stroke_width = "1.2" if angle % 90 == 0 else "0.8"
        color = "#aaaaaa" if angle % 90 == 0 else "#cccccc"
        svg += f'  <line x1="{x_pos}" y1="{x_axis_y}" x2="{x_pos}" y2="{margin_top}" stroke="{color}" stroke-width="{stroke_width}" stroke-dasharray="3,3"/>\n'

    svg += '\n'

    svg += '  <!-- Axes -->\n'
    # X-axis
    svg += f'  <line x1="{margin_left}" y1="{x_axis_y}" x2="{width - margin_right}" y2="{x_axis_y}" stroke="black" stroke-width="2"/>\n'
    # Y-axis
    svg += f'  <line x1="{y_axis_x}" y1="{x_axis_y}" x2="{y_axis_x}" y2="{margin_top}" stroke="black" stroke-width="2"/>\n\n'

    # Arrow heads
    svg += '  <!-- Arrow heads -->\n'
    svg += f'  <polygon points="{width - margin_right},{x_axis_y} {width - margin_right - 5},{x_axis_y - 5} {width - margin_right - 5},{x_axis_y + 5}" fill="black"/>\n'
    svg += f'  <polygon points="{y_axis_x},{margin_top} {y_axis_x - 5},{margin_top + 5} {y_axis_x + 5},{margin_top + 5}" fill="black"/>\n\n'

    # Axis labels
    svg += '  <!-- Axis labels -->\n'
    svg += f'  <text x="{width - margin_right + 10}" y="{x_axis_y + 5}" font-family="Arial" font-size="16" font-weight="bold">θ</text>\n'
    svg += f'  <text x="{y_axis_x - 40}" y="{margin_top - 5}" font-family="Arial" font-size="16" font-weight="bold">sin θ</text>\n\n'

    # X-axis tick marks and labels
    svg += '  <!-- X-axis ticks and labels -->\n'
    angles = [0, 30, 45, 60, 90]
    for angle in angles:
        # Map angle (0-90) to x position
        x_pos = margin_left + (angle / 90) * graph_width

        # Tick mark
        svg += f'  <line x1="{x_pos}" y1="{x_axis_y - 5}" x2="{x_pos}" y2="{x_axis_y + 5}" stroke="black" stroke-width="1.5"/>\n'

        # Label
        label_offset = 10 if angle == 0 else 0
        svg += f'  <text x="{x_pos - 10 - label_offset}" y="{x_axis_y + 20}" font-family="Arial" font-size="14">{angle}°</text>\n'

    svg += '\n'

    # Y-axis tick marks and labels with fractional values
    svg += '  <!-- Y-axis ticks and labels -->\n'
    y_values_labels = [
        (0, "0"),
        (1/2, "1/2"),
        (1/math.sqrt(2), "1/√2"),
        (math.sqrt(3)/2, "√3/2"),
        (1, "1")
    ]
    for y_val, label in y_values_labels:
        # Map y value (0-1) to y position (inverted because SVG y increases downward)
        y_pos = x_axis_y - (y_val * graph_height)

        # Tick mark
        svg += f'  <line x1="{y_axis_x - 5}" y1="{y_pos}" x2="{y_axis_x + 5}" y2="{y_pos}" stroke="black" stroke-width="1.5"/>\n'

        # Label
        label_offset = 45 if "√" in label else 30
        svg += f'  <text x="{y_axis_x - label_offset}" y="{y_pos + 4}" font-family="Arial" font-size="12">{label}</text>\n'

    svg += '\n'

    # Generate sine curve
    svg += '  <!-- Sine curve -->\n'
    svg += '  <path d="'

    # Generate points for smooth curve
    num_points = 200
    for i in range(num_points + 1):
        # Angle in degrees
        angle_deg = (i / num_points) * 90
        # Convert to radians
        angle_rad = math.radians(angle_deg)
        # Calculate sine value
        sin_val = math.sin(angle_rad)

        # Map to SVG coordinates
        x = margin_left + (angle_deg / 90) * graph_width
        y = x_axis_y - (sin_val * graph_height)

        if i == 0:
            svg += f'M {x:.2f} {y:.2f}'
        else:
            svg += f' L {x:.2f} {y:.2f}'

    svg += '" fill="none" stroke="blue" stroke-width="3"/>\n\n'

    # Add special points at all special angles
    svg += '  <!-- Special points -->\n'
    special_angles = [0, 30, 45, 60, 90]
    for angle in special_angles:
        angle_rad = math.radians(angle)
        sin_val = math.sin(angle_rad)
        x = margin_left + (angle / 90) * graph_width
        y = x_axis_y - (sin_val * graph_height)
        svg += f'  <circle cx="{x}" cy="{y}" r="3" fill="red"/>\n'

    # Labels for endpoints
    svg += f'  <text x="{margin_left + 8}" y="{x_axis_y - 8}" font-family="Arial" font-size="11" fill="red">(0°, 0)</text>\n'
    y_90 = x_axis_y - graph_height
    svg += f'  <text x="{margin_left + graph_width - 50}" y="{y_90 - 8}" font-family="Arial" font-size="11" fill="red">(90°, 1)</text>\n'

    # Add annotation
    svg += '\n  <!-- Annotation -->\n'
    svg += f'  <text x="{margin_left + graph_width/2 - 80}" y="{margin_top + 20}" font-family="Arial" font-size="14" fill="green" font-style="italic">sin θ increases from 0 to 1</text>\n'
    svg += f'  <text x="{margin_left + graph_width/2 - 60}" y="{margin_top + 38}" font-family="Arial" font-size="14" fill="green" font-style="italic">as θ goes from 0° to 90°</text>\n'

    # Close SVG
    svg += '</svg>\n'

    return svg

if __name__ == '__main__':
    svg_content = generate_sine_svg()

    # Write to file
    with open('sine_function.svg', 'w') as f:
        f.write(svg_content)

    print('sine_function.svg generated successfully!')
