def define_env(env):

    def _darken(hex_color, factor=0.55):
        hex_color = hex_color.lstrip('#')
        r, g, b = (int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        return '#{:02x}{:02x}{:02x}'.format(
            int(r * factor), int(g * factor), int(b * factor)
        )

    @env.macro
    def book_covers():
        books = env.variables.get('books', [])
        items = []
        for book in books:
            color = book.get('color', '#1a1a2e')
            dark  = _darken(color)
            style = f'background: linear-gradient(145deg, {color}, {dark});'
            items.append(
                f'  <a href="{book["url"]}" class="book-cover" style="{style}">\n'
                f'    <span class="ba-author">{book["author"]}</span>\n'
                f'    <span class="ba-rule"></span>\n'
                f'    <span class="ba-title">{book["title"]}</span>\n'
                f'    <span class="ba-rule-bottom"></span>\n'
                f'    <span class="ba-publisher">AbelSantos.com.br</span>\n'
                f'  </a>'
            )
        return '<div class="book-grid">\n' + '\n'.join(items) + '\n</div>'
