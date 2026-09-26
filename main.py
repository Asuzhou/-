shopping_cart = {}
print("欢迎使用购物车管理系统~")
menu = """
######## 购物车系统 ########
#       1.添加购物车       #
#       2.修改购物车       #
#       3.删除购物车       #
#       4.查询购物车       #
#       5.退出购物车       #
##########################"""
print(menu)#制作菜单

while True:
    choice = input("请选择要执行的操作（1~5）：")
    match choice:
        case "1":
            goods_name = input("请输入商品的名称：")
            goods_price = float(input("请输入商品的价格："))
            goods_num = int(input("请输入商品的数量："))
            if goods_name in shopping_cart:
                print("该商品已存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕~")

        case "2":
            goods_name = input("请输入要修改商品的名称：")
            goods_price = float(input("请输入新的商品的价格："))
            goods_num = int(input("请输入新的商品的数量："))
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改成功~")

        case "3":
            goods_name = input("请输入要删除商品的名称：")
            if goods_name not in shopping_cart:
                print("该商品不存在，请重新选择~")
            else:
                del shopping_cart[goods_name]

        case "4":
            for goods_name in shopping_cart:
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name},商品价格：{goods_info["price"]},商品数量：{goods_info["num"]}")

        case "5":
            print("Bye Bye~")
            break

        case _:
            print("没有这个选项，请重新选择")