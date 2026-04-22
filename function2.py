def click_handle():
    click = 0

    def handle_click():
        nonlocal click
        click += 1
        print(f"Clicked {click} times")

       

    return handle_click

handler=click_handle()  

handler()
handler()
handler()

print(handler.__closure__)


