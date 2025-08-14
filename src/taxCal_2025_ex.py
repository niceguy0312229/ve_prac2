import numpy as np

def calculate_cpp(income):
    YMPE = 71300
    YAMPE = 81200
    exemption = 3500
    # Step 1: base CPP
    cpp1_base = max(0, min(income, YMPE) - exemption)
    cpp1 = cpp1_base * 0.0595
    # Step 2: additional CPP (CPP2)
    cpp2_base = max(0, min(income, YAMPE) - YMPE)
    cpp2 = cpp2_base * 0.04
    # Apply max total contributions for employees (2025 limit: $4,390.35, but summing both for here)
    cpp_total = round(cpp1 + cpp2, 2)
    # For 2025, employee max (sum both): should be ~$4,390.35, but check new year's CRA for latest.
    cpp_employee_max = 4390.35
    return min(cpp_total, cpp_employee_max)

def calculate_ei(income):
    ei_rate = 0.0166  # 2025 rate
    ei_max_earnings = 64950  # 2025 max insurable
    ei_max = 1077.48  # 2025 max employee contribution
    ei = min(income, ei_max_earnings) * ei_rate
    return round(min(ei, ei_max), 2)

def calculate_federal_tax(income):
    # Canada Employment Amount first
    canada_emp_amt = 1405
    federal_bpa = 16129
    # Subtract employment amount first (non-refundable)
    taxable = max(0, income - canada_emp_amt)
    # 2025 combined bracket (PIT) rates after July 1
    # Reference: [1]
    brackets = [
        (0, 57375, 0.145),          # 14.5%
        (57375, 114750, 0.205),     # 20.5%
        (114750, 177882, 0.26),     # 26%
        (177882, 253414, 0.29),     # 29%
        (253414, float('inf'), 0.33) # 33%
    ]
    tax = 0
    for lower, upper, rate in brackets:
        if taxable > lower:
            amount = min(taxable, upper) - lower
            if amount > 0:
                tax += amount * rate
    # Apply non-refundable federal BPA credit (at 14.5% rate)
    tax -= federal_bpa * 0.145
    return round(max(0, tax), 2)

def calculate_ontario_tax(income):
    ontario_bpa = 12656
    # 2025 Ontario brackets (unchanged July)
    brackets = [
        (0, 52886, 0.0505),
        (52886, 105775, 0.0915),
        (105775, 150000, 0.1116),
        (150000, 220000, 0.1216),
        (220000, float('inf'), 0.1316)
    ]
    tax = 0
    for lower, upper, rate in brackets:
        if income > lower:
            amount = min(income, upper) - lower
            if amount > 0:
                tax += amount * rate
    # Apply non-refundable ON BPA credit (at 5.05%)
    tax -= ontario_bpa * 0.0505
    # Ontario Health Premium (ref: ON finance 2025)
    ohp = 0
    if income > 20000:
        brackets_health = [
            (20000, 36000, lambda x: (x-20000)*0.06),
            (36000, 48000, lambda x: 960 + (x-36000)*0.06),
            (48000, 72000, lambda x: 1728 + (x-48000)*0.25),
            (72000, 200000, lambda x: 7328 + (x-72000)*0.25),
            (200000, float('inf'), lambda x: 900)
        ]
        for lower, upper, formula in brackets_health:
            if income > lower:
                tax_health = formula(min(income, upper))
                ohp = max(ohp, min(tax_health, 900))
    tax += ohp
    return round(max(0, tax), 2)

def calculate_total_tax(income):
    cpp = calculate_cpp(income)
    ei = calculate_ei(income)
    fed_tax = calculate_federal_tax(income)
    ont_tax = calculate_ontario_tax(income)
    total = cpp + ei + fed_tax + ont_tax
    net = income - total
    return {
        'CPP': cpp,
        'EI': ei,
        'Federal Tax': fed_tax,
        'Ontario Tax (+health premium)': ont_tax,
        'Total Tax': round(total, 2),
        'After-Tax Income': round(net, 2)
    }

# Example usage (for $100,000, $150,000, $200,000)
for salary in [100000, 178000, 200000]:
    print(f"\nGross Salary: ${salary:,}")
    result = calculate_total_tax(salary)
    for k, v in result.items():
        print(f"{k:25s}: ${v:,.2f}")



matrix1 = np.array([[1, 2],
                   [3, 4]])

print(matrix1.shape)  # (2, 2) → (rows, columns)
print(matrix1.size)   # 4     → total elements
print(matrix1[0][1])  # Outputs 2 (row 1, column 2 in MATLAB)
print(matrix1[1][0])  # Outputs 3 (row 2, column 1 in MATLAB)
print(len(matrix1))

matrix2 = np.array([[1, 2, 3 ], 
                    [4, 5, 6 ]])
print(matrix2.shape)