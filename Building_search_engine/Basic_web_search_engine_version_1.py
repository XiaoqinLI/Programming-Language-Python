# Modified the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

def get_next_target(page):
    start_link = page.find('<a href=')
    
    if start_link >= 0:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    else: return None,0

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

print_all_links('this <a href="test1">link 1</a> is a <a href="test2">link 2</a> a <a href="test3">link 3</a>')