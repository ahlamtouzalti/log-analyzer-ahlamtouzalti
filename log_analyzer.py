from colorama import Fore, Style

def analyze_log(file_path, output_path):
    error = warning = info = 0
    with open(file_path, 'r') as f:
        for line in f:
            if 'ERROR' in line:
                error += 1
            elif 'WARNING' in line:
                warning += 1
            elif 'INFO' in line:
                info += 1

    with open(output_path, 'w') as out:
        out.write(f"ERROR: {error}\nWARNING: {warning}\nINFO: {info}\n")

    # Affichage coloré dans le terminal
    print(Fore.RED + f"ERROR: {error}")
    print(Fore.YELLOW + f"WARNING: {warning}")
    print(Fore.GREEN + f"INFO: {info}" + Style.RESET_ALL)

if __name__ == "__main__":
    analyze_log('log.txt', 'rapport.txt')

