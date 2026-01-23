scrollbar_stylesheet = """
    QScrollBar:vertical {
        border: none;
        background: #000000; /* Track color */
        width: 5px;
        margin: 0px;
    }
    QScrollBar::handle:vertical {
        background: #000000; /* Handle color */
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background: #222222; /* Hover color */
    QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
        height: 0px;
        background: 222222;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: 222222;
    }
    """
