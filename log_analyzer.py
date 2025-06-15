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

if __name__ == "__main__":
    analyze_log('log.txt', 'rapport.txt')
