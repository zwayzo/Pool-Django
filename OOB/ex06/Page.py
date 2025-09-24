from elements import *

class Page:
    """
    A Page class that validates HTML structure and can output HTML with proper doctype.
    """
    
    def __init__(self, elem):
        """
        Initialize Page with an element (should be an instance inheriting from Elem).
        
        Args:
            elem: Root element of the page (typically Html)
        """
        if not isinstance(elem, Elem):
            raise TypeError("Page must be initialized with an Elem instance")
        self.elem = elem
    
    def __str__(self):
        """
        Return HTML string representation with doctype if root is Html.
        """
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + str(self.elem)
        else:
            return str(self.elem)
    
    def write_to_file(self, filename):
        """
        Write HTML content to a file with doctype if root is Html.
        
        Args:
            filename (str): Name of the file to write to
        """
        with open(filename, 'w') as f:
            f.write(str(self))
    
    def is_valid(self):
        """
        Validate the HTML structure according to the specified rules.
        
        Returns:
            bool: True if valid, False otherwise
        """
        return self._validate_element(self.elem)
    
    def _validate_element(self, elem):
        """
        Recursively validate an element and its children.
        
        Args:
            elem: Element to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        # Check if element type is allowed
        allowed_types = (
            Html, Head, Body, Title, meta, img, table, th, tr, td,
            ul, ol, li, h1, h2, p, div, span, hr, br, Text
        )
        
        if not isinstance(elem, allowed_types):
            return False
        
        # Text elements are always valid
        if isinstance(elem, Text):
            return True
        
        # Validate based on element type
        if isinstance(elem, Html):
            return self._validate_html(elem)
        elif isinstance(elem, Head):
            return self._validate_head(elem)
        elif isinstance(elem, Body):
            return self._validate_body(elem)
        elif isinstance(elem, div):
            return self._validate_body(elem)  # Same rules as Body
        elif isinstance(elem, Title):
            return self._validate_title(elem)
        elif isinstance(elem, (h1, h2)):
            return self._validate_heading(elem)
        elif isinstance(elem, li):
            return self._validate_li(elem)
        elif isinstance(elem, (th, td)):
            return self._validate_cell(elem)
        elif isinstance(elem, p):
            return self._validate_p(elem)
        elif isinstance(elem, span):
            return self._validate_span(elem)
        elif isinstance(elem, (ul, ol)):
            return self._validate_list(elem)
        elif isinstance(elem, tr):
            return self._validate_tr(elem)
        elif isinstance(elem, table):
            return self._validate_table(elem)
        elif isinstance(elem, (meta, img, hr, br)):
            # Self-closing elements - no content validation needed
            return True
        
        # For other elements, just validate children
        return all(self._validate_element(child) for child in elem.content)
    
    def _validate_html(self, elem):
        """Html must strictly contain a Head, then a Body."""
        if len(elem.content) != 2:
            return False
        return (isinstance(elem.content[0], Head) and 
                isinstance(elem.content[1], Body) and
                self._validate_element(elem.content[0]) and
                self._validate_element(elem.content[1]))
    
    def _validate_head(self, elem):
        """Head must only contain one Title and only one Title."""
        if len(elem.content) != 1:
            return False
        return (isinstance(elem.content[0], Title) and
                self._validate_element(elem.content[0]))
    
    def _validate_body(self, elem):
        """Body and Div must only contain: H1, H2, Div, Table, Ul, Ol, Span, or Text."""
        allowed = (h1, h2, div, table, ul, ol, span, Text)
        return (len(elem.content) > 0 and
                all(isinstance(child, allowed) and self._validate_element(child) 
                    for child in elem.content))
    
    def _validate_title(self, elem):
        """Title must only contain one Text and only this Text."""
        if len(elem.content) != 1:
            return False
        return isinstance(elem.content[0], Text)
    
    def _validate_heading(self, elem):
        """H1, H2 must only contain one Text and only this Text."""
        if len(elem.content) != 1:
            return False
        return isinstance(elem.content[0], Text)
    
    def _validate_li(self, elem):
        """Li must only contain one Text and only this Text."""
        if len(elem.content) != 1:
            return False
        return isinstance(elem.content[0], Text)
    
    def _validate_cell(self, elem):
        """Th, Td must only contain one Text and only this Text."""
        if len(elem.content) != 1:
            return False
        return isinstance(elem.content[0], Text)
    
    def _validate_p(self, elem):
        """P must only contain Text."""
        return (len(elem.content) > 0 and
                all(isinstance(child, Text) for child in elem.content))
    
    def _validate_span(self, elem):
        """Span must only contain Text or some P."""
        allowed = (Text, p)
        return (len(elem.content) > 0 and
                all(isinstance(child, allowed) and self._validate_element(child)
                    for child in elem.content))
    
    def _validate_list(self, elem):
        """Ul and Ol must contain at least one Li and only some Li."""
        return (len(elem.content) >= 1 and
                all(isinstance(child, li) and self._validate_element(child)
                    for child in elem.content))
    
    def _validate_tr(self, elem):
        """Tr must contain at least one Th or Td and only some Th or Td. Th and Td must be mutually exclusive."""
        if len(elem.content) < 1:
            return False
        
        has_th = any(isinstance(child, th) for child in elem.content)
        has_td = any(isinstance(child, td) for child in elem.content)
        
        # Th and Td must be mutually exclusive
        if has_th and has_td:
            return False
        
        # Must contain only th or only td
        if has_th:
            return all(isinstance(child, th) and self._validate_element(child)
                      for child in elem.content)
        else:
            return all(isinstance(child, td) and self._validate_element(child)
                      for child in elem.content)
    
    def _validate_table(self, elem):
        """Table must only contain Tr and only some Tr."""
        return (len(elem.content) > 0 and
                all(isinstance(child, tr) and self._validate_element(child)
                    for child in elem.content))


# Test demonstrations
if __name__ == "__main__":
    print("=== Testing Page Class ===\n")
    
    # Test 1: Valid HTML page
    print("Test 1: Valid HTML page")
    valid_page = Page(Html([
        Head(Title(Text("Valid Page"))),
        Body([
            h1(Text("Welcome")),
            p(Text("This is a valid page.")),
            div([
                h2(Text("Section")),
                span(Text("Some text in span"))
            ])
        ])
    ]))
    
    print(f"Valid: {valid_page.is_valid()}")
    print("HTML output:")
    print(valid_page)
    print()
    
    # Test 2: Invalid HTML - missing Body
    print("Test 2: Invalid HTML - Html missing Body")
    invalid_page1 = Page(Html([
        Head(Title(Text("Invalid")))
    ]))
    print(f"Valid: {invalid_page1.is_valid()}")
    print()
    
    # Test 3: Invalid HTML - Head with multiple Titles
    print("Test 3: Invalid HTML - Head with multiple Titles")
    invalid_page2 = Page(Html([
        Head([Title(Text("First")), Title(Text("Second"))]),
        Body(h1(Text("Hello")))
    ]))
    print(f"Valid: {invalid_page2.is_valid()}")
    print()
    
    # Test 4: Valid table structure
    print("Test 4: Valid table with headers")
    table_page = Page(Html([
        Head(Title(Text("Table Page"))),
        Body([
            h1(Text("Data Table")),
            table([
                tr([th(Text("Name")), th(Text("Age"))]),
                tr([td(Text("John")), td(Text("25"))])
            ])
        ])
    ]))
    print(f"Valid: {table_page.is_valid()}")
    print()
    
    # Test 5: Invalid table - mixing th and td in same row
    print("Test 5: Invalid table - mixing th and td in same row")
    invalid_table = Page(Html([
        Head(Title(Text("Invalid Table"))),
        Body(table([
            tr([th(Text("Header")), td(Text("Data"))])  # Invalid: mixing th and td
        ]))
    ]))
    print(f"Valid: {invalid_table.is_valid()}")
    print()
    
    # Test 6: Valid list structure
    print("Test 6: Valid list structure")
    list_page = Page(Html([
        Head(Title(Text("List Page"))),
        Body([
            h1(Text("My List")),
            ul([
                li(Text("Item 1")),
                li(Text("Item 2")),
                li(Text("Item 3"))
            ])
        ])
    ]))
    print(f"Valid: {list_page.is_valid()}")
    print()
    
    # Test 7: Non-Html root (no doctype)
    print("Test 7: Non-Html root element (no doctype)")
    div_page = Page(div([
        h1(Text("Just a div")),
        p(Text("No HTML wrapper"))
    ]))
    print(f"Valid: {div_page.is_valid()}")
    print("Output (no doctype):")
    print(div_page)
    print()
    
    # Test 8: Write to file
    print("Test 8: Writing to file")
    valid_page.write_to_file("test_output.html")
    print("HTML written to 'test_output.html'")
    
    # Test 9: Invalid - P containing non-Text
    print("\nTest 9: Invalid - P containing H1")
    invalid_p = Page(Html([
        Head(Title(Text("Invalid P"))),
        Body(p([Text("Some text"), h1(Text("Invalid heading in P"))]))  # Invalid
    ]))
    print(f"Valid: {invalid_p.is_valid()}")
    
    # Test 10: Valid span with P
    print("\nTest 10: Valid span containing P")
    span_page = Page(Html([
        Head(Title(Text("Span Page"))),
        Body(span([
            Text("Text before paragraph "),
            p(Text("Paragraph inside span")),
            Text(" text after paragraph")
        ]))
    ]))
    print(f"Valid: {span_page.is_valid()}")
    
    print("\n=== All tests completed ===")
    