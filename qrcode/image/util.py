from PIL import Image, ImageDraw

def draw_round_rectangle(draw, xoffset, yoffset, size, radius, left_top, right_top, right_bottom, left_bottom, fore_color, back_color):
    draw.rectangle((xoffset, yoffset, xoffset + size, yoffset + size), fill=back_color)

    if radius > size / 2:
        radius = size / 2

    if left_top:
        draw.pieslice((xoffset, yoffset, xoffset + 2 * radius, yoffset + 2 * radius), 180, 270, fill=fore_color)
        if radius * 2 < size:
            draw.rectangle((xoffset + radius, yoffset, xoffset + size / 2, yoffset + size / 2), fill=fore_color)
            draw.rectangle((xoffset, yoffset + radius, xoffset + radius, yoffset + size / 2), fill=fore_color)
    else:
        draw.rectangle((xoffset, yoffset, xoffset + size / 2, yoffset + size / 2), fill=fore_color)


    if right_top:
        draw.pieslice((xoffset + size - 2 * radius, yoffset, xoffset + size, yoffset + 2 * radius), 270, 360, fill=fore_color)
        if radius * 2 < size:
            draw.rectangle((xoffset + size / 2, yoffset, xoffset + size - radius, yoffset + size / 2), fill=fore_color)
            draw.rectangle((xoffset + size - radius, yoffset + radius, xoffset + size, yoffset + size / 2), fill=fore_color)
    else:
        draw.rectangle((xoffset + size / 2, yoffset, xoffset + size, yoffset + size / 2), fill=fore_color)

    if right_bottom:
        draw.pieslice((xoffset + size - 2 * radius, yoffset + size - 2 * radius, xoffset + size, yoffset + size), 0, 90, fill=fore_color)
        if radius * 2 < size:
            draw.rectangle((xoffset + size / 2, yoffset + size / 2, xoffset + size - radius, yoffset + size), fill=fore_color)
            draw.rectangle((xoffset + size - radius, yoffset + size / 2, xoffset + size, yoffset + size - radius), fill=fore_color)
    else:
        draw.rectangle((xoffset + size / 2, yoffset + size / 2, xoffset + size, yoffset + size), fill=fore_color)

    if left_bottom:
        draw.pieslice((xoffset, yoffset + size - 2 * radius, xoffset + 2 * radius, yoffset + size), 90, 180, fill=fore_color)
        if radius * 2 < size:
            draw.rectangle((xoffset, yoffset + size / 2, xoffset + radius, yoffset + size - radius), fill=fore_color)
            draw.rectangle((xoffset + radius, yoffset + size / 2, xoffset + size / 2, yoffset + size), fill=fore_color)
    else:
        draw.rectangle((xoffset, yoffset + size / 2, xoffset + size / 2, yoffset + size), fill=fore_color)
