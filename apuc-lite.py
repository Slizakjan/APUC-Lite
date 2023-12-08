from itertools import product
import math
import itertools
from itertools import permutations
import time
import os
import signal

list1 = []
gt_mode = [False]
output = None
user_input = None
version = 1.0

green = "\033[1;32;40m"
yellow = "\033[1;33;40m"
red = "\033[1;31;40m"
color_end = "\033[0;37;40m"

def title():
    print(f"    _    ____  _   _  ____      _     ___ _____ _____\n   / \  |  _ \| | | |/ ___|    | |   |_ _|_   _| ____|\n  / _ \ | |_) | | | | |   _____| |    | |  | | |  _|\n / ___ \|  __/| |_| | |__|_____| |___ | |  | | | |___\n/_/   \_\_|    \___/ \____|    |_____|___| |_| |_____|\n   Version: {version}")

#while True:
try:
    try:
        def signal_handler(sig, frame):
            user_input = input("\nDo you want continue? (y/n)\nApuc-lite:> ")
            if user_input.lower() == 'y':
                signal.signal(signal.SIGINT, signal_handler)  # znovu nastavíme handler pro SIGINT
            else:
                exit()

        signal.signal(signal.SIGINT, signal_handler)


        def large_calculate(all_combinations, word_size=5):
            size_in_bytes = all_combinations * word_size

            size_in_units = size_in_bytes
            units = ['B', 'KB', 'MB', 'GB', 'TB']

            for unit in units:
                if size_in_units < 1024.0:
                    return f"{size_in_units:.2f} {unit}"
                size_in_units /= 1024.0
            return size_in_units

        def calculate_percentage(wordcount, all_combinations):
            if all_combinations == 0:
                return 0  # Zabrání dělení nulou

            percentage = (wordcount / all_combinations) * 100
            #if percentage <= 30:
            #    percentage = f"{red}{percentage}{color_end}"
            #elif percentage >= 30 and percentage <= 60:
            #    percentage = f"{yellow}{percentage}{color_end}"
            #else:
            #    percentage = f"{green}{percentage}{color_end}"
            return percentage

        def calculate_old_special_setting(how_repeat, custom_range_one, custom_range_two, more_setting_handler):
            all_combinations = 0
            if more_setting_handler == "y":
                print("Calculating, this can take a while")
                for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                            for combination in permutations(list1, i):
                                all_combinations += 1
            else:
                print("Calculating, this can take a while")
                for combination in permutations(list1, how_repeat):
                    all_combinations += 1
                    print(f"\r{all_combinations}", end='', flush=True)
            return all_combinations

        def combinator_old_special_setting(file_name, how_repeat, more_setting_handler, custom_range_one, custom_range_two):
            try:
                wordcount = 0
                output = "\nPasswords saved in " + file_name
                if gt_mode[0]:
                    print("Using GT Mode\n")
                    if more_setting_handler == "y":
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                                for combination in permutations(list1, i):
                                    combined_word = ''.join(combination)
                                    file.write(combined_word + '\n')  # Zápis slova do souboru

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)

                    else:
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pr>
                            for combination in permutations(list1, how_repeat):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
                    
                else:
                    if more_setting_handler == "y":
                        all_combinations = calculate_old_special_setting(how_repeat, custom_range_one, custom_range_two, more_setting_handler)
                        list2 = []  # Vytvořte prázdný seznam pro uložení slov
                        size_in_result = large_calculate(all_combinations)
                        print(size_in_result)
                        print(f"Generating {all_combinations} combinations, please wait")
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                                for combination in permutations(list1, i):
                                    combined_word = ''.join(combination)
                                    file.write(combined_word + '\n')  # Zápis slova do souboru
                                    generating_status = True
                                    wordcount += 1
                                    if wordcount % 2000 == 0:
                                        percentage_generated = calculate_percentage(wordcount, all_combinations)
                                        print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
                    else:
                        all_combinations = calculate_old_special_setting(how_repeat, None, None, None)
                        list2 = []  # Vytvořte prázdný seznam pro uložení slov
                        size_in_result = large_calculate(all_combinations)
                        print(size_in_result)
                        print(f"Generating {all_combinations} combinations, please wait")
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pr>
                            for combination in permutations(list1, how_repeat):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova
                                generating_status = True
                                wordcount += 1
                                if wordcount % 2000 == 0:
                                    percentage_generated = calculate_percentage(wordcount, all_combinations)
                                    print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
            except KeyboardInterrupt:
                user_input = input("\nDo you want continue? (y/n)\nApuc-lite:> ")
                if user_input.lower() == 'y' or user_input.lower() == 'Y':
                    signal.signal(signal.SIGINT, signal_handler)  # znovu nastavíme handler pro SIGINT
                else:
                    exit()

        def calculate_new_special_setting(how_repeat, custom_range_one, custom_range_two, more_setting_handler):
            all_combinations = 0
            print("Calculating, this can take a while")
            if more_setting_handler == "y":
                for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                    for combination in product(list1, repeat=i):
                        all_combinations += 1

            else:
                for combination in product(list1, repeat=how_repeat):
                    all_combinations += 1
            return all_combinations

        def combinator_new_special_setting(file_name, how_repeat, more_setting_handler, custom_range_one, custom_range_two):
            try:
                wordcount = 0
                output = "\nPasswords saved in " + file_name
                if gt_mode[0]:
                    print("Using GT Mode\n")
                    if more_setting_handler == "y":
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                                for combination in product(list1, repeat=i):
                                    combined_word = ''.join(combination)
                                    file.write(combined_word + '\n')  # Zápis slova do souboru

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
                    else:
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for combination in product(list1, repeat=how_repeat):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)

                else:
                    if more_setting_handler == "y":
                        all_combinations = calculate_new_special_setting(None, custom_range_one, custom_range_two, more_setting_handler)
                        list2 = []  # Vytvořte prázdný seznam pro uložení slov
                        size_in_result = large_calculate(all_combinations)
                        print(size_in_result)
                        print(f"Generating {all_combinations} combinations, please wait")
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for i in range(custom_range_one, custom_range_two):  # Generovat slova s 4 až 6 slovy
                                for combination in product(list1, repeat=i):
                                    combined_word = ''.join(combination)
                                    file.write(combined_word + '\n')  # Zápis slova do souboru
                                    generating_status = True
                                    wordcount += 1
                                    if wordcount % 2000 == 0:
                                        percentage_generated = calculate_percentage(wordcount, all_combinations)
                                        print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
                    else:
                        all_combinations = calculate_new_special_setting(how_repeat, None, None, None)
                        list2 = []  # Vytvořte prázdný seznam pro uložení slov
                        size_in_result = large_calculate(all_combinations)
                        print(size_in_result)
                        print(f"Generating {all_combinations} combinations, please wait")
                        start_time = time.time()
                        with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                            for combination in product(list1, repeat=how_repeat):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru
                                generating_status = True
                                wordcount += 1
                                if wordcount % 2000 == 0:
                                    percentage_generated = calculate_percentage(wordcount, all_combinations)
                                    print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                        menu(output)
            except KeyboardInterrupt:
                user_input = input("\nDo you want continue? (y/n)\nApuc-lite:> ")
                if user_input.lower() == 'y' or user_input.lower() == 'Y':
                    signal.signal(signal.SIGINT, signal_handler)  # znovu nastavíme handler pro SIGINT
                else:
                    exit()

        def calculate_new():
            all_combinations = 0
            print("Calculating, this can take a while")
            for i in range(1, len(list1) + 1):
                for combination in product(list1, repeat=i):
                    all_combinations += 1
            return all_combinations

        def combinator_new(file_name):
            try:
                wordcount = 0
                output = "\nPasswords saved in " + file_name
                if gt_mode[0]:
                    print("Using GT Mode\n")
                    start_time = time.time()
                    with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                        for i in range(1, len(list1) + 1):
                            for combination in product(list1, repeat=i):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru

                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                    menu(output)
                else:
                    all_combinations = calculate_new()
                    list2 = []  # Vytvořte prázdný seznam pro uložení slov
                    size_in_result = large_calculate(all_combinations)
                    print(size_in_result)
                    print(f"Generating {all_combinations} combinations, please wait")
                    start_time = time.time()
                    with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                        for i in range(1, len(list1) + 1):
                            for combination in product(list1, repeat=i):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru
                                generating_status = True
                                wordcount += 1
                                if wordcount % 2000 == 0:
                                    percentage_generated = calculate_percentage(wordcount, all_combinations)
                                    print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                    menu(output)
            except KeyboardInterrupt:
                user_input = input("\nDo you want continue? (y/n)\nApuc-lite:> ")
                if user_input.lower() == 'y' or user_input.lower() == 'Y':
                    signal.signal(signal.SIGINT, signal_handler)  # znovu nastavíme handler pro SIGINT
                else:
                    exit()


        def calculate_old():
            combinations = 0
            for i in range(1, len(list1) + 1):
                for combination in permutations(list1, i):
                    combinations += 1
            return combinations

        def combinator_old(file_name):
            try:
                wordcount = 0
                output = "\nPasswords saved in " + file_name
                if gt_mode[0]:
                    print("Using GT Mode\n")
                    start_time = time.time()
                    with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                        for i in range(1, len(list1) + 1):
                            for combination in permutations(list1, i):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru

                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                    menu(output)
                else:
                    print(list1)
                    all_combinations = calculate_old()
                    list2 = []  # Vytvořte prázdný seznam pro uložení slov
                    size_in_result = large_calculate(all_combinations)
                    print(size_in_result)
                    print(f"Generating {all_combinations} combinations, please wait")
                    start_time = time.time()
                    with open(file_name, 'w') as file:  # Otevření souboru pro zápis
                        for i in range(1, len(list1) + 1):
                            for combination in permutations(list1, i):
                                combined_word = ''.join(combination)
                                file.write(combined_word + '\n')  # Zápis slova do souboru
                                generating_status = True
                                wordcount += 1
                                if wordcount % 2000 == 0:
                                    percentage_generated = calculate_percentage(wordcount, all_combinations)
                                    print(f"\rDone: {percentage_generated:.2f}%", end='', flush=True)

                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        output = output + f" with {wordcount} words and taken {elapsed_time:.2f}s"
                    menu(output)
            except KeyboardInterrupt:
                user_input = input("\nDo you want continue? (y/n)\nApuc-lite:> ")
                if user_input.lower() == 'y' or user_input.lower() == 'Y':
                    signal.signal(signal.SIGINT, signal_handler)  # znovu nastavíme handler pro SIGINT
                else:
                    exit()

        def start_new(a):
            try:
                loop_handler = True
                os.system("clear")
                title()
                if gt_mode[0]:
                    print("\nGT Mode is ON")
                file_name = input("\nEnter file name.txt:> ")
                print("\nEnter word you want to make combination from")
                b = 1
                loop_handler = True
                while loop_handler:
                    b = input("\nApuc-Lite word(Leave with nothing to start):> ")
                    if b == "":
                        loop_handler = False
                        combinator_new(file_name)
                    else:
                        list1.append(b)
            except KeyboardInterrupt:
                print("Exiting")
                exit()

        def start_old(a):
            try:
                loop_handler = True
                os.system("clear")
                title()
                if gt_mode[0]:
                    print("\nGT Mode is ON")
                file_name = input("\nEnter file name.txt:> ")
                print("\nEnter word you want to make combination from")
                b = 1
                loop_handler = True
                while loop_handler:
                    b = input("\nApuc-Lite word(Leave with nothing to start):> ")
                    if b == "":
                        loop_handler = False
                        combinator_old(file_name)
                    else:
                        list1.append(b)
            except KeyboardInterrupt:
                print("Exiting")
                exit()

        def start_new_spec_sett(a):
            try:
                loop_handler = True
                os.system("clear")
                title()
                if gt_mode[0]:
                    print("\nGT Mode is ON")
                more_setting = input("\nAdvenced setting? Y/N:> ")
                def inputs():
                    if more_setting.lower() == "y":
                        print("\nSetting")
                        try:
                            custom_range_one = int(input("\nChosse custom range from:> "))
                            custom_range_two = int(input("To words:> "))
                            custom_range_two += 1
                            how_repeat = None
                            more_setting_handler = "y"
                            if custom_range_one > custom_range_two:
                                print("Cannot have first value bigger then second value")
                                inputs()
                            elif custom_range_one == custom_range_two:
                                print("Cannot have value one same as value two")
                                inputs()
                        except ValueError:
                            print("You can add only numbers, try again")
                            inputs()
                    if more_setting.lower() != "y":
                        try:
                            how_repeat = int(input("\nHow long words max? (mean combinated words)\nApuc-lite:> "))
                            custom_range_one = None
                            custom_range_two = None
                        except ValueError:
                            print("You can add only numbers, try again")
                            inputs()
                    file_name = input("\nEnter file name.txt:> ")
                    print("\nEnter word you want to make combination from")
                    b = 1
                    loop_handler = True
                    while loop_handler:
                        b = input("\nApuc-Lite word(Leave with nothing to start):> ")
                        if b == "":
                            loop_handler = False
                            combinator_new_special_setting(file_name, how_repeat, more_setting_handler, custom_range_one, custom_range_two)
                        else:
                            list1.append(b)
                inputs()
            except KeyboardInterrupt:
                print("Exiting")
                exit()

        def start_old_spec_sett(a):
            try:
                os.system("clear")
                title()
                if gt_mode[0]:
                    print("\nGT Mode is ON")
                more_setting = input("\nAdvenced setting? Y/N:> ")
                def inputs():
                    if more_setting.lower() == "y":
                        print("\nSetting")
                        try:
                            custom_range_one = int(input("\nChosse custom range from:> "))
                            custom_range_two = int(input("To words:> "))
                            custom_range_two += 1
                            how_repeat = None
                            more_setting_handler = "y"
                            if custom_range_one > custom_range_two:
                                print("Cannot have first value bigger then second value")
                                inputs()
                            elif custom_range_one == custom_range_two:
                                print("Cannot have value one same as value two")
                                inputs()
                        except ValueError:
                            print("You can add only number, try again\n")
                            inputs()
                    if more_setting.lower() != "y":
                        try:
                            how_repeat = int(input("\nHow long words max? (mean combinated words)\nApuc-lite:> "))
                            custom_range_one = None
                            custom_range_two = None
                        except ValueError:
                            print("You can add only numbers, try again")
                            inputs()
                    file_name = input("\nEnter file name.txt:> ")
                    print("\nEnter word you want to make combination from")
                    b = 1
                    loop_handler = True
                    while loop_handler:
                        b = input("\nApuc-Lite word(Leave with nothing to start):> ")
                        if b == "":
                            loop_handler = False
                            combinator_old_special_setting(file_name, how_repeat, more_setting_handler, custom_range_one, custom_range_two)
                        else:
                            list1.append(b)
                inputs()
            except KeyboardInterrupt:
                print("Exiting")
                exit()


        def menu(output):
            global gt_mode
            global list1
            list1 = []
            if gt_mode[0]:
                gt_mode_stat = "*"
            else:
                gt_mode_stat =" "
            os.system("clear")
            title()
            if output:
                print(output)
            menu_in = input(str(f"\n[0][{gt_mode_stat}] GT Mode\n\n[1] Start Old V\n[2] Start New V\n[3] Start Old with special setting\n[4] Start new with special setting\n[99] Exit\nApuc-Lite:> "))
            if menu_in == "0":
                if gt_mode[0]:
                    gt_mode = [False]
                    gt_mode_stat = "*"
                    menu(None)
                else:
                    gt_mode = [True]
                    gt_mode_stat = " "
                    menu(None)
            elif menu_in == "1":
                start_old("1")
            elif menu_in == "2":
                start_new("1")
            elif menu_in == "3":
                start_old_spec_sett("1")
            elif menu_in == "4":
                start_new_spec_sett("1")
            elif menu_in == "99":
                print("Exiting")
                exit()
            else:
                print("Wrong input, try again")
                time.sleep(1)
                menu()

        menu(output)
    except RuntimeError:
        print("Exiting")
        exit()
except KeyboardInterrupt:
    print("Exiting")
    exit()