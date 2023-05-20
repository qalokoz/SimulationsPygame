import pygame
# the width and height dimensions
WIDTH = 800
HEIGHT = 600
# colors required
BACKGROUND_COLOR = (255, 255, 255)
BOX_COLOR = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)
SELECTED_COLOR = (255, 0, 0)
SWAPPED_COLOR = (0, 255, 0)
CODE_COLOR = (0, 0, 255)
HIGHLIGHTED_CODE_COLOR = (255, 0, 0)

# Insertion Sort algorithm to sort the numbers 
# we will use this function for simulatiuon purpose 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Insertion Sort Visualization")

font = pygame.font.SysFont(None, 30)
code_font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
user_input = input("Enter a list of integers separated by commas: ")
numbers = list(map(int, user_input.split(",")))

box_size = 60
box_spacing = 20
current_index = 1
key_index = 1
sorting_done = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not sorting_done:
                if current_index < len(numbers):
                    if key_index > 0 and numbers[key_index - 1] > numbers[key_index]:
                        numbers[key_index], numbers[key_index - 1] = numbers[key_index - 1], numbers[key_index]
                        key_index -= 1
                    else:
                        current_index += 1
                        key_index = current_index
                else:
                    insertion_sort(numbers)
                    sorting_done = True

    window.fill(BACKGROUND_COLOR)

    # boxes with the numbers 
    for i, number in enumerate(numbers):
        x = (box_size + box_spacing) * i
        y = HEIGHT // 2 - box_size // 2
        box_rect = pygame.Rect(x, y, box_size, box_size)
        pygame.draw.rect(window, BOX_COLOR, box_rect)

        number_text = font.render(str(number), True, TEXT_COLOR)
        text_rect = number_text.get_rect(center=box_rect.center)
        window.blit(number_text, text_rect)

        # Highlight
        if i == current_index:
            pygame.draw.rect(window, SELECTED_COLOR, box_rect, 4)
        elif i == key_index:
            pygame.draw.rect(window, SWAPPED_COLOR, box_rect, 4)

    # Display code
    code_lines = [
        "for i in range(1, len(arr)):",
        "    key = arr[i]",
        "    j = i - 1",
        "    while j >= 0 and arr[j] > key:",
        "        arr[j + 1] = arr[j]",
        "        j -= 1",
        "    arr[j + 1] = key"
    ]

    code_x = 50
    code_y = 50

    for i, line in enumerate(code_lines):
        code_text = code_font.render(line, True, CODE_COLOR)
        code_rect = code_text.get_rect(x=code_x, y=code_y + i * 30)

        if not sorting_done and i == current_index:
            pygame.draw.rect(window, HIGHLIGHTED_CODE_COLOR, code_rect, 2)

        window.blit(code_text, code_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
