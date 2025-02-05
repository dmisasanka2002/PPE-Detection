from gui.main_window import create_first_window


def main():
    
    app_title = 'PPE Detection'
    check_items = ['Helmet', 'Gloves', 'Vest', 'Boots', 'Goggles']

    # Start the GUI by calling the first window
    create_first_window(title=app_title, items=check_items)

    return

if __name__ == '__main__':
    main()