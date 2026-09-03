from fastapi import APIRouter

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@router.get("/")
def get_teachers():
    return {
        "message": "List of teachers"
    }


@router.get("/{teacher_id}")
def get_teacher(teacher_id: int):
    return {
        "teacher_id": teacher_id,
        "message": "Teacher details"
    }


@router.post("/")
def create_teacher(name: str, subject: str):
    return {
        "message": "Teacher created",
        "name": name,
        "subject": subject
    }