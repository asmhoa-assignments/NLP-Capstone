with open('../stream_output/output0') as main_file:
    prev = None
    i = 0
    for line in main_file:
        tokens = line.split('\t')
        if len(tokens) >= 5:
            country = tokens[4].lower()
            prev = '../country_output/output_country_{0}.txt'.format(country)
        with open(prev, 'a') as country_file:
            country_file.write(line.strip())
            country_file.write('\n')
        i += 1

    if i % 50000 == 0:
        print(i)
