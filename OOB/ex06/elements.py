from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag="html", attr=attr, content=content, tag_type="double")

class Head(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag="head", attr=attr, content=content, tag_type="double")

class Body(Elem):
    def __init__(self, content=None, attr=None):
        super().__init__(tag="body", attr=attr, content=content, tag_type="double")
        

class Title(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="title", attr=attr, content=content, tag_type="double")

class meta(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="meta", attr=attr, content=content, tag_type="simple")

class img(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="img", attr=attr, content=content, tag_type="simple")

class table(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="table", attr=attr, content=content, tag_type="double")

class tr(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="tr", attr=attr, content=content, tag_type="double")

class td(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="td", attr=attr, content=content, tag_type="double")


class th(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="th", attr=attr, content=content, tag_type="double")

class ul(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="ul", attr=attr, content=content, tag_type="double")

class li(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="li", attr=attr, content=content, tag_type="double")

class ol(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="ol", attr=attr, content=content, tag_type="double")

class h1(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="h1", attr=attr, content=content, tag_type="double")

class p(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="p", attr=attr, content=content, tag_type="double")

class h2(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="h2", attr=attr, content=content, tag_type="double")

class div(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="div", attr=attr, content=content, tag_type="double")

class span(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="span", attr=attr, content=content, tag_type="double")
class hr(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="hr", attr=attr, content=content, tag_type="simple")
class br(Elem):
    def __init__(self, content=None, attr=None):
         super().__init__(tag="br", attr=attr, content=content, tag_type="simple")




if __name__ == "__main__":
   html = Html([
    Head(Title(Text("Hello ground!"))),
    Body([
        h1(Text("Oh no, not again!")),
        img(attr={"src": "http://i.imgur.com/pfp3T.jpg"})
   ])])
   print(html)
