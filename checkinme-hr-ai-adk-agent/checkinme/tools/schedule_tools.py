# Staff scheduling tools


def get_staff_schedule(department: str, week_start: str) -> dict:
    """
    Returns the staff schedule for a department for the week starting on a given date.
    Use this when HR or a manager needs to view or confirm shift assignments.

    Args:
        department: Department name
        week_start: The Monday of the week in YYYY-MM-DD format
    """
    return {
        "status": "success",
        "department": department,
        "week_start": week_start,
        "schedule": [
            {
                "employee": "Sokha Meas",
                "shift": "Morning 7AM-4PM",
                "days": ["Mon", "Tue", "Wed", "Thu", "Fri"],
            },
            {
                "employee": "Dara Pich",
                "shift": "Afternoon 1PM-9PM",
                "days": ["Mon", "Tue", "Wed", "Thu", "Sat"],
            },
            {
                "employee": "Leap Chan",
                "shift": "Morning 7AM-4PM",
                "days": ["Tue", "Wed", "Thu", "Fri", "Sat"],
            },
        ],
    }


def update_shift_assignment(
    employee_id: str, date: str, new_shift: str, reason: str
) -> dict:
    """
    Updates a shift assignment for an employee on a specific date.
    Use this when HR needs to reassign an employee's shift.

    Args:
        employee_id: The employee's unique ID
        date: Date of the shift change in YYYY-MM-DD format
        new_shift: The new shift to assign (e.g. 'Morning 7AM-4PM', 'Night 9PM-6AM')
        reason: Reason for the change
    """
    return {
        "status": "updated",
        "employee_id": employee_id,
        "date": date,
        "new_shift": new_shift,
        "reason": reason,
        "notification_sent": True,
    }
