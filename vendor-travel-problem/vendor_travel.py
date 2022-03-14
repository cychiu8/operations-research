from ortools.linear_solver import pywraplp
import numpy

# Create the mip solver with the SCIP backend.
solver = pywraplp.Solver.CreateSolver('SCIP')

infinity = solver.infinity()

# Set
TOTAL_DAY = 7
TOTAL_POSITION = 5
BIG_M = 1000

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
    solver.IntVar(0, max_walk_unit, '') for day in range(TOTAL_DAY)
]
y_var = [
    [solver.IntVar(0, max_size_in_one_unit[m], '') for m in range(TOTAL_POSITION)] for day in range(TOTAL_DAY)
]
z_var = [
    [solver.IntVar(0, 1, '') for m in range(TOTAL_POSITION)] for day in range(TOTAL_DAY)
]
w_var = [
    [solver.IntVar(0, 1, '') for m in range(TOTAL_POSITION)] for day in range(TOTAL_DAY)
]


# Define the constraints
# the lower bound of the revenue
bounus_revenue = 0
extra_effor_bonus_revenue = 0
for i in range(TOTAL_DAY):
    for m in range(TOTAL_POSITION):
        bounus_revenue += (z_var[i][m] * bonus[m])
        extra_effor_bonus_revenue += w_var[i][m] * extra_bonus[m]

solver.Add(revenue_per_unit*sum(x_var) + bounus_revenue +
           extra_effor_bonus_revenue >= min_revenue)

# tiredeness function
for i in range(TOTAL_DAY):
    solver.Add(sum(y_var[i][m] for m in range(TOTAL_POSITION)) == x_var[i])
    for m in range(TOTAL_POSITION):
        solver.Add(max_size_in_one_unit[m]*z_var[i][m] <= y_var[i][m])
        if m > 0:
            solver.Add(y_var[i][m] <= BIG_M * z_var[i][m-1])
        if m < TOTAL_POSITION - 1:
            solver.Add(z_var[i][m] >= z_var[i][m+1])
        # relation between z and w
        solver.Add(z_var[i][m] >= w_var[i][m])

solver.NumConstraints()

# define the objective
tiredness = 0
for i in range(TOTAL_DAY):
    for m in range(TOTAL_POSITION):
        tiredness += (energe[m]*y_var[i][m] + extra_effort[m]*w_var[i][m])
solver.Minimize(tiredness)

status = solver.Solve()


# Display the solution
if status == pywraplp.Solver.OPTIMAL:
    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    for i in range(TOTAL_DAY):
        print('x[[' + str(i) + '] = ', x_var[i].solution_value())
else:
    print('The problem does not have an optimal solution.')

print('\nAdvanced usage:')
print('Problem solved in %f milliseconds' % solver.wall_time())
print('Problem solved in %d iterations' % solver.iterations())
print('Problem solved in %d branch-and-bound nodes' % solver.nodes())


def getSolution_value(x): return x.solution_value()


print('----x----')
print(list(map(getSolution_value, x_var)))

print('----y----')
for i in range(TOTAL_DAY):
    print(list(map(getSolution_value, y_var[i])))

print('----z----')
for i in range(TOTAL_DAY):
    print(list(map(getSolution_value, z_var[i])))
print('----w----')
for i in range(TOTAL_DAY):
    print(list(map(getSolution_value, w_var[i])))
