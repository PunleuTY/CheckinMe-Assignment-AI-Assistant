# Leave request tools — balances, submissions, approvals


def get_leave_balance(employee_id: str) -> dict:
    """
    Returns the remaining leave balance for an employee.
    Use this when an employee or HR asks how many leave days are left,
    or before approving a leave request.

    Args:
        employee_id: The employee's unique ID
    """
    return {
        "status": "success",
        "employee_id": employee_id,
        "annual_leave_remaining": 9,
        "sick_leave_remaining": 5,
        "unpaid_leave_used": 0,
        "maternity_leave_remaining": 0,
        "special_leave_remaining": 2,
    }


def submit_leave_request(
    employee_id: str, leave_type: str, start_date: str, end_date: str, reason: str
) -> dict:
    """
    Submits a leave request on behalf of an employee.
    Use this when an HR user or manager wants to file a leave request.

    Args:
        employee_id: The employee's unique ID
        leave_type: Type of leave — 'annual', 'sick', 'maternity', 'unpaid', 'special'
        start_date: Leave start date in YYYY-MM-DD format
        end_date: Leave end date in YYYY-MM-DD format
        reason: Brief reason for the leave
    """
    return {
        "status": "submitted",
        "request_id": "LV-2025-0342",
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "pending_approval_from": "Line Manager",
        "telegram_notification_sent": True,
    }


def get_leave_policy(leave_type: str) -> dict:
    """
    Returns CheckinMe company leave policy for a specific leave type.
    Use this when an employee asks about entitlements, rules, or eligibility.

    Args:
        leave_type: Type of leave — 'annual', 'sick', 'maternity', 'unpaid', 'special'
    """
    policies = {
        "annual": {
            "days_per_year": 18,
            "carry_forward": "Up to 5 days may be carried forward to the next year",
            "notice_required": "At least 3 working days in advance",
            "approval": "Line Manager",
        },
        "sick": {
            "days_per_year": 14,
            "documentation": "Medical certificate required for 3+ consecutive days",
            "notice_required": "Notify manager on the same day by 9 AM",
            "approval": "HR Department",
        },
        "maternity": {
            "days": 90,
            "paid": "Full pay for first 3 months as per Cambodian Labour Law",
            "notice_required": "At least 30 days before expected due date",
            "approval": "HR Department",
        },
        "special": {
            "occasions": "Marriage (3 days), bereavement (3 days), official duty",
            "documentation": "Supporting documents required",
            "approval": "HR Director",
        },
    }
    policy = policies.get(leave_type.lower())
    if not policy:
        return {
            "status": "not_found",
            "message": f"No policy found for leave type: {leave_type}",
        }
    return {"status": "success", "leave_type": leave_type, "policy": policy}
