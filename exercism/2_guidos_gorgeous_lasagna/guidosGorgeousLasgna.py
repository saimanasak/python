def lasagna():
    while True:
        print("""\n*** WELCOME TO LASAGNA COOKING ASSISTANT ***
                1. Calculate Remaining Bake Time
                2. Calculate Preparation Time
                3. Calculate Total Elapsed Cooking Time
                4. Exit
""")

        choice = int(input("Enter your choice: "))

        total_time = 40
        layer_time = 2

        match choice:
            case 1:
                elapsed_bake_time = int(input("Enter elapsed bake time: "))
                remaining_bake_time = total_time - elapsed_bake_time

                print("\nRemaining bake time:", remaining_bake_time, "minutes.")

            case 2:
                layers = int(input("Enter number of layers: "))
                prep_time = layers * layer_time

                print("\nPreparation Time:", prep_time, "minutes.")

            case 3:
                layers = int(input("Enter number of layers: "))
                elapsed_time = int(input("Enter elapsed bake time: "))
                prep_time = layers * layer_time
                total_elapsed_time = prep_time + elapsed_time

                print("\nTotal elapsed cooking time:", total_elapsed_time, "minutes.")

            case 4:
                print("\nThank you for using the Lasagna Cooking Assistant...!!!")
                break

            case _:
                print("\nEnter a choice from 1 to 4!")


lasagna()