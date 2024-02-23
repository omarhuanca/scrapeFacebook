from src.X import X


def main():
    x = X("config.txt")
    config_obj = x.read_config_path()
    x.fb_login(config_obj)

    item_option = input("Enter number value 1 or 2 or 3 or 4 or 5 or 6 or 7 to generate list: ")

    if item_option == "1":
        x.scrape_degrees_1st("1_1_")
        x.generate_basic_info("1_2_")
        x.generate_user_like_1st("1_3_")
    elif item_option == "2":
        x.scrape_2nd_degrees("2_1_")
        x.generate_basic_info("2_2_")
    elif item_option == "3":
        x.generate_user_like_from_list("2_3_")
    elif item_option == "4":
        x.generate_group_member("3_1_")
    elif item_option == "5":
        x.generate_follower("4_1_")
    elif item_option == "6":
        x.generate_following("5_1_")
    elif item_option == "7":
        x.generate_user_like_from_list("5_2_")
    else:
        print(
            "Invalid # of arguments specified. Use none to scrape your 1st degree connections, or specify the name of the CSV file as the first argument.")


if __name__ == "__main__":
    main()
