scrollbar_stylesheet = """
    QScrollBar:vertical {
        border: none;
        background: #f0f0f0; /* Track color */
        width: 10px;
        margin: 0px;
    }
    QScrollBar::handle:vertical {
        background: #c0c0c0; /* Handle color */
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::handle:vertical:hover {
        background: #a0a0a0; /* Hover color */
    QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {
        height: 0px;
        background: none;
    }
    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        background: none;
    }
    """
