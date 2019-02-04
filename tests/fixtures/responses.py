body_no_links = """
<head>
    <title>No links</title>
</head>
</html>
"""

body_index_empty_link = """
<head>
    <title>Index empty link</title>
</head>
<body>
    <a href="http://0.0.0.0/site.html">Site</a>
</body>
</html>
"""

body_index_site_link = """
<head>
    <title>Test</title>
</head>
<body>
    <a href="http://0.0.0.0/site.html">Site</a>
</body>
</html>
"""

body_site_empty_link = """
<head>
    <title>Site no links</title>
</head>
</html>
"""

body_index_external_link = """
<head>
    <title>External Link</title>
</head>
<body>
    <a href="http://clearcode.pl">External link</a>
</body>
</html>"""


body_index_redirects = """
<head>
    <title>External Link</title>
</head>
<body>
    <a href="http://0.0.0.0/site_redirects.html">External link</a>
</body>
</html>"""

body_site_redirects = """<head>
    <title>Site links to index</title>
</head>
<body>
    <a href="http://0.0.0.0">Link to index</a>
    <a href="http://clearcode.pl">External link</a>
    <a href="http://0.0.0.0/subsite.html">Subsite</a>
</body>
</html>"""

body_site_invalid_link = """
<head>
    <title>Invalid link</title>
</head>
<body>
    <a href="http://0.0.0.0/invalid_link.html">Broken link</a>
</body>
</html>
"""

body_site_invalid_content_link = """
<head>
    <title>Invalid link</title>
</head>
<body>
    <a href="http://0.0.0.0/invalid_content.txt">Invalid content</a>
</body>
</html>
"""
