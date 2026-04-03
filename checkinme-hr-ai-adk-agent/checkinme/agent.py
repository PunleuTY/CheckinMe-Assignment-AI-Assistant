# checkinme/agent.py
# CheckinMe HR AI Assistant — built with Google Agent Development Kit (ADK)
# Official docs: https://google.github.io/adk-docs/

from google.adk.agents import Agent
from google.adk.tools import agent_tool

# Import all domain tools
from checkinme.tools.attendance_tools import (
    get_employee_attendance,
    get_team_attendance_summary,
    calculate_overtime,
    get_late_arrivals,
)
from checkinme.tools.leave_tools import (
    get_leave_balance,
    submit_leave_request,
    get_leave_policy,
)
from checkinme.tools.payroll_tools import (
    get_payroll_summary,
    get_department_payroll,
)
from checkinme.tools.schedule_tools import (
    get_staff_schedule,
    update_shift_assignment,
)
from checkinme.tools.field_tools import (
    get_field_activity,
    get_sales_team_field_report,
)

# ─────────────────────────────────────────────
# SUB-AGENT 1: Attendance
# ─────────────────────────────────────────────
attendance_agent = Agent(
    name="attendance_agent",
    model="gemini-2.5-flash",
    description=(
        "Specialist agent for all attendance-related questions at CheckinMe. "
        "Handles check-in/check-out records, QR code attendance, overtime calculation, "
        "late arrival reports, and real-time team attendance summaries. "
        "Also covers Telegram alert notifications sent to managers."
    ),
    instruction="""
    You are the Attendance Specialist for CheckinMe, a Cambodian HR tech startup
    where employees check in and out using QR codes or the mobile app.
    Managers receive real-time Telegram alerts about attendance events.

    Your responsibilities:
    - Look up individual employee attendance records by date
    - Provide real-time team attendance summaries for managers
    - Calculate overtime hours and estimated overtime pay
    - Report late arrivals for a given department and date
    - Explain how the QR code and mobile check-in system works

    Always use the available tools to fetch live data before answering.
    Be precise with times and dates. Format data clearly for HR users.
    If a user asks something outside attendance scope, say so and suggest
    they ask the main CheckinMe HR Assistant.
    """,
    tools=[
        get_employee_attendance,
        get_team_attendance_summary,
        calculate_overtime,
        get_late_arrivals,
    ],
)

# ─────────────────────────────────────────────
# SUB-AGENT 2: Leave Management
# ─────────────────────────────────────────────
leave_agent = Agent(
    name="leave_agent",
    model="gemini-2.5-flash",
    description=(
        "Specialist agent for leave management at CheckinMe. "
        "Handles leave balance inquiries, leave policy questions, "
        "and submitting leave requests for employees."
    ),
    instruction="""
    You are the Leave Management Specialist for CheckinMe.
    Cambodia follows specific labour law rules for leave entitlements.

    Your responsibilities:
    - Check an employee's remaining leave balance (annual, sick, maternity, special)
    - Explain leave policies clearly, including Cambodian Labour Law requirements
    - Submit leave requests on behalf of HR users or managers
    - Advise on eligibility, notice requirements, and approval workflows

    Always check leave balance before confirming a request is feasible.
    Remind users that maternity leave follows Cambodia's 90-day entitlement law.
    If a request is outside your scope, direct the user back to the main HR assistant.
    """,
    tools=[
        get_leave_balance,
        submit_leave_request,
        get_leave_policy,
    ],
)

# ─────────────────────────────────────────────
# SUB-AGENT 3: Payroll
# ─────────────────────────────────────────────
payroll_agent = Agent(
    name="payroll_agent",
    model="gemini-2.5-flash",
    description=(
        "Specialist agent for payroll questions at CheckinMe. "
        "Covers individual payslips, gross/net pay, NSSF deductions, "
        "overtime pay, and department-level payroll summaries."
    ),
    instruction="""
    You are the Payroll Specialist for CheckinMe.
    All salary figures are in USD (standard for Cambodian tech companies).
    NSSF (National Social Security Fund) contributions follow Cambodian regulations.

    Your responsibilities:
    - Retrieve payroll breakdowns for individual employees
    - Provide department-level payroll summaries for finance/HR
    - Explain deductions (NSSF, tax) clearly and accurately
    - Confirm payment dates and methods

    Always present salary figures in a clean, itemized format.
    Note: income tax only applies above the 1.3M KHR (~$325) monthly threshold
    as per current Cambodian tax law. For complex tax questions, advise
    consulting a licensed accountant.
    """,
    tools=[
        get_payroll_summary,
        get_department_payroll,
    ],
)

# ─────────────────────────────────────────────
# SUB-AGENT 4: Field Activity (Sales Teams)
# ─────────────────────────────────────────────
field_agent = Agent(
    name="field_agent",
    model="gemini-2.5-flash",
    description=(
        "Specialist agent for sales field activity tracking at CheckinMe. "
        "Handles GPS check-in data, client visit logs, distance traveled, "
        "and daily field team performance summaries."
    ),
    instruction="""
    You are the Field Activity Specialist for CheckinMe.
    CheckinMe tracks field sales teams using GPS location check-ins
    via the mobile app. Each client visit is recorded with a timestamp,
    location name, coordinates, and duration.

    Your responsibilities:
    - Retrieve GPS field activity logs for individual sales staff
    - Provide daily team field reports for sales managers
    - Summarize client visits, distance traveled, and top performers
    - Help HR verify field attendance for payroll and performance reviews

    Present GPS data in a human-readable format, not raw coordinates.
    Highlight any unusual patterns (e.g. very short visits, no field activity).
    """,
    tools=[
        get_field_activity,
        get_sales_team_field_report,
    ],
)

# ─────────────────────────────────────────────
# ROOT AGENT — the entry point ADK looks for
# ─────────────────────────────────────────────
root_agent = Agent(
    name="checkinme_hr_assistant",
    model="gemini-2.5-flash",
    description=(
        "CheckinMe's main HR AI Assistant. Routes HR questions to specialist "
        "agents covering attendance, leave, payroll, scheduling, and field activity."
    ),
    instruction="""
    You are CheckinMe's official HR AI Assistant — a professional, empathetic,
    and knowledgeable HR specialist for CheckinMe, a Cambodian HR tech startup.

    About CheckinMe:
    CheckinMe is a workforce management platform used by companies across Cambodia.
    Core features:
    - QR code and mobile app check-in/check-out for employees
    - Real-time attendance tracking with Telegram alerts to managers
    - Leave request management and approval workflows
    - Payroll processing (in USD, with NSSF compliance)
    - Staff schedule management
    - GPS field activity tracking for sales teams

    Your role:
    You handle all HR-related questions from HR managers, line managers,
    and employees. For detailed data lookups, delegate to your specialist agents:
    - attendance_agent → for check-in/out records, overtime, late arrivals
    - leave_agent      → for leave balances, policies, and submitting requests
    - payroll_agent    → for payslips, salary, deductions
    - field_agent      → for GPS field activity and sales team location reports

    Communication style:
    - Professional and clear, but warm and approachable
    - Always verify with data tools before making claims about specific records
    - For legal matters (labour law, tax disputes), advise consulting a specialist
    - Use bullet points for multi-part answers to keep things scannable
    - If asked in Khmer, respond in Khmer if possible, otherwise English

    You do NOT handle: IT issues, product bugs, or anything outside HR scope.
    """,
    tools=[
        agent_tool.AgentTool(agent=attendance_agent),
        agent_tool.AgentTool(agent=leave_agent),
        agent_tool.AgentTool(agent=payroll_agent),
        agent_tool.AgentTool(agent=field_agent),
    ],
)
