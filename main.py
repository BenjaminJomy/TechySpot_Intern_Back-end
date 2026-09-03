from fastapi import FastAPI

from student import router as student_router
from teacher import router as teacher_router
from admin import router as admin_router

app = FastAPI(title="School Management System")

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(admin_router)


@app.get("/")
def home():
    return {"message": "School Management API"}