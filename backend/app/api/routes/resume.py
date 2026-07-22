from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/api/v1/resume",
    tags=["Resume"],
)

resume_service = ResumeService()


@router.post(
    "/upload",
    status_code=status.HTTP_200_OK,
)
async def upload_resume(
    file: UploadFile = File(...),
):
    """
    Upload a resume and extract structured information.
    """

    try:

        candidate = await resume_service.process_resume(file)

        return {
            "success": True,
            "message": "Resume processed successfully.",
            "data": candidate,
        }

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

    except Exception:

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process resume.",
        )