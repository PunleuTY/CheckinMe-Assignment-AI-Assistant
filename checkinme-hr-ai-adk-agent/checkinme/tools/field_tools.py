# Field activity tools for sales teams — GPS, location check-ins
def get_field_activity(employee_id: str, date: str) -> dict:
    """
    Returns GPS-tracked field activity for a sales employee on a given date.
    Use this when a sales manager or HR wants to review where a field
    representative visited and how long they spent at each location.

    Args:
        employee_id: The sales employee's unique ID
        date: Date in YYYY-MM-DD format
    """
    return {
        "status": "success",
        "employee_id": employee_id,
        "date": date,
        "total_locations_visited": 5,
        "total_distance_km": 34.2,
        "check_ins": [
            {
                "time": "08:30 AM",
                "location": "Client A - Toul Kork",
                "duration_min": 45,
                "lat": 11.5788,
                "lng": 104.9117,
            },
            {
                "time": "10:15 AM",
                "location": "Client B - Daun Penh",
                "duration_min": 30,
                "lat": 11.5696,
                "lng": 104.9217,
            },
            {
                "time": "01:00 PM",
                "location": "Client C - Sen Sok",
                "duration_min": 60,
                "lat": 11.5935,
                "lng": 104.8926,
            },
            {
                "time": "03:30 PM",
                "location": "Client D - Chamkarmon",
                "duration_min": 35,
                "lat": 11.5511,
                "lng": 104.9282,
            },
        ],
    }


def get_sales_team_field_report(date: str) -> dict:
    """
    Returns a summary of field activity for the entire sales team on a given date.
    Use this for daily sales team reports or when management wants a team overview.

    Args:
        date: Date in YYYY-MM-DD format
    """
    return {
        "status": "success",
        "date": date,
        "team_size": 8,
        "active_in_field": 6,
        "office_based": 2,
        "total_client_visits": 28,
        "top_performer": {"name": "Rina Keo", "visits": 7, "distance_km": 52.1},
    }
