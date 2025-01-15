def check_word_in_bbox(word_bbox, user_bbox, doc_width, doc_height):
    word_width, word_height, word_left, word_top = word_bbox
    x1, y1, x3, y3 = user_bbox

    # Check if the word's bounding box is within the user-drawn bounding box
    if (word_left >= x1 and
        word_top >= y1 and
        (word_left + word_width) <= x3 and
        (word_top + word_height) <= y3):
        return True
    return False

def scale_bbox_to_actual_coords(scaled_bbox, doc_width, doc_height):
    w_scale, h_scale, left_scale, top_scale = scaled_bbox
    word_width = w_scale * doc_width
    word_height = h_scale * doc_height
    word_left = left_scale * doc_width
    word_top = top_scale * doc_height
    return word_width, word_height, word_left, word_top

def get_words_in_user_bbox(words_position_dict, user_bbox, doc_width, doc_height):
    words_in_bbox = []

    for word, scaled_bbox in words_position_dict.items():
        word_bbox = scale_bbox_to_actual_coords(scaled_bbox, doc_width, doc_height)
        if check_word_in_bbox(word_bbox, user_bbox, doc_width, doc_height):
            words_in_bbox.append(word)

    return words_in_bbox

# Example input:
words_position_dict = {
    "word1": [0.1, 0.05, 0.2, 0.1],
    "word2": [0.3, 0.1, 0.2, 0.15],
    "word3": [0.5, 0.05, 0.1, 0.1],
    "word4": [0.2, 0.1, 0.25, 0.2]
}

doc_width = 1263
doc_height = 1644
user_bbox = [358, 140, 498, 171]

# Get the words inside the user-drawn bounding box
words_in_bbox = get_words_in_user_bbox(words_position_dict, user_bbox, doc_width, doc_height)
print("Words inside the user-drawn bounding box:", words_in_bbox)
