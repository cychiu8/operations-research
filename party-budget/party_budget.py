from ortools.linear_solver import pywraplp


def main():
    """
    entry point for solving the mathematical model
    """
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')
    infinity = solver.infinity()

    # Set
    main_dish = ['Beef hamburger', 'Pork hamburger',
                 'Chicken hamburger', 'Fried Chicken']
    side_dish = ['Fries', 'Popcorn chicken', 'Smoothie', 'Salad']
    drinks = ['Coke', 'Sprite', 'Black tea', 'Green tea']
    hamburgers = ['Beef hamburger', 'Pork hamburger',
                  'Chicken hamburger']
    set_dish = ['Beef hamburger', 'Pork hamburger',
                'Chicken hamburger', 'Fried Chicken', 'Party']

    # Parameters
    main_price = {
        'Beef hamburger': 120, 'Pork hamburger': 100,
        'Chicken hamburger': 110, 'Fried Chicken': 60
    }
    side_price = {
        'Fries': 55, 'Popcorn chicken': 60, 'Smoothie': 45, 'Salad': 50
    }
    drinks_price = {
        'Coke': 30, 'Sprite': 30, 'Black tea': 25, 'Green tea': 25
    }
    set_price = {
        'Beef hamburger': 150, 'Pork hamburger': 130,
        'Chicken hamburger': 140, 'Fried Chicken': 150, 'Party': 200
    }
    total_main_need = 8
    total_side_need = 13
    total_hamburger_need = 4
    total_drink_need = 6
    extra_main = 1
    extra_side = 3
    extra_drinks = 2
    set_numbers = {
        'Beef hamburger': {
            'Beef hamburger': 1,
            'Fries': 1,
            'Coke': 1
        },
        'Pork hamburger': {
            'Pork hamburger': 1,
            'Popcorn chicken': 1,
            'Sprite': 1
        },
        'Chicken hamburger': {
            'Chicken hamburger': 1,
            'Smoothie': 1,
            'Black tea': 1
        },
        'Fried Chicken': {
            'Fried Chicken': 2,
            'Salad': 1,
            'Green tea': 1
        },
        'Party': {
            'Fried Chicken': 4,
            'Fries': 3,
            'Smoothie': 3,
            'Coke': 4
        }
    }
    main_need = {
        'Beef hamburger': 1, 'Pork hamburger': 0,
        'Chicken hamburger': 1, 'Fried Chicken': 3
    }
    side_need = {
        'Fries': 5, 'Popcorn chicken': 1, 'Smoothie': 4, 'Salad': 2
    }
    drinks_need = {
        'Coke': 2, 'Sprite': 2, 'Black tea': 1, 'Green tea': 0
    }

    # Define the variables
    x_var = [
        solver.IntVar(0, infinity, '') for m in range(len(main_dish))
    ]
    y_var = [
        solver.IntVar(0, infinity, '') for m in range(len(side_dish))
    ]
    z_var = [
        solver.IntVar(0, infinity, '') for m in range(len(drinks))
    ]
    w_var = [
        solver.IntVar(0, infinity, '') for m in range(len(set_dish))
    ]

    # Define the constraints
    total_main = 0
    total_hamburger = 0
    for idx, m in enumerate(main_dish):
        # number of main dish for each kind
        # number of main dish for all
        # number of hamburger
        num_main = x_var[idx]
        for jdx, s in enumerate(set_dish):
            num_main += w_var[jdx] * set_numbers[s].get(m, 0)
        solver.Add(num_main >= main_need[m])
        total_main += num_main
        if m in hamburgers:
            total_hamburger += num_main
    solver.Add(total_main_need + extra_main >= total_main >= total_main_need)
    solver.Add(total_hamburger >= total_hamburger_need)

    total_side = 0
    for idx, n in enumerate(side_dish):
        # number of side dish for each kind
        num_side = y_var[idx]
        for jdx, s in enumerate(set_dish):
            num_side += w_var[jdx] * set_numbers[s].get(n, 0)
        solver.Add(num_side >= side_need[n])
        total_side += num_side
    solver.Add(total_side_need + extra_side >= total_side >= total_side_need)

    total_drink = 0
    for idx, a in enumerate(drinks):
        # number of side dish for each kind
        num_drink = z_var[idx]
        for jdx, s in enumerate(set_dish):
            num_drink += w_var[jdx] * set_numbers[s].get(a, 0)
        solver.Add(num_drink >= drinks_need[a])
        total_drink += num_drink
    solver.Add(total_drink_need + extra_drinks >=
               total_drink >= total_drink_need)

    # define the objective
    total_cost = 0
    for idx, m in enumerate(main_dish):
        total_cost += main_price.get(m, 0) * x_var[idx]
    for idx, n in enumerate(side_dish):
        total_cost += side_price.get(n, 0) * y_var[idx]
    for idx, a in enumerate(drinks):
        total_cost += drinks_price.get(a, 0) * z_var[idx]
    for idx, s in enumerate(set_dish):
        total_cost += set_price.get(s, 0) * w_var[idx]

    solver.Minimize(total_cost)
    status = solver.Solve()

    def get_solution_value(x):
        """
        get the solution value from the decision variable
        """
        return x.solution_value()

    # Display the solution
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in {} milliseconds', solver.wall_time())
    print('Problem solved in {} iterations', solver.iterations())
    print('Problem solved in {} branch-and-bound nodes', solver.nodes())
    print('----x----')
    print(list(map(get_solution_value, x_var)))
    print('----y----')
    print(list(map(get_solution_value, y_var)))
    print('----z----')
    print(list(map(get_solution_value, z_var)))
    print('----w----')
    print(list(map(get_solution_value, w_var)))


if __name__ == '__main__':
    main()
