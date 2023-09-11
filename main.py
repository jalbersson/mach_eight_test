def sums(array, target):
    """
        A function that returns all the possible combinations inside an array
        that will sum the target.

        Parameters
        ----------
        array : int []
            The input array were there might be elements that sum the target
        target : int
            the wanted result of the addition of the array two elements

        Returns
        -------
        A dictionary containing the possible elements which added, sum the target
    """
    main_map = {}
    result_map = {}

    # save the values inside a dictionary, so I can look for them in O(1)
    #  complexity in a single pass
    for i, number in enumerate(array):
        main_map[number] = i

    # this loop is necessary because we need to have all the values in there before
    # searching for solutions
    for key in main_map:
        difference = target - key
        if difference in main_map:
            if key not in result_map and difference not in result_map:
                result_map[key] = difference
    return result_map


with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        parameters = line.split('  ')
        if len(parameters) == 2:
            target = int(parameters[1])
            striped_string = parameters[0].replace('[', '')
            striped_string = striped_string.replace(']', '')
            striped_string = striped_string.replace(',', '')
            string_array = striped_string.split(' ')
            array = list(map(int, string_array))
            print(sums(array, target))
