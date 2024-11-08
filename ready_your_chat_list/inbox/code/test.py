from lxml import html

# Sample HTML snippet
html_content = '''<div class="_2ph_ _a6-h _a6-i">Ismail Han</div>'''

# Parse HTML content
tree = html.fromstring(html_content)

# Use XPath to locate the div with specific classes and extract text
main_text = tree.xpath('//div[contains(@class, "_2ph_") and contains(@class, "_a6-h") and contains(@class, "_a6-i")]/text()')

print(main_text[0])  # Output: Ismail Han
