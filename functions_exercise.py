def get_order_details():
    """Prompt the user for job details and return them."""
    # returns: number_of_pages, is_color, is_rush, wants_binding, has_student_id
    pass

def calculate_print_cost(number_of_pages, is_color, is_rush):
    """Calculate printing cost including rush surcharge, before binding/discount."""
    # returns: print_cost
    pass

def apply_binding(print_cost, wants_binding):
    """Add binding cost if requested."""
    # returns: subtotal
    pass

def apply_discount(subtotal, has_student_id):
    """Apply student discount if applicable."""
    # returns: final_total, discount_amount
    pass

def display_receipt(print_cost, is_rush, wants_binding, discount_amount, final_total):
    """Print an itemized receipt."""
    pass

def main():
    number_of_pages, is_color, is_rush, wants_binding, has_student_id = get_order_details()
    print_cost = calculate_print_cost(number_of_pages, is_color, is_rush)
    subtotal = apply_binding(print_cost, wants_binding)
    final_total, discount_amount = apply_discount(subtotal, has_student_id)
    display_receipt(print_cost, is_rush, wants_binding, discount_amount, final_total)

main()
