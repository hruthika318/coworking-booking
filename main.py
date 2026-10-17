
def book_workspace(available):
    if available:
        return "Workspace booked successfully"
    else:
        return "Workspace is not available"

print(book_workspace(True))
print(book_workspace(False))

