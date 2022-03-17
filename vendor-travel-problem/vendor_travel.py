from ortools.linear_solver import pywraplp


def main():
    """
    entry point for solving the mathematical model
    """
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Set
    total_day = 7
    total_position = 5
    big_m = 1000

    # Paramenters
    max_walk_unit = 40
    max_size_in_one_unit = [5, 5, 10, 10, 10]
    min_revenue = 10000
    revenue_per_unit = 20
    energe = [5, 5, 10, 15, 20]
    bonus = [20, 40, 60, 60, 60]
    extra_effort = [20, 40, 100, 100, 120]
    extra_bonus = [40, 80, 240, 240, 300]

    # Define the variables
    x_var = [
        solver.IntVar(0, max_walk_unit, '') for day in range(total_day)
    ]
    y_var = [
        [solver.IntVar(0, max_size_in_one_unit[m], '') for m in range(total_position)] for day in range(total_day)
    ]
    z_var = [
        [solver.IntVar(0, 1, '') for m in range(total_position)] for day in range(total_day)
    ]
    w_var = [
        [solver.IntVar(0, 1, '') for m in range(total_position)] for day in range(total_day)
    ]

    # Define the constraints
    # the lower bound of the revenue
    bounus_revenue = 0
    extra_effor_bonus_revenue = 0
    for i in range(total_day):
        for m in range(total_position):
            bounus_revenue += (z_var[i][m] * bonus[m])
            extra_effor_bonus_revenue += w_var[i][m] * extra_bonus[m]

    solver.Add(revenue_per_unit*sum(x_var) + bounus_revenue +
               extra_effor_bonus_revenue >= min_revenue)

    # tiredeness function
    for i in range(total_day):
        solver.Add(sum(y_var[i][m] for m in range(total_position)) == x_var[i])
        for m in range(total_position):
            solver.Add(max_size_in_one_unit[m]*z_var[i][m] <= y_var[i][m])
            if m > 0:
                solver.Add(y_var[i][m] <= big_m * z_var[i][m-1])
            if m < total_position - 1:
                solver.Add(z_var[i][m] >= z_var[i][m+1])
            # relation between z and w
            solver.Add(z_var[i][m] >= w_var[i][m])

    solver.NumConstraints()

    # define the objective
    tiredness = 0
    for i in range(total_day):
        for m in range(total_position):
            tiredness += (energe[m]*y_var[i][m] + extra_effort[m]*w_var[i][m])
    solver.Minimize(tiredness)

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
    for i in range(total_day):
        print(list(map(get_solution_value, y_var[i])))
    print('----z----')
    for i in range(total_day):
        print(list(map(get_solution_value, z_var[i])))
    print('----w----')
    for i in range(total_day):
        print(list(map(get_solution_value, w_var[i])))


if __name__ == '__main__':
    main()
