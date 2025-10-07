class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.
    
    This class inherits from str but adds HTML escaping functionality.
    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Converts the Text object to a string with HTML escaping.
        
        This method handles special HTML characters by replacing them
        with their HTML entity equivalents to prevent HTML injection.
        """
        # Get the original string content
        result = super().__str__()
        
        # Replace HTML special characters with their HTML entities
        result = result.replace('&', '&amp;')    # Must be first to avoid double-escaping
        result = result.replace('<', '&lt;')     # Less than symbol
        result = result.replace('>', '&gt;')     # Greater than symbol
        result = result.replace('"', '&quot;')   # Double quote
        
        # Convert newlines to HTML line breaks
        result = result.replace('\n', '\n<br />\n')
        
        return result


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    
    This class can create any HTML element with attributes, content,
    and proper nesting structure.
    """

    class ValidationError(Exception):
        """
        Custom exception class for content validation errors.
        
        Raised when invalid content types are passed to Elem.
        """
        def __init__(self):
            pass

    def __init__(self, tag='div', attr=None, content=None, tag_type='double'):
        """
        Initialize an HTML element.
        
        Args:
            tag (str): HTML tag name (e.g., 'div', 'p', 'img')
            attr (dict): Dictionary of HTML attributes {'id': 'main', 'class': 'container'}
            content (Text/Elem/list): Content inside the element
            tag_type (str): 'double' for <tag></tag> or 'simple' for <tag />
        """
        # Set basic properties
        self.tag = tag
        self.attr = attr if attr is not None else {}  # Avoid mutable default argument
        self.tag_type = tag_type
        self.content = []  # Initialize as empty list
        
        # Handle initial content if provided
        if content is not None:
            # Validate content type before adding
            if Elem.check_type(content):
                if isinstance(content, list):
                    # Filter out empty Text objects from list
                    self.content = [elem for elem in content if not (isinstance(elem, Text) and str(elem) == "")]
                elif not (isinstance(content, Text) and str(content) == ""):
                    # Add single non-empty content
                    self.content = [content]
            else:
                # Raise error for invalid content types
                raise Elem.ValidationError()

    def __str__(self):
        """
        Elem(tag="p", content=Text("hello"))

        <p>
            hello
        </p>

        
        Returns properly formatted HTML with indentation for nested elements.
        """
        if self.tag_type == 'double':
            # Create opening tag with attributes
            result = "<" + self.tag + self.__make_attr() + ">"
            
            if self.content:
                # Add content with proper indentation and closing tag
                result += "\n" + self.__make_content(1)
                result += "\n</" + self.tag + ">"
            else:
                # Empty double tag - just add closing tag
                result += "</" + self.tag + ">"
                
        elif self.tag_type == 'simple':
            # Self-closing tag (like <img />, <br />)
            result = "<" + self.tag + self.__make_attr() + " />"
            
        return result

    def __make_attr(self):
        """
        Elem(tag="img", attr={"src": "cat.png", "alt": "cat"}, tag_type="simple")
        → <img alt="cat" src="cat.png" />

        Convert the attributes dictionary to HTML attribute string.
        
        Returns string like ' id="main" class="container"' (note leading space).
        Attributes are sorted alphabetically for consistent output.
        """
        result = ''
        # Sort attributes for consistent ordering
        for pair in sorted(self.attr.items()):
            # Format: space + key="value"
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self, indent=1):
        """
        deep nesting
        Elem(content=Elem(content=Elem()))

        <div>
        <div>
            <div></div>
        </div>
        </div>
        If nested elements exist, they call __str__, which calls __make_content, increasing indentation.

        Convert the content list to properly indented HTML string.
        
        Args:
            indent (int): Current indentation level (number of 2-space indents)
            
        Returns formatted content string with proper indentation for nesting.
        """
        if not self.content:
            return ''
            
        result = ''
        # Process each content element
        for elem in self.content:
            # Convert element to string (calls __str__ on Text or Elem objects)
            elem_str = str(elem)
            
            # Split into lines to handle multi-line content
            lines = elem_str.split('\n')
            
            # Add proper indentation to each line
            for line in lines:
                # Indent with 2 spaces per level
                result += '  ' * indent + line + '\n'
                
        # Remove the trailing newline
        return result.rstrip('\n')

    def add_content(self, content):
        """
        Add new content to the element.
        
        Args:
            content (Text/Elem/list): Content to add
            
        Validates content before adding and filters out empty Text objects.
        """
        # Validate content type first
        if not Elem.check_type(content):
            raise Elem.ValidationError()
            
        if isinstance(content, list):
            # Add all non-empty elements from list
            self.content += [elem for elem in content if not (isinstance(elem, Text) and str(elem) == "")]
        elif not (isinstance(content, Text) and str(content) == ""):
            # Add single non-empty element
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Validate if content is of acceptable type.
        
        Args:
            content: Content to validate
            
        Returns:
            bool: True if content is valid (Text, Elem, or list of Text/Elem)
        
        Valid types:
        - Elem object
        - Text object  
        - List containing only Text and/or Elem objects
        """
        return (isinstance(content, Elem) or 
                isinstance(content, Text) or
                (isinstance(content, list) and 
                 all(isinstance(elem, (Text, Elem)) for elem in content)))





import traceback


def test_text():
    # What is Text?
    assert isinstance(Text(), str)
    # Default behaviour :
    assert str(Text()) == ''
    # With an argument :
    assert str(Text('')) == ''
    assert str(Text('foo')) == 'foo'
    # Pattern replacing :
    assert str(Text('\n')) == '\n<br />\n'
    assert str(Text('foo\nbar')) == 'foo\n<br />\nbar'
    # Escaping <, >, "...
    assert str(Text('<')) == '&lt;'
    assert str(Text('>')) == '&gt;'
    assert str(Text('"')) == '&quot;'
    print('Text behaviour : OK.')

    
def test_elem_basics():
    # Default behaviour :
    assert str(Elem()) == '<div></div>'
    # Arguments order :
    assert str(Elem('div', {}, None, 'double')) == '<div></div>'
    # Argument names :
    assert str(Elem(tag='body', attr={}, content=Elem(),
                    tag_type='double')) == '<body>\n  <div></div>\n</body>'
    # With elem as content :
    assert str(Elem(content=Elem())) == '<div>\n  <div></div>\n</div>'
    # With list as content :
    assert str(Elem(content=[Text('foo'), Text('bar'), Elem()])) == '<div>\n  foo\n  bar\n \
 <div></div>\n</div>'
    print('Basic Elem behaviour : OK.')

    
def test_empty_texts():
    assert str(Elem(content=Text(''))) == '<div></div>'
    assert str(Elem(content=[Text(''), Text('')])) == '<div></div>'
    assert str(Elem(content=[Text('foo'), Text(''), Elem()])) == '<div>\n  foo\
\n  <div></div>\n</div>'
    print('Elem with empty texts : OK.')

    
def test_errors():
    # Type error if the content isn't made of Text or Elem.
    try:
        Elem(content=1)
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert str(Elem(content=Text(1))) == '<div>\n  1\n</div>'

    # Type error if the elements of the list aren't Text or Elem instances.
    try:
        Elem(content=['foo', Elem(), 1])
    except Exception as e:
        assert type(e) == Elem.ValidationError
    # The right way :
    assert (str(Elem(content=[Text('foo'), Elem(), Text(1)]))
            == '<div>\n  foo\n  <div></div>\n  1\n</div>')

    # Same with add_method()
    try:
        elem = Elem()
        elem.add_content(1)
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    
    # Or with lists :
    try :
        elem = Elem()
        elem.add_content([1,])
        raise(Exception('incorrect behaviour'))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)

    # str can't be used :
    try:
        elem = Elem()
        elem.add_content(['',])
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    
    try:
        elem = Elem(content='')
        raise(Exception("incorrect behaviour."))
    except Exception as e:
        assert isinstance(e, Elem.ValidationError)
    print('Error cases : OK.')


def test_embedding():
    assert (str(Elem(content=Elem(content=Elem(content=Elem()))))
            == """<div>
  <div>
    <div>
      <div></div>
    </div>
  </div>
</div>""")
    print('Element embedding : OK.')


def test():
    test_text()
    test_elem_basics()
    test_embedding()
    test_empty_texts()
    test_errors()
    
if __name__ == '__main__':
    try:
        # Create the HTML structure you requested
        html = Elem(
            tag="html",
            content=[
                Elem(
                    tag="head",
                    content=Elem(
                        tag="title",
                        content=Text("Hello ground!")
                    )
                ),
                Elem(
                    tag="body", 
                    content=[
                        Elem(
                            tag="h1",
                            content=Text('"Oh no, not again!"')
                        ),
                        Elem(
                            tag="img",
                            attr={"src": "http://i.imgur.com/pfp3T.jpg"},
                            tag_type="simple"
                        )
                    ]
                )
            ]
        )
        
        
        print(html)
        
        test()  
        print('Tests succeeded!')
    except AssertionError as e:
        traceback.print_exc()
        print(e)
        print('Tests failed!')
