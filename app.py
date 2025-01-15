# Helper function to check if two rectangles overlap
def is_overlap(rect1, rect2):
    # rect1 = (left, top, right, bottom)
    # rect2 = (x1, y1, x3, y3) -> (x1, y1) -> bottom-left, (x3, y3) -> top-right
    rect1_left, rect1_top, rect1_right, rect1_bottom = rect1
    rect2_left, rect2_bottom, rect2_right, rect2_top = rect2
    
    # Check for non-overlapping conditions
    if rect1_right <= rect2_left or rect1_left >= rect2_right:
        return False
    if rect1_bottom >= rect2_top or rect1_top <= rect2_bottom:
        return False
    return True

def find_words_in_box(document_width, document_height, word_bounding_boxes, user_box):
    # Convert the user box into (left, top, right, bottom)
    x1, y1, x3, y3 = user_box
    user_rect = (x1 * document_width, y3 * document_height, x3 * document_width, y1 * document_height)

    found_words = []
    
    # Iterate through the word bounding boxes
    for word, box in word_bounding_boxes.items():
        # Scale word box to pixel-based coordinates
        word_width, word_height, word_left, word_top = box
        word_rect = (word_left * document_width, word_top * document_height,
                     (word_left + word_width) * document_width, 
                     (word_top + word_height) * document_height)
        
        # Check if there's an overlap
        if is_overlap(word_rect, user_rect):
            found_words.append(word)
    
    return found_words

# Example of usage:
# Let's assume the document size is 1000x1000 (width x height)
document_width = 1000
document_height = 1000

# Example of word bounding boxes: word -> (width, height, left, top)
word_bounding_boxes = {
    "hello": (0.1, 0.05, 0.2, 0.3),
    "world": (0.1, 0.05, 0.4, 0.3),
    "example": (0.2, 0.1, 0.5, 0.6)
}

# User defined rectangle (scaled)
user_box = [0.15, 0.25, 0.45, 0.35]  # [x1, y1, x3, y3] scaled to [0, 1] range

# Find the words that overlap
result = find_words_in_box(document_width, document_height, word_bounding_boxes, user_box)
print("Words in the user-defined box:", result)
