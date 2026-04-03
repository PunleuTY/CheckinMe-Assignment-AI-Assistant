# Attendance tools — check-in/out, QR, overtime, real-time tracking
from datetime import datetime


def get_employee_attendance(employee_id: str, date: str) -> dict:
    """
    Retrieves attendance record for a specific employee on a given date.
    Use this when an HR user asks about check-in/check-out times,
    attendance status, or whether an employee was present.

    Args:
        employee_id: The unique ID of the employee (e.g. 'EMP001')
        date: Date in YYYY-MM-DD format
    """
    # Sample data — we can just replace with real DB query
    return {
        "status": "success",
        "employee_id": employee_id,
        "date": date,
        "check_in": "08:05 AM",
        "check_out": "05:48 PM",
        "method": "QR Code",
        "location": "Head Office - Phnom Penh",
        "total_hours": 9.72,
        "overtime_hours": 1.72,
    }


def get_team_attendance_summary(department: str, date: str) -> dict:
    """
    Returns a real-time attendance summary for an entire department.
    Use this when a manager or HR asks how many people are present today
    or wants a team overview.

    Args:
        department: Department name (e.g. 'Sales', 'Engineering', 'Operations')
        date: Date in YYYY-MM-DD format
    """
    return {
        "status": "success",
        "department": department,
        "date": date,
        "total_staff": 24,
        "present": 21,
        "absent": 2,
        "on_leave": 1,
        "late_arrivals": 3,
        "telegram_alert_sent": True,
    }


def calculate_overtime(employee_id: str, month: str) -> dict:
    """
    Calculates total overtime hours for an employee in a given month.
    Use this for payroll preparation or when an employee disputes overtime.

    Args:
        employee_id: The employee's unique ID
        month: Month in YYYY-MM format (e.g. '2025-03')
    """
    return {
        "status": "success",
        "employee_id": employee_id,
        "month": month,
        "regular_hours": 176,
        "overtime_hours": 14.5,
        "overtime_rate": "1.5x",
        "estimated_overtime_pay_usd": 87.0,
    }


def get_late_arrivals(department: str, date: str) -> dict:
    """
    Returns a list of employees who arrived late on a given date.
    Useful for managers tracking punctuality or HR reviewing attendance.

    Args:
        department: Department name
        date: Date in YYYY-MM-DD format
    """
    return {
        "status": "success",
        "department": department,
        "date": date,
        "late_employees": [
            {
                "id": "EMP003",
                "name": "Sokha Meas",
                "arrived_at": "08:42 AM",
                "minutes_late": 42,
            },
            {
                "id": "EMP011",
                "name": "Dara Pich",
                "arrived_at": "09:15 AM",
                "minutes_late": 75,
            },
        ],
    }
