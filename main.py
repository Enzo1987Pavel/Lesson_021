from run import Request, shop, store


while True:
	print(f"\nСКЛАД\n========\n{store}========\n")
	print(f"МАГАЗИН\n========\n{shop}========\n")

	user_req = input("""Введите необходимую задачу:\n
						
					""")
	if user_req == "стоп" or user_req == "stop":
		print("Действие завершено пользователем!")
		break
	else:
		try:
			req = Request(user_req)
			req.move()
		except Exception as e:
			print(f"Произошла ошибка ввода задачи: {e}.")
