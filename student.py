from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/")
def get_students():
    return {
        "message": "List of students"
    }


@router.get("/{student_id}")
def get_student(student_id: int):
    return {
        "student_id": student_id,
        "message": "Student details"
    }


@router.post("/")
def create_student(name: str, email: str):
    return {
        "message": "Student created",
        "name": name,
        "email": email
    }