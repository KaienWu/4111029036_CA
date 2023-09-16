def memory_addressing(page_size):
    try:
        page_table = {}
        num_entries = int(input("請輸入頁表數量: "))
        
        for _ in range(num_entries):
            page_number = int(input("請輸入頁號: "))
            frame_number = int(input(f"請輸入頁號 {page_number} 對應的幀號: "))
            page_table[page_number] = frame_number

        logical_address = int(input("請輸入logical address: "))
        page_number, offset = divmod(logical_address, page_size)

        if page_number in page_table:
            frame_number = page_table[page_number]
            physical_address = frame_number * page_size + offset
            print(f"Physical address 是 {physical_address}")
        else:
            print("無效的Page number")
    except ValueError:
        print("輸入無效，請輸入整數值。")
page_size = 4096

memory_addressing(page_size)
