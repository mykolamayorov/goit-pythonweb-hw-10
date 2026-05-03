import cloudinary
import cloudinary.uploader

from app.config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET


cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True,
)


def upload_avatar(file_obj, public_id: str) -> str:
    """
    Upload avatar image to Cloudinary and return secure URL.
    file_obj: file-like object (e.g., UploadFile.file)
    """
    result = cloudinary.uploader.upload(
        file_obj,
        folder="avatars",
        public_id=public_id,
        overwrite=True,
        resource_type="image",
    )
    url = result.get("secure_url")
    if not url:
        raise RuntimeError("Cloudinary did not return secure_url")
    return url