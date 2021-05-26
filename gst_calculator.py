def Calculate_GST(item_price: int, gst_percentage: float):
    total_cost = item_price + item_price*gst_percentage/100
    return total_cost

if __name__ == "__main__":
    print(Calculate_GST(1000, 1.2))