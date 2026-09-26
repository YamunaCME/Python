product_name=input("enter product name:").strip().lower()
product_id=input("enter price:")
result=f"{product_name[:3].upper()}-{product_id.zfill(4)}"
print(result)
