# Payroll tools — salary queries, payslips, deductions


def get_payroll_summary(employee_id: str, month: str) -> dict:
    """
    Returns the payroll breakdown for an employee for a specific month.
    Use this when HR asks about salary, deductions, net pay, or payslip details.

    Args:
        employee_id: The employee's unique ID
        month: Month in YYYY-MM format
    """
    return {
        "status": "success",
        "employee_id": employee_id,
        "month": month,
        "base_salary_usd": 800,
        "overtime_pay_usd": 87.0,
        "allowances_usd": 50,
        "gross_pay_usd": 937.0,
        "nssf_deduction_usd": 18.0,  # National Social Security Fund (Cambodia)
        "tax_deduction_usd": 0,  # Below tax threshold
        "net_pay_usd": 919.0,
        "payment_method": "Bank Transfer",
        "payment_date": f"{month}-25",
    }


def get_department_payroll(department: str, month: str) -> dict:
    """
    Returns aggregate payroll figures for an entire department.
    Use this when HR or finance needs a department-level payroll report.

    Args:
        department: Department name
        month: Month in YYYY-MM format
    """
    return {
        "status": "success",
        "department": department,
        "month": month,
        "total_headcount": 24,
        "total_gross_payroll_usd": 22488,
        "total_net_payroll_usd": 21984,
        "total_overtime_usd": 2088,
        "total_nssf_usd": 432,
    }
