from fastapi import APIRouter

router = APIRouter(
    prefix="/admins",
    tags=["Admins"]
)


@router.get("/")
def get_admins():
    return {
        "message": "List of admins"
    }


@router.get("/{admin_id}")
def get_admin(admin_id: int):
    return {
        "admin_id": admin_id,
        "message": "Admin details"
    }


@router.post("/")
def create_admin(name: str, email: str):
    return {
        "message": "Admin created",
        "name": name,
        "email": email
    }