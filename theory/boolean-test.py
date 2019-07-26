for A in [False, True]:
	for B in [False, True]:
		for C in [False, True]:
			print();

			# (alternate: `!(A || B) || ( (A || C) && !(B || !C) )`)

			if (not (A or B) or (A or C) and not (B or not C)):
				print(f"A: {A}, B: {B}, C: {C} --- 1");
			else:
				print(f"A: {A}, B: {B}, C: {C} --- 0");