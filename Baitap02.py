# Dataset raw_cart:
raw_cart = [
    {"id": "SP1", "ten": " Áo sơ mi nam ", "gia": 150000, "sl": 2, "danh_muc": "Thời trang"},
    {"id": "SP2", "ten": "Quần tây ", "gia": 250000, "sl": 1, "danh_muc": "Thời trang"},
    {"id": "SP3", "ten": " Giày thể thao ", "gia": 450000, "sl": 1, "danh_muc": "Giày dép"},
    {"id": "SP4", "ten": "Tất cổ ngắn ", "gia": 30000, "sl": 5, "danh_muc": "Phụ kiện"}
]

for item in raw_cart:
    item['ten'] = item['ten'].strip()
    item['tong_tien'] = item['gia'] * item['sl']

new_product = {
    "id": "SP5",
    "ten": "Áo khoác",
    "gia": 320000,
    "sl": 1,
    "danh_muc": "Thời trang",
    "tong_tien": 320000
}
raw_cart.append(new_product)
raw_cart = [item for item in raw_cart if item['id'] != 'SP4']
print(raw_cart)


unique_category = {item['danh_muc'] for item in raw_cart}
San_pham_tren_200k = [item['ten'] for item in raw_cart if item['tong_tien'] > 200000]

print("Danh mục duy nhất (Set):", unique_category)
print("Sản phẩm > 200000 (List Comprehension):", San_pham_tren_200k)
